# -*- coding: cp1251 -*-

class Figure :
    def __init__ ( self, texture, frag_texture, rotation0 ) :
        self.texture        = texture
        self.frag_texture   = frag_texture
        self.rotation0      = rotation0
        self.cells          = len ( rotation0 )
        self.center_x       = 0
        self.center_y       = 0


figures = \
{   'O' : Figure
    (   texture         = "res/game/064x064_o.png"
    ,   frag_texture    = "res/game/032x032_o_frag.png"
    ,   rotation0       = \
        [ [ 1, 1 ]
        , [ 1, 1 ] ]
    )
,   'J' : Figure
    (   texture         = "res/game/096x096_j.png"
    ,   frag_texture    = "res/game/032x032_j_frag.png"
    ,   rotation0       = \
        [ [ 0, 0, 0 ]
        , [ 1, 0, 0 ]
        , [ 1, 1, 1 ] ]
    )
,   'L' : Figure
    (   texture         = "res/game/096x096_l.png"
    ,   frag_texture    = "res/game/032x032_l_frag.png"
    ,   rotation0       = \
        [ [ 0, 0, 0 ]
        , [ 0, 0, 1 ]
        , [ 1, 1, 1 ] ]
    )
,   'S' : Figure
    (   texture         = "res/game/096x096_s.png"
    ,   frag_texture    = "res/game/032x032_s_frag.png"
    ,   rotation0       = \
        [ [ 0, 0, 0 ]
        , [ 0, 1, 1 ]
        , [ 1, 1, 0 ] ]
    )
,   'T' : Figure
    (   texture         = "res/game/096x096_t.png"
    ,   frag_texture    = "res/game/032x032_t_frag.png"
    ,   rotation0       = \
        [ [ 0, 0, 0 ]
        , [ 0, 1, 0 ]
        , [ 1, 1, 1 ] ]
    )
,   'Z' : Figure
    (   texture         = "res/game/096x096_z.png"
    ,   frag_texture    = "res/game/032x032_z_frag.png"
    ,   rotation0       = \
        [ [ 0, 0, 0 ]
        , [ 1, 1, 0 ]
        , [ 0, 1, 1 ] ]
    )
,   'I' : Figure
    (   texture         = "res/game/128x128_i.png"
    ,   frag_texture    = "res/game/032x032_i_frag.png"
    ,   rotation0       = \
        [ [ 0, 0, 0, 0 ]
        , [ 0, 0, 0, 0 ]
        , [ 1, 1, 1, 1 ]
        , [ 0, 0, 0, 0 ] ]
    )
}


# PREPROCESS FIGURES

for key in figures.keys () :

    figure = figures [ key ]

    def row_empty ( y ) :
        for cell in figure.rotation0 [ y ] :
            if cell :
                return False
        return True


    def rotation ( rot0, n ) :
        n = n % 4
        size = len ( rot0 ) - 1

        def transform ( x, y ) :
            if   n == 0 : return rot0 [        y ] [        x ]
            elif n == 1 : return rot0 [ size - x ] [        y ]
            elif n == 2 : return rot0 [ size - y ] [ size - x ]
            elif n == 3 : return rot0 [        x ] [ size - y ]

        return [ [ transform ( x, y ) for x in range ( size + 1 ) ] for y in range ( size + 1 ) ]

    figure.rotations = [ rotation ( figure.rotation0, n ) for n in range ( 4 ) ]
    figure.type      = key

    y0 = 0
    while row_empty ( y0 ) :
        y0 += 1
    y1 = y0
    while y1 < figure.cells and not row_empty ( y1 ) :
        y1 += 1
    figure.center_y = ( y0 - 0.5 * ( figure.cells - y1 + y0 ) ) / float ( figure.cells )

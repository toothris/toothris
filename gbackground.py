# -*- coding: cp1251 -*-

# BASE
from bapi import *

# GAME
import glayers

# CONSTS

BACKGROUND_TEXTURE      = "res/ui_menu/256x256_back.png"
BACKGROUND_SIZE_X       = 4 * screen_width
BACKGROUND_SIZE_Y       = 4 * screen_width
BACKGROUND_SLIDE_TIME   = 10

SCRATCH_SIZE            = screen_height * 0.05
SCRATCHES_MAX_COUNT     = 10
SCRATCH_TEXTURES        = \
[ "res/ui_menu/064x064_lines1.png"
, "res/ui_menu/064x064_lines2.png"
, "res/ui_menu/064x064_lines3.png"
, "res/ui_menu/064x064_lines4.png"
]
SCRATCH_TRANSPARENCY    = 0.3
SCRATCH_APPEAR_TIME     = 0.5
SCRATCH_LIFE_TIME       = 3
SCRATCH_DISAPPEAR_TIME  = 1
SCRATCH_SCALE_MIN       = 0.6
SCRATCH_SCALE_MAX       = 1

# ALIASES

background_layer        = layer ( glayers.BACKGROUND           )
scratch_layer           = layer ( glayers.BACKGROUND_SCRATCH   )


def prefetch () :
    background_layer.prefetch_sprites ( BACKGROUND_TEXTURE, 1 )
    for texture in SCRATCH_TEXTURES :
        scratch_layer.prefetch_sprites ( texture, SCRATCHES_MAX_COUNT )


@start_async
def async_show () :
    back_sprite = background_layer.new_sprite ( BACKGROUND_TEXTURE )
    back_sprite.shape = [ -BACKGROUND_SIZE_X, BACKGROUND_SIZE_Y, BACKGROUND_SIZE_X, -BACKGROUND_SIZE_Y ]


    def random_pos () :
        x_bound = max ( 0.0, 0.5 * ( BACKGROUND_SIZE_X - screen_width  ) )
        y_bound = max ( 0.0, 0.5 * ( BACKGROUND_SIZE_Y - screen_height ) )
        x = rand ( - x_bound, x_bound )
        y = rand ( - y_bound, y_bound )
        return ( x, y )


    nodes = [ random_pos () for i in range ( 4 ) ]

    tscratches = set ()


    @start_async
    def async_put_scratch () :
        texture = rand ( SCRATCH_TEXTURES )
        if scratch_layer.available_sprites ( texture ) == 0 :
            for t in SCRATCH_TEXTURES :
                if scratch_layer.available_sprites ( t ) > 0 :
                    texture = t
                    break
        if scratch_layer.available_sprites ( texture ) == 0 :
            return

        tscratches.add ( current_task () )
        scratch_sprite = scratch_layer.new_sprite ( texture )
        scratch_sprite.shape = [ -SCRATCH_SIZE, SCRATCH_SIZE, SCRATCH_SIZE, -SCRATCH_SIZE ]
        try :
            x = mouse_pos () [ 0 ] - back_sprite.x
            y = mouse_pos () [ 1 ] - back_sprite.y

            scratch_sprite.x     = lambda : x + back_sprite.x
            scratch_sprite.y     = lambda : y + back_sprite.y
            scratch_sprite.scale = rand ( SCRATCH_SCALE_MIN, SCRATCH_SCALE_MAX )

            scratch_sprite.alpha = lerp ( 0, SCRATCH_TRANSPARENCY, dt = SCRATCH_APPEAR_TIME )
            wait ( SCRATCH_APPEAR_TIME )
            wait ( SCRATCH_LIFE_TIME   )
            scratch_sprite.alpha = lerp ( SCRATCH_TRANSPARENCY, 0, dt = SCRATCH_DISAPPEAR_TIME )
            wait ( SCRATCH_DISAPPEAR_TIME )

        finally :
            scratch_sprite.kill ()
            tscratches.remove ( current_task () )


    @start_async
    def async_catch_clicks () :
        while work_async () :
            wait ( scratch_layer.key_click.push )
            scratch_layer.handled_key_click.push ()
            async_put_scratch ()


    tclick = async_catch_clicks ()

    try :
        while work_async () :
            back_sprite.xy = bezier3 ( nodes [ 0 ], nodes [ 1 ], nodes [ 2 ], nodes [ 3 ], dt = BACKGROUND_SLIDE_TIME )
            wait ( BACKGROUND_SLIDE_TIME )

            # MAKE CONTINUOUS BEZIER CURVE SMOOTH
            second = ( 2.0 * nodes [ -1 ] [ 0 ] - nodes [ -2 ] [ 0 ]
                     , 2.0 * nodes [ -1 ] [ 1 ] - nodes [ -2 ] [ 1 ] )

            nodes = nodes [ -1 : ] + [ second ] + [ random_pos () for i in range ( 2 ) ]

    finally :
        stop ( tclick )
        for tscratch in tscratches.copy () :
            stop ( tscratch )
        back_sprite.kill ()


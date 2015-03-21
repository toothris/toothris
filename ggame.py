# -*- coding: utf-8 -*-

# BASE
from bapi import *

# GAME
from gfigures import *
import gactions
import gbonuses
import gkey
import glayers

#
# CONSTS
#

#
# STAKAN
#

STAKAN_TEXTURE                      = "res/game/256x512_stakan.png"
STAKAN_BORDER_SIZE_Y                = 0.1 * screen_height
STAKAN_BORDER_SIZE_X                = 0.1 * screen_height
STAKAN_HALF_SIZE_Y                  = 1   * screen_height
STAKAN_HALF_SIZE_X                  = 0.5 * ( 2 * STAKAN_BORDER_SIZE_X + 0.5 * ( 2 * STAKAN_HALF_SIZE_Y - STAKAN_BORDER_SIZE_Y ) )
STAKAN_X                            = -screen_width + STAKAN_HALF_SIZE_X
STAKAN_Y                            = 0
STAKAN_APPEAR_TIME                  = 0.7
STAKAN_APPEAR_X_SHIFT               = [ -1, 0.2, 0.1, 0 ]
STAKAN_DISAPPEAR_TIME               = 0.7
STAKAN_DISAPPEAR_X_SHIFT            = [ 0, 0.1, 0.2, -1 ]
STAKAN_CLICK_TIME                   = 0.5
STAKAN_CLICK_SCALE                  = [ 0.9, 1.1, 1.05, 1 ]
STAKAN_HIT_SIDE_TIME                = 0.3
STAKAN_HIT_SIDE_X_SHIFT             = [ 0, 0.05, -0.025, 0 ]
STAKAN_HIT_DOWN_TIME                = 0.3
STAKAN_HIT_DOWN_Y_SHIFT             = [ 0, 0.05, -0.025, 0 ]
STAKAN_CELLS_X                      = 10
STAKAN_CELLS_Y                      = 20

#
# KEYS
#

KEY_LEFT_TEXTURE                    = "res/game/064x064_left.png"
KEY_LEFT_X                          =  0.3 * screen_width
KEY_LEFT_Y                          = -0.6 * screen_height
KEY_LEFT_DELAY                      =  0

KEY_RIGHT_TEXTURE                   = "res/game/064x064_right.png"
KEY_RIGHT_X                         =  0.5 * screen_width
KEY_RIGHT_Y                         = -0.6 * screen_height
KEY_RIGHT_DELAY                     =  0.2

KEY_DOWN_TEXTURE                    = "res/game/064x064_down.png"
KEY_DOWN_X                          =  0.4 * screen_width
KEY_DOWN_Y                          = -0.8 * screen_height
KEY_DOWN_DELAY                      = 0.3

KEY_ROTATE_TEXTURE                  = "res/game/064x064_rotate.png"
KEY_ROTATE_X                        =  0.4 * screen_width
KEY_ROTATE_Y                        = -0.4 * screen_height
KEY_ROTATE_DELAY                    =  0.1

KEY_PAUSE_TEXTURE                   = "res/game/064x064_pause.png"
KEY_PAUSE_X                         =  0.8 * screen_width
KEY_PAUSE_Y                         = -0.8 * screen_height
KEY_PAUSE_DELAY                     =  0.4

#
# ACTIONS & BONUSES
#

ACTIONS_X                           = 0
ACTIONS_Y                           = 0.8  * screen_height
ACTIONS_STEP_X                      = 0.16 * screen_height
ACTIONS_STEP_Y                      = 0.16 * screen_height

BONUS_STEP_X                        = 0.3  * screen_height

#
# BONUS ACID RAIN
#

BONUS_ACID_RAIN_MAX_DROPS           = STAKAN_CELLS_X
BONUS_ACID_RAIN_DROP_TEXTURE        = "res/game/032x032_acid_drop.png"
BONUS_ACID_RAIN_DROP_HALF_SIZE      = 0.05 * screen_height
BONUS_ACID_RAIN_DROP_Y              = [ 0, 0.1, 0.2, 1 ]
BONUS_ACID_RAIN_DROP_ALPHA          = [ 1, 1.0, 0.9, 0 ]
BONUS_ACID_RAIN_DROP_TIME           = 1
BONUS_ACID_RAIN_DROP_DELAY          = 0.1

BONUS_ACID_RAIN_MAX_SPLATS          = STAKAN_CELLS_X * 2
BONUS_ACID_RAIN_SPLAT_TEXTURES      = \
[   "res/ui_menu/064x064_splat1.png"
,   "res/ui_menu/064x064_splat2.png"
,   "res/ui_menu/064x064_splat3.png"
,   "res/ui_menu/064x064_splat4.png"
]
BONUS_ACID_RAIN_SPLAT_HALF_SIZE     = 0.05 * screen_height
BONUS_ACID_RAIN_SPLAT_SCALE         = [ 0, 0.2, 1.5, 2 ]
BONUS_ACID_RAIN_SPLAT_TIME          = 1
BONUS_ACID_RAIN_SPLATS_SAME_TIME    = 2

#
# BONUS HAIL
#

BONUS_HAIL_FALL_Y                   = [ 0, 0.1, 0.9, 1 ]
BONUS_HAIL_FALL_TIME                = 1
BONUS_HAIL_FALL_DELAY               = 0.1

#
# BONUS EARTHQUAKE
#

BONUS_EARTHQUAKE_DESCEND_Y          = [ 0, 0.1, 0.5, 1.0 ]
BONUS_EARTHQUAKE_DESCEND_TIME       = 0.5
BONUS_EARTHQUAKE_DESCEND_DELAY      = 0.05
BONUS_EARTHQUAKE_STAKAN_SHAKE_X     = screen_height * 0.03
BONUS_EARTHQUAKE_STAKAN_SHAKE_TIME  = 0.15
BONUS_EARTHQUAKE_STAKAN_SHAKE_DELAY = 1

#
# BONUS KING OF HILL
#

BONUS_KING_OF_HILL_SLIDE_X          = [ 0, -0.1, 0.5, 5 ]
BONUS_KING_OF_HILL_SLIDE_SCALE      = [ 1,  0.9, 2.0, 0 ]
BONUS_KING_OF_HILL_SLIDE_TIME       = 2

#
# BONUS BUILDER
#

BONUS_BUILDER_BRICK_Y               = [ 0, 0.1, 0.9, 1 ]
BONUS_BUILDER_BRICK_SCALE           = [ 0, 3.0, 1.5, 1 ]
BONUS_BUILDER_BRICK_ROTATE          = [ 0, 0.1, 0.9, 1 ]
BONUS_BUILDER_BRICK_ALPHA           = [ 0, 1.0, 1.0, 1 ]
BONUS_BUILDER_BRICK_TIME            = 1
BONUS_BUILDER_BRICK_DELAY           = 0.3

#
# BONUS SUPER HIT
#

BONUS_SUPER_HIT_FRAG_TIME           = 0.5
BONUS_SUPER_HIT_DESCEND_TIME        = 0.4
BONUS_SUPER_HIT_STAKAN_SHAKE_TIME   = 0.5
BONUS_SUPER_HIT_STAKAN_SHAKE_X      = [ 0, 0.1, -0.05, 0 ]
BONUS_SUPER_HIT_MOVE_SIDE_TIME      = 0.3

#
# BONUS_SUPER_DROP
#

BONUS_SUPER_DROP_FRAG_TIME          = 0.5
BONUS_SUPER_DROP_STAKAN_SHAKE_TIME  = 0.5
BONUS_SUPER_DROP_STAKAN_SHAKE_Y     = [ 0, 0.1, -0.05, 0 ]
BONUS_SUPER_DROP_SOULFLY_FRAGS      = 10
BONUS_SUPER_DROP_TIME               = 0.4

#
# FIGURES
#

FIGURES_MAX_COUNT                   = 50
FIGURES_HIGHLIGHTS_MAX_COUNT        = 100
FIGURE_APPEAR_TIME                  = 0.3
FIGURE_MOVE_SIDE_ROTATE             = [ 0, -2, -7, -20 ]
FIGURE_MOVE_SIDE_X                  = [ 0, 0.1, 0.2, 1 ]
FIGURE_MOVE_SIDE_TIME               = 0.5
FIGURE_MOVE_SIDE_EASE_OUT_TIME      = 0.3
FIGURE_MOVE_DOWN_TIME               = 10
FIGURE_MOVE_DOWN_EASE_OUT_TIME      = 0.6
FIGURE_DROP_Y                       = [ 0, 0.1, 0.2, 1 ]
FIGURE_DROP_TIME                    = 0.6
FIGURE_ROTATE_START_PERIODS         = [ 0, 0.1, 0.2, 1 ]
FIGURE_ROTATE_START_TIME            = 0.3
FIGURE_ROTATE_STOP_PERIODS          = [ 1, 0.2, 0.1, 0 ]
FIGURE_ROTATE_STOP_TIME             = 0.3
FIGURE_CELLS_TO_SIDE_HIT            = 3
FIGURE_CELLS_TO_DOWN_HIT            = 6
FIGURE_SIDE_HIT_ROTATE_K            = [ 1, -2, 1, 0 ]
FIGURE_FREEZE_RGBA                  = [ 0.7, 0.7, 0.9, 0.9 ]
FIGURE_FREEZE_TIME                  = 1
FIGURE_UNFREEZE_TIME                = 0.3
FIGURE_SOULFLY_RADIUS               = [ 0,-0.5, 1.0, 2.0 ]
FIGURE_SOULFLY_ROTATE               = [ 0, 0.1, 0.2, 0.5 ]
FIGURE_SOULFLY_SCALE                = [ 1, 3.0, 2.0, 0.0 ]
FIGURE_SOULFLY_TIME                 = 1.5
FIGURE_SOULFLY_DELAY                = 0.05
FIGURE_DESCEND_TIME                 = 0.7
FIGURE_DESCEND_DELAY                = 0.05
FIGURE_TRAIL_ALPHA                  = 0.3
FIGURE_TRAIL_TIME                   = 0.5
FIGURE_TRAIL_DELAY                  = 0

FRAGS_MAX_COUNT                     = 200
FRAGS_HIGHLIGHTS_MAX_COUNT          = 100
FRAG_APPEAR_TIME                    = 0.5
FRAG_APPEAR_SCALE                   = [ 0, 0.5, 2, 1 ]
FRAG_APPEAR_DELAY                   = 0.05

FIGURE_SELECTION_THRESHOLD          = 3

#
# DEPENDEND CONSTS
#

STAKAN_CELL_SIZE                    = 2 * ( STAKAN_HALF_SIZE_X - STAKAN_BORDER_SIZE_X ) / STAKAN_CELLS_X

STAKAN_LEFT                         = STAKAN_X - STAKAN_HALF_SIZE_X + STAKAN_BORDER_SIZE_X
STAKAN_RIGHT                        = STAKAN_X + STAKAN_HALF_SIZE_X - STAKAN_BORDER_SIZE_X
STAKAN_BOTTOM                       = STAKAN_Y - STAKAN_HALF_SIZE_Y + STAKAN_BORDER_SIZE_Y
STAKAN_TOP                          = STAKAN_BOTTOM + STAKAN_CELLS_Y * STAKAN_CELL_SIZE


# ALIASES

stakan_layer                        = layer ( glayers.GAME_STAKAN     )
figures_layer                       = layer ( glayers.GAME_FIGURES    )
frags_layer                         = layer ( glayers.GAME_FRAGS      )
highlights_layer                    = layer ( glayers.GAME_HIGHLIGHTS )

# GLOBALS

figure_tag                          = 0
stakan                              = None

# PREFETCH

def prefetch () :
    stakan_layer.prefetch_sprites ( STAKAN_TEXTURE, 1 )

    gkey.prefetch_keys ( KEY_LEFT_TEXTURE   , 1 )
    gkey.prefetch_keys ( KEY_RIGHT_TEXTURE  , 1 )
    gkey.prefetch_keys ( KEY_DOWN_TEXTURE   , 1 )
    gkey.prefetch_keys ( KEY_ROTATE_TEXTURE , 1 )
    gkey.prefetch_keys ( KEY_PAUSE_TEXTURE  , 1 )

    for figure in figures.values () :
        figures_layer.prefetch_sprites    ( figure.texture      , FIGURES_MAX_COUNT            )
        frags_layer.prefetch_sprites      ( figure.frag_texture , FRAGS_MAX_COUNT              )
        highlights_layer.prefetch_sprites ( figure.texture      , FIGURES_HIGHLIGHTS_MAX_COUNT )
        highlights_layer.prefetch_sprites ( figure.frag_texture , FRAGS_HIGHLIGHTS_MAX_COUNT   )

    highlights_layer.prefetch_sprites ( BONUS_ACID_RAIN_DROP_TEXTURE, BONUS_ACID_RAIN_MAX_DROPS )
    for texture in BONUS_ACID_RAIN_SPLAT_TEXTURES :
        highlights_layer.prefetch_sprites ( texture, BONUS_ACID_RAIN_MAX_SPLATS )

# GAME

def show () :

    class Keys :
        def __init__ ( self ) :
            self.left                   = False
            self.right                  = False
            self.rotate                 = False
            self.down                   = False

    @start_async
    def async_work_game () :

        class FigureInStakan :
            def __init__ ( self, figure, is_frag, cell_x, cell_y ) :
                self.cell_x             = cell_x
                self.cell_y             = cell_y
                self.current_rotation   = 0
                self.is_frag            = is_frag
                self.figure             = figure
                self.rotating           = False
                self.fragmentating      = False
                self.tag                = 0

                if is_frag :
                    self.is_frozen          = True
                    self.cell_half_size     = 0.5 * STAKAN_CELL_SIZE
                    self.sprite             = frags_layer.new_sprite ( self.figure.frag_texture )
                    self.cells              = 1
                else :
                    self.is_frozen          = False
                    self.cell_half_size     = 0.5 * STAKAN_CELL_SIZE * self.figure.cells
                    self.sprite             = figures_layer.new_sprite ( self.figure.texture )
                    self.cells              = figure.cells

                self.sprite.x, self.sprite.y = self.cell_to_sprite ()
                self.sprite.shape = [ -self.cell_half_size, self.cell_half_size, self.cell_half_size, -self.cell_half_size ]

                if self.is_frozen :
                    freeze ( self )


            def __del__ ( self ) :
                self.sprite.kill ()


            def colshape ( self, drot = 0 ) :
                if self.is_frag :
                    return [ [ 1 ] ]
                else :
                    return self.figure.rotations [ ( self.current_rotation + drot ) % len ( self.figure.rotations ) ]


            def colshape_to_rot ( self, drot = 0 ) :
                return - 90 * ( self.current_rotation + drot )


            def cell_to_sprite ( self ) :
                x, y = stakan_to_world ( self.cell_x, self.cell_y )
                x += self.cell_half_size
                y -= self.cell_half_size
                return x, y


            def sprite_to_cell ( self ) :
                x = self.sprite.x - self.cell_half_size
                y = self.sprite.y + self.cell_half_size
                return world_to_stakan ( x, y )


            def can_fit ( self, dx = 0, dy = 0, drot = 0 ) :
                return can_fit ( self.colshape ( drot ), self.cell_x + dx, self.cell_y + dy )


            def in_rows ( self, yfrom, yto ) :
                for y in range ( self.cells ) :
                    for x in range ( self.cells ) :
                        final_y = y + self.cell_y
                        if self.colshape () [ y ] [ x ] and ( final_y < yfrom or final_y > yto ) :
                            return False
                return True


            def intersecting_rows ( self, yfrom, yto ) :
                is_inside  = False
                is_outside = False
                for y in range ( self.cells ) :
                    for x in range ( self.cells ) :
                        final_y = y + self.cell_y
                        if self.colshape () [ y ] [ x ] :
                            if final_y < yfrom or final_y > yto :
                                is_outside = True
                            else :
                                is_inside  = True
                            if is_outside and is_inside :
                                return True
                return False


        def place_to_stakan ( figure ) :
            for y in range ( figure.cells ) :
                for x in range ( figure.cells ) :
                    if figure.colshape () [ y ] [ x ] :
                        stakan_cell_set ( figure.cell_x + x, figure.cell_y + y, figure )


        def remove_from_stakan ( figure ) :
            for y in range ( figure.cells ) :
                for x in range ( figure.cells ) :
                    if figure.colshape () [ y ] [ x ] :
                        stakan_cell_set ( figure.cell_x + x, figure.cell_y + y, None )

        def freeze ( figure, bind_x = True, bind_y = True, fade_alpha = True ) :
            figure.is_frozen = True
            dx = figure.sprite.x - STAKAN_X
            dy = figure.sprite.y - STAKAN_Y

            if bind_x :
                figure.sprite.x = lambda : dx + stakan_sprite.x
            if bind_y :
                figure.sprite.y = lambda : dy + stakan_sprite.y

            figure.sprite.rot = figure.colshape_to_rot ()

            if fade_alpha :
                figure.sprite.rgba = ease ( figure.sprite.rgba, tuple ( FIGURE_FREEZE_RGBA ), dt = FIGURE_FREEZE_TIME )
            else :
                figure.sprite.red   = ease ( end = FIGURE_FREEZE_RGBA [ 0 ], dt = FIGURE_FREEZE_TIME )
                figure.sprite.green = ease ( end = FIGURE_FREEZE_RGBA [ 1 ], dt = FIGURE_FREEZE_TIME )
                figure.sprite.blue  = ease ( end = FIGURE_FREEZE_RGBA [ 2 ], dt = FIGURE_FREEZE_TIME )

            place_to_stakan ( figure )


        def unfreeze ( figure, fade_alpha = True ) :
            figure.is_frozen = False

            if fade_alpha :
                figure.sprite.rgba = ease ( figure.sprite.rgba, ( 1, 1, 1, 1 ), dt = FIGURE_UNFREEZE_TIME )
            else :
                figure.sprite.red   = ease ( end = 1, dt = FIGURE_UNFREEZE_TIME )
                figure.sprite.green = ease ( end = 1, dt = FIGURE_UNFREEZE_TIME )
                figure.sprite.blue  = ease ( end = 1, dt = FIGURE_UNFREEZE_TIME )

            remove_from_stakan ( figure )


        def handle_placement ( figure ) :
            action = gactions.ACTION_GROUND
            for x in range ( figure.cells ) :
                for y in range ( figure.cells ) :
                    if figure.colshape () [ figure.cells - y - 1 ] [ x ] :
                        final_y = figure.cell_y + figure.cells - y
                        final_x = figure.cell_x + x
                        if final_y < STAKAN_CELLS_Y and not stakan_cell_get ( final_x, final_y ) :
                            action = gactions.ACTION_FLOAT
                            break
            gactions.handle_action ( actions, action, figure.figure, figure.sprite.x, figure.sprite.y )


        def fragmentate ( figure, appear_time = FRAG_APPEAR_TIME, appear_delay = FRAG_APPEAR_DELAY ) :
            assert figure.is_frozen
            figure.sprite.alpha = ease_in ( end = 0, dt = appear_time )
            figure.fragmentating = True

            gactions.handle_action ( actions, gactions.ACTION_FRAG, figure.figure, figure.sprite.x, figure.sprite.y )

            frags = []
            for y in range ( figure.cells ) :
                for x in range ( figure.cells ) :
                    if figure.colshape () [ y ] [ x ] :
                        final_x = figure.cell_x + x
                        final_y = figure.cell_y + y
                        frag = FigureInStakan ( figure.figure, True, final_x, final_y )
                        frags.append ( frag )
                        stakan_cell_set ( final_x, final_y, frag )
                        frag.sprite.alpha = ease_out ( 0, frag.sprite.alpha, dt = appear_time )
                        s = FRAG_APPEAR_SCALE
                        frag.sprite.scale = bezier3 ( s [ 0 ], s [ 1 ], s [ 2 ], s [ 3 ], dt = appear_time )
                        wait ( appear_delay )

            return frags


        @start_async
        def async_soulfly ( figure, angle ) :
            assert figure.is_frozen
            soul_sprite = None
            if figure.is_frag :
                soul_sprite = highlights_layer.new_sprite ( figure.figure.frag_texture )
            else :
                soul_sprite = highlights_layer.new_sprite ( figure.figure.texture )

            figure.sprite.alpha   = 0

            soul_sprite.shape   = figure.sprite.shape
            soul_sprite.red     = figure.sprite.red
            soul_sprite.green   = figure.sprite.green
            soul_sprite.blue    = figure.sprite.blue
            soul_sprite.alpha   = ease_in ( end = 0, dt = FIGURE_SOULFLY_TIME )

            x = [ figure.sprite.x + cos ( angle ) * screen_height * r for r in FIGURE_SOULFLY_RADIUS ]
            y = [ figure.sprite.y + sin ( angle ) * screen_height * r for r in FIGURE_SOULFLY_RADIUS ]
            r = [ figure.sprite.rot - 360 * r for r in FIGURE_SOULFLY_ROTATE ]
            s = FIGURE_SOULFLY_SCALE

            soul_sprite.x     = bezier3 ( x [ 0 ], x [ 1 ], x [ 2 ], x [ 3 ], dt = FIGURE_SOULFLY_TIME )
            soul_sprite.y     = bezier3 ( y [ 0 ], y [ 1 ], y [ 2 ], y [ 3 ], dt = FIGURE_SOULFLY_TIME )
            soul_sprite.rot   = bezier3 ( r [ 0 ], r [ 1 ], r [ 2 ], r [ 3 ], dt = FIGURE_SOULFLY_TIME )
            soul_sprite.scale = bezier3 ( s [ 0 ], s [ 1 ], s [ 2 ], s [ 3 ], dt = FIGURE_SOULFLY_TIME )

            wait ( FIGURE_SOULFLY_DELAY )

            @start_async
            def async_suicide () :
                wait ( FIGURE_SOULFLY_TIME )
                soul_sprite.kill ()

            async_suicide ()


        def soulfly ( figures ) :

            figures_count = len ( figures )
            if not figures_count :
                return

            angle_step = 90.0 / float ( figures_count )
            angle = 90.0
            for figure in figures :
                async_soulfly ( figure, angle )
                angle -= angle_step
                if not figure.is_frag :
                    gactions.handle_action ( actions, gactions.ACTION_SWALLOW, figure.figure, figure.sprite.x, figure.sprite.y )
                work_async ()


        def descend ( yfrom, yto ) :

            @start_async
            def async_descend ( figure, cells_y ) :
                assert figure.is_frozen
                unfreeze ( figure, fade_alpha = False )
                figure.cell_y += cells_y
                figure.sprite.y = ease ( end = figure.sprite.y - STAKAN_CELL_SIZE * cells_y, dt = FIGURE_DESCEND_TIME )
                wait ( FIGURE_DESCEND_TIME )
                freeze ( figure, bind_x = False, fade_alpha = False )

            tdescendants = []
            try :
                stakan_clear_rows ( yfrom, yto )

                for figure in reversed ( figures_in_rows ( 0, yfrom - 1 ) ) :
                    tdescendants.append ( async_descend ( figure, yto - yfrom + 1 ) )
                    wait ( FIGURE_DESCEND_DELAY )
                for tdesc in tdescendants :
                    wait ( tdesc )
            finally :
                for tdesc in tdescendants :
                    stop ( tdesc )


        @start_async
        def async_trail ( figure ) :

            @start_async
            def async_single_trail ( figure ) :
                trail_sprite        = highlights_layer.new_sprite ( figure.figure.texture )

                trail_sprite.shape  = figure.sprite.shape
                trail_sprite.x      = figure.sprite.x
                trail_sprite.y      = figure.sprite.y
                trail_sprite.rot    = figure.sprite.rot

                trail_sprite.alpha  = ease ( FIGURE_TRAIL_ALPHA, 0, dt = FIGURE_TRAIL_TIME )
                wait ( FIGURE_TRAIL_TIME )
                trail_sprite.kill ()


            assert not figure.is_frozen
            while work_async () :
                async_single_trail ( figure )
                wait ( FIGURE_TRAIL_DELAY )


        def can_fit ( colshape, cell_x, cell_y ) :
            for y in range ( len ( colshape ) ) :
                for x in range ( len ( colshape ) ) :
                    if colshape [ y ] [ x ] :
                        final_x = cell_x + x
                        final_y = cell_y + y

                        if final_x < 0 or final_x >= STAKAN_CELLS_X \
                        or final_y < 0 or final_y >= STAKAN_CELLS_Y \
                        or stakan_cell_get ( final_x, final_y ) :
                            return False
            return True


        def figures_in_rows ( yfrom, yto ) :
            global figure_tag
            figure_tag += 1
            figures = []
            for row in stakan_rows ( yfrom, yto ) :
                for figure in row :
                    if figure and figure.tag != figure_tag and figure.in_rows ( yfrom, yto ) :
                        figure.tag = figure_tag
                        figures += [ figure ]
            return figures


        def figures_intersecting_rows ( yfrom, yto ) :
            global figure_tag
            figure_tag += 1
            figures = []
            for row in stakan_rows ( yfrom, yto ) :
                for figure in row :
                    if figure and figure.tag != figure_tag and figure.intersecting_rows ( yfrom, yto ) :
                        figure.tag = figure_tag
                        figures += [ figure ]
            return figures


        def is_rows_full ( yfrom, yto ) :
            for row in stakan_rows ( yfrom, yto ) :
                for figure in row :
                    if figure == None :
                        return False
            return True


        def is_rows_empty ( yfrom, yto ) :
            for row in stakan_rows ( yfrom, yto ) :
                for figure in row :
                    if figure != None :
                        return False
            return True


        def stakan_to_world ( cell_x, cell_y ) :
            return  STAKAN_LEFT + cell_x * STAKAN_CELL_SIZE \
                 ,  STAKAN_TOP  - cell_y * STAKAN_CELL_SIZE


        def world_to_stakan ( x, y ) :
            cell_x = float ( x - STAKAN_LEFT ) / float ( STAKAN_CELL_SIZE ) + TOLERANCE
            cell_y = float ( STAKAN_TOP - y  ) / float ( STAKAN_CELL_SIZE ) + TOLERANCE
            return floor ( cell_x ), floor ( cell_y )


        @start_async
        def async_game_play () :

            @start_async
            def async_move_side () :

                def move_side ( xdir, pressed ) :

                    #
                    # BONUS SUPER HIT
                    #

                    @start_async
                    def async_super_hit () :

                        def descend_fast ( yfrom, yto ) :

                            figures = figures_in_rows ( 0, yfrom - 1 )

                            stakan_clear_rows ( yfrom, yto )

                            for figure in figures :
                                cells_y = yto - yfrom + 1
                                assert figure.is_frozen
                                unfreeze ( figure, fade_alpha = False )
                                figure.cell_y += cells_y
                                figure.sprite.y = ease ( end = figure.sprite.y - STAKAN_CELL_SIZE * cells_y, dt = BONUS_SUPER_HIT_DESCEND_TIME )

                            wait ( BONUS_SUPER_HIT_DESCEND_TIME )

                            for figure in figures :
                                freeze ( figure, bind_x = False, fade_alpha = False )


                        yfrom = STAKAN_CELLS_Y - 1
                        yto   = STAKAN_CELLS_Y - 1

                        # FRAGMENTATE INTERSECTING FIGURES
                        for figure in figures_intersecting_rows ( yfrom, yto ) :
                            fragmentate ( figure, appear_time = BONUS_SUPER_HIT_FRAG_TIME, appear_delay = 0 )
                            work_async ()

                        soulfly ( figures_in_rows ( yfrom, yto ) )
                        descend_fast ( yfrom, yto )

                    #
                    # SIDE FIGURE MOVEMENT
                    #

                    assert active_figure
                    assert active_figure.can_fit ()

                    # RETURN IF THERE'S NOTHING TO MOVE TO
                    if not active_figure.can_fit ( dx = xdir ) :
                        return

                    #
                    # MOVE USING BEZIER CURVE
                    #

                    move_side_time = BONUS_SUPER_HIT_MOVE_SIDE_TIME if bonus_super_hit.is_active else FIGURE_MOVE_SIDE_TIME

                    x = [ active_figure.sprite.x + xdir * STAKAN_CELLS_X * STAKAN_CELL_SIZE * x for x in FIGURE_MOVE_SIDE_X ]
                    active_figure.sprite.x = bezier3 ( x [ 0 ], x [ 1 ], x [ 2 ], x [ 3 ], dt = move_side_time )

                    # ADD VISUAL ROTATION IF NOT ROTATING ALREADY
                    if not active_figure.rotating :
                        r = [ active_figure.sprite.rot + xdir * r for r in FIGURE_MOVE_SIDE_ROTATE ]
                        active_figure.sprite.rot = bezier3 ( r [ 0 ], r [ 1 ], r [ 2 ], r [ 3 ], dt = move_side_time )

                    #
                    # TRACK SIDE MOVEMENT
                    #

                    ttrail = None

                    try :
                        hit_side = False
                        cells_passed = 0 if xdir < 0 else 1
                        while pressed () :
                            cell_x, cell_y = active_figure.sprite_to_cell ()

                            prev_cell_x = active_figure.cell_x

                            if xdir < 0 :
                                active_figure.cell_x = cell_x
                            else :
                                active_figure.cell_x = cell_x + 1

                            # CALC CELLS PASSED
                            if prev_cell_x != active_figure.cell_x :
                                cells_passed += abs ( active_figure.cell_x - prev_cell_x )

                            # DRAW TRAIL IF SUPER HIT BONUS IS ACTIVE
                            if  cells_passed >= FIGURE_CELLS_TO_SIDE_HIT    \
                            and bonus_super_hit.is_active                   \
                            and not ttrail :
                                ttrail = async_trail ( active_figure )

                            #
                            # STOP MOVEMENT IF WE'RE HIT THE WALL
                            #

                            hit_side = not active_figure.can_fit ( dx = xdir )
                            if hit_side :
                                break

                            work_async ()

                            hit_side = not active_figure.can_fit ( dx = xdir )
                            if hit_side :
                                break


                        #
                        # WEAK HIT OR SIDE MOVEMENT KEY WAS POPPED
                        #

                        if not hit_side or cells_passed < FIGURE_CELLS_TO_SIDE_HIT :

                            stop ( ttrail )

                            x, y = active_figure.cell_to_sprite ()

                            if active_figure.can_fit ( dx = xdir ) :
                                if xdir < 0 and active_figure.sprite.x < x :
                                    active_figure.cell_x -= 1
                                if xdir > 0 and active_figure.sprite.x > x :
                                    active_figure.cell_x += 1

                            #
                            # MOVE TO FIXED X POSITION
                            #

                            x, y = active_figure.cell_to_sprite ()

                            time = FIGURE_MOVE_SIDE_EASE_OUT_TIME * abs ( active_figure.sprite.x - x ) / STAKAN_CELL_SIZE
                            active_figure.sprite.x = ease_out ( end = x, dt = time )
                            if not active_figure.rotating :
                                active_figure.sprite.rot = ease_out ( end = active_figure.colshape_to_rot (), dt = time )
                            wait ( time )

                        #
                        # STRONG WALL HIT
                        #

                        else :

                            #
                            # MOVE TO ACTUAL WALL HIT
                            #

                            while True :
                                cell_x, cell_y = active_figure.sprite_to_cell ()

                                if xdir > 0 :
                                    active_figure.cell_x = cell_x + 1
                                else :
                                    active_figure.cell_x = cell_x

                                if not active_figure.can_fit () :
                                    # PULL OUT FROM COLLISION
                                    while not active_figure.can_fit () :
                                        active_figure.cell_x -= xdir
                                        if xdir > 0 :
                                            assert active_figure.cell_x >= 0
                                        else :
                                            assert active_figure.cell_x < STAKAN_CELLS_X
                                    break

                                work_async ()

                            stop ( ttrail )

                            #
                            # MOVE TO X JUST BEFORE COLLISION
                            #

                            assert active_figure.can_fit ()
                            x, y = active_figure.cell_to_sprite ()
                            active_figure.sprite.x = x

                            # HANDLE WALL HIT ACTION
                            gactions.handle_action ( actions, gactions.ACTION_HIT, active_figure.figure, active_figure.sprite.x, active_figure.sprite.y )

                            #
                            # SUPER HIT BONUS
                            #

                            tsuper_hit = async_super_hit () if bonus_super_hit.is_active else None
                            shake_stakan_x = BONUS_SUPER_HIT_STAKAN_SHAKE_X if bonus_super_hit.is_active else STAKAN_HIT_SIDE_X_SHIFT
                            shake_time = BONUS_SUPER_HIT_STAKAN_SHAKE_TIME if bonus_super_hit.is_active else STAKAN_HIT_SIDE_TIME

                            #
                            # HORIZONTAL STAKAN SHAKING
                            #

                            assert active_figure.cells + FIGURE_CELLS_TO_SIDE_HIT <= STAKAN_CELLS_X

                            amount = float ( cells_passed - FIGURE_CELLS_TO_SIDE_HIT + 1 ) / ( STAKAN_CELLS_X - active_figure.cells - FIGURE_CELLS_TO_SIDE_HIT + 1 )
                            x = [ STAKAN_X + xdir * x * amount * screen_width for x in shake_stakan_x ]

                            stakan_sprite.x = bezier3 ( x [ 0 ], x [ 1 ], x [ 2 ], x [ 3 ], dt = shake_time )

                            #
                            # FIGURE ROTATION SHAKING
                            #

                            if not active_figure.rotating :
                                r = [ active_figure.colshape_to_rot () * ( 1 + r ) - active_figure.sprite.rot * r for r in FIGURE_SIDE_HIT_ROTATE_K ]
                                active_figure.sprite.rot = bezier3 ( r [ 0 ], r [ 1 ], r [ 2 ], r [ 3 ], dt = shake_time )

                            wait ( shake_time )
                            wait ( tsuper_hit )

                    finally :
                        stop ( ttrail )


                #
                # CATCH LEFT & RIGHT KEYS
                #

                while work_async () :

                    def left_pressed () :
                        return keys.left

                    def right_pressed () :
                        return keys.right

                    if keys.left :
                        move_side ( -1, left_pressed )
                    if keys.right :
                        move_side ( +1, right_pressed )


            @start_async
            def async_move_down () :

                def soulfly_frag ( frag ) :
                    async_soulfly ( frag, 45.0 + 45.0 * cos ( 360.0 * soulfly_frags / BONUS_SUPER_DROP_SOULFLY_FRAGS ) )


                #
                # STOP IF CAN'T FALL
                #

                assert active_figure
                assert active_figure.can_fit ()
                if not active_figure.can_fit ( dy = 1 ) :
                    stop ( tmove_side )
                    stop ( trotate )
                    freeze ( active_figure )
                    handle_placement ( active_figure )
                    return

                #
                # MOVE FIGURE DOWN WITH CONSTANT SPEED
                #

                active_figure.sprite.y = lerp ( end = active_figure.sprite.y - STAKAN_CELLS_Y * STAKAN_CELL_SIZE, dt = FIGURE_MOVE_DOWN_TIME )
                while not active_figure.is_frozen :

                    #
                    # CHECK IF WE'RE REACHED THE GROUND
                    #

                    cell_x, cell_y = active_figure.sprite_to_cell ()
                    dy = cell_y + 1 - active_figure.cell_y

                    if active_figure.can_fit ( dy = dy ) :
                        active_figure.cell_y += dy
                    else :
                        while active_figure.can_fit ( dy = 1 ) :
                            active_figure.cell_y += 1

                    if not active_figure.can_fit ( dy = 1 ) :

                        #
                        # GENTLY PUT FIGURE ON GROUND
                        #

                        x, y = active_figure.cell_to_sprite ()
                        time_y = FIGURE_MOVE_DOWN_EASE_OUT_TIME * ( active_figure.sprite.y - y ) / STAKAN_CELL_SIZE
                        active_figure.sprite.y = ease_out ( end = y, dt = time_y )
                        wait ( time_y )

                        #
                        # CHECK IF WE'RE STILL CAN NOT FALL
                        #

                        if not active_figure.can_fit ( dy = 1 ) :

                            #
                            # MOVE TO FIXED X AND ROTATION STATE
                            #

                            stop ( tmove_side )
                            stop ( trotate )
                            x, y = active_figure.cell_to_sprite ()
                            time_x = FIGURE_MOVE_SIDE_EASE_OUT_TIME * abs ( active_figure.sprite.x - x ) / STAKAN_CELL_SIZE
                            time_rot = FIGURE_MOVE_SIDE_EASE_OUT_TIME * abs ( active_figure.sprite.rot - active_figure.colshape_to_rot () ) / 90.0
                            time = max ( time_x, time_rot )
                            active_figure.sprite.x   = ease_out ( end = x, dt = time )
                            active_figure.sprite.rot = ease_out ( end = active_figure.colshape_to_rot (), dt = time )
                            wait ( time )

                            #
                            # FREEZE FIGURE IN STAKAN
                            #

                            freeze ( active_figure )
                            handle_placement ( active_figure )
                        else :

                            #
                            # CONTINUE FALLING
                            #

                            active_figure.sprite.y = lerp ( end = active_figure.sprite.y - STAKAN_CELLS_Y * STAKAN_CELL_SIZE, dt = FIGURE_MOVE_DOWN_TIME )

                    else :

                        #
                        # DROP FIGURE USING BEZIER CURVE
                        #

                        if keys.down :

                            drop_time = BONUS_SUPER_DROP_TIME if bonus_super_drop.is_active else FIGURE_DROP_TIME

                            y = [ active_figure.sprite.y - y * STAKAN_CELL_SIZE * STAKAN_CELLS_Y for y in FIGURE_DROP_Y ]
                            active_figure.sprite.y = bezier3 ( y [ 0 ], y [ 1 ], y [ 2 ], y [ 3 ], dt = drop_time )
                            cells_passed = 1
                            ttrail = None
                            soulfly_frags = 0

                            #
                            # TRACK FALLING
                            #

                            try :
                                while keys.down :
                                    cell_x, cell_y = active_figure.sprite_to_cell ()
                                    dy = cell_y + 1 - active_figure.cell_y
                                    cells_passed += dy

                                    #
                                    # BONUS SUPER DROP
                                    #

                                    if bonus_super_drop.is_active and cells_passed >= FIGURE_CELLS_TO_DOWN_HIT :

                                        # DRAW TRAIL
                                        if not working ( ttrail ) :
                                            ttrail = async_trail ( active_figure )

                                        # CLEAN THE WAY!
                                        for y in range ( dy + 1 ) :
                                            for colshape_y in range ( active_figure.cells ) :
                                                for colshape_x in range ( active_figure.cells ) :

                                                    if not active_figure.colshape () [ colshape_y ] [ colshape_x ] :
                                                        continue

                                                    final_x = colshape_x + active_figure.cell_x
                                                    final_y = colshape_y + active_figure.cell_y + y + 1

                                                    if final_x < 0 or final_x > STAKAN_CELLS_X - 1 :
                                                        continue
                                                    if final_y < 0 or final_y > STAKAN_CELLS_Y - 1 :
                                                        continue

                                                    victim = stakan_cell_get ( final_x, final_y )
                                                    if not victim :
                                                        continue

                                                    if not victim.is_frag :
                                                        fragmentate ( victim, appear_time = BONUS_SUPER_DROP_FRAG_TIME, appear_delay = 0 )
                                                        victim = stakan_cell_get ( final_x, final_y )
                                                    else :
                                                        work_async ()

                                                    assert victim.is_frag

                                                    soulfly_frag ( victim )
                                                    soulfly_frags += 1
                                                    stakan_cell_set ( final_x, final_y, None )

                                    #
                                    # MOVE FIGURE ONE CELL DOWN
                                    #

                                    if active_figure.can_fit ( dy = dy ) :
                                        active_figure.cell_y += dy
                                    else :
                                        while active_figure.can_fit ( dy = 1 ) :
                                            active_figure.cell_y += 1

                                    #
                                    # CHECK IF WE'RE REACHED THE GROUND
                                    #

                                    if not active_figure.can_fit ( dy = 1 ) :
                                        if cells_passed < FIGURE_CELLS_TO_DOWN_HIT :
                                            break

                                        #
                                        # MOVE TO FIXED X AND ROTATION STATE
                                        #

                                        stop ( tmove_side )
                                        stop ( trotate    )
                                        x, y = active_figure.cell_to_sprite ()
                                        time_x   = FIGURE_MOVE_SIDE_EASE_OUT_TIME * abs ( active_figure.sprite.x - x ) / STAKAN_CELL_SIZE
                                        time_rot = STAKAN_HIT_DOWN_TIME * abs ( active_figure.sprite.rot - active_figure.colshape_to_rot () ) / 90.0
                                        active_figure.sprite.rot = ease_out ( end = active_figure.colshape_to_rot (), dt = time_rot )
                                        active_figure.sprite.x   = ease_out ( end = x, dt = time_x )

                                        #
                                        # WAIT ACTUAL GROUND HIT
                                        #

                                        while True :
                                            cell_x, cell_y = active_figure.sprite_to_cell ()

                                            active_figure.cell_y = cell_y + 1
                                            if not active_figure.can_fit () :
                                                # PULL OUT FROM COLLISION
                                                while not active_figure.can_fit () :
                                                    active_figure.cell_y -= 1
                                                    assert active_figure.cell_y > 0
                                                break
                                            work_async ()

                                        # MOVE BY Y JUST BEFORE COLLISION
                                        assert active_figure.can_fit ()
                                        x, y = active_figure.cell_to_sprite ()
                                        active_figure.sprite.y = y

                                        # STOP TRAIL
                                        stop ( ttrail )

                                        # HANDLE DROP ACTION
                                        gactions.handle_action ( actions, gactions.ACTION_DROP, active_figure.figure, active_figure.sprite.x, active_figure.sprite.y )

                                        #
                                        # VERTICAL STAKAN SHAKING
                                        #

                                        assert active_figure.cells + FIGURE_CELLS_TO_DOWN_HIT <= STAKAN_CELLS_Y

                                        hit_time = BONUS_SUPER_DROP_STAKAN_SHAKE_TIME if bonus_super_drop.is_active else STAKAN_HIT_DOWN_TIME
                                        hit_stakan_y_shift = BONUS_SUPER_DROP_STAKAN_SHAKE_Y if bonus_super_drop.is_active else STAKAN_HIT_DOWN_Y_SHIFT

                                        amount = float ( cells_passed - FIGURE_CELLS_TO_DOWN_HIT + 1 ) / ( STAKAN_CELLS_Y - active_figure.cells - FIGURE_CELLS_TO_DOWN_HIT + 1 )
                                        y = [ STAKAN_Y - y * amount * screen_width for y in hit_stakan_y_shift ]
                                        stakan_sprite.y = bezier3 ( y [ 0 ], y [ 1 ], y [ 2 ], y [ 3 ], dt = hit_time )

                                        wait ( hit_time )

                                        #
                                        # FREEZE FIGURE IN STAKAN
                                        #

                                        freeze ( active_figure )
                                        handle_placement ( active_figure )
                                        return
                                    else :
                                        # WAIT FRAME
                                        work_async ()

                            finally :
                                stop ( ttrail )

                            #
                            # CONTINUE FALLING IF DROP KEY WAS POPPED
                            #

                            if not keys.down :
                                active_figure.sprite.y = lerp ( end = active_figure.sprite.y - STAKAN_CELLS_Y * STAKAN_CELL_SIZE, dt = FIGURE_MOVE_DOWN_TIME )
                        else :
                            # WAIT FRAME
                            work_async ()


            @start_async
            def async_rotate () :

                #
                # CATCH ROTATION KEYS
                #

                assert active_figure
                tlerp = None
                try :
                    while work_async () :
                        if keys.rotate :

                            #
                            # BEGIN ROTATING USING BEZIER CURVE
                            #

                            active_figure.rotating = True

                            r = [ active_figure.colshape_to_rot ( drot = r ) for r in FIGURE_ROTATE_START_PERIODS ]
                            active_figure.sprite.rot = bezier3 ( r [ 0 ], r [ 1 ], r [ 2 ], r [ 3 ], dt = FIGURE_ROTATE_START_TIME )

                            #
                            # CONTINUE ROTATING USING LERP
                            #

                            @start_async
                            def async_rotate_lerp () :
                                wait ( FIGURE_ROTATE_START_TIME )
                                drot = FIGURE_ROTATE_START_PERIODS [ 3 ] - FIGURE_ROTATE_START_PERIODS [ 2 ]
                                active_figure.sprite.rot = lerp ( end = active_figure.sprite.rot - 90 * drot, dt = FIGURE_ROTATE_START_TIME / 3.0, extend = 'extrapolate' )

                            tlerp = async_rotate_lerp ()

                            #
                            # TRACK ROTATIONS
                            #

                            rotations_passed = 0
                            while keys.rotate :
                                drot = floor ( ( active_figure.colshape_to_rot () - active_figure.sprite.rot ) / 90.0 ) + 1
                                if active_figure.can_fit ( drot = drot ) :

                                    active_figure.current_rotation += drot
                                    rotations_passed += drot

                                    # HANDLE FULL ROTATION ACTION
                                    while rotations_passed >= 4 :
                                        rotations_passed -= 4
                                        gactions.handle_action ( actions, gactions.ACTION_ROTATE, active_figure.figure, active_figure.sprite.x, active_figure.sprite.y )
                                    work_async ()
                                else :
                                    break

                            #
                            # FINISH ROTATION TO FIXED POSITION
                            #

                            stop ( tlerp )

                            r = [ active_figure.colshape_to_rot () * ( 1 - r ) + active_figure.sprite.rot * r for r in FIGURE_ROTATE_STOP_PERIODS ]
                            time = FIGURE_ROTATE_STOP_TIME * abs ( active_figure.colshape_to_rot () - active_figure.sprite.rot ) / 90.0
                            active_figure.sprite.rot = bezier3 ( r [ 0 ], r [ 1 ], r [ 2 ], r [ 3 ], dt = time )
                            wait ( time )

                            active_figure.rotating = False
                finally :
                    stop ( tlerp )
                    active_figure.rotating = False


            #
            # EAT ROWS
            #

            def eat_rows () :

                assert not active_figure

                #
                # EAT FULL ROWS
                #

                # DETERMINE FULL ROWS BEGIN
                yfrom = 0
                while yfrom < STAKAN_CELLS_Y :
                    if is_rows_full ( yfrom, yfrom ) :
                        # DETERMINE FULL ROWS END
                        yto = yfrom
                        while yto < STAKAN_CELLS_Y - 1 and is_rows_full ( yfrom, yto + 1 ) :
                            yto += 1

                        # FRAGMENTATE INTERSECTING FIGURES
                        for figure in figures_intersecting_rows ( yfrom, yto ) :
                            fragmentate ( figure )

                        # FLY AWAY FIGURES IN ROWS
                        soulfly ( figures_in_rows ( yfrom, yto ) )

                        # DESCEND REST OF STAKAN
                        if yfrom > 0 :
                            descend ( yfrom, yto )

                        yfrom = yto
                    yfrom += 1

                #
                # EAT EMPTY ROWS
                #

                # DETERMINE EMPTY ROWS BEGIN
                yfrom = 0
                while yfrom < STAKAN_CELLS_Y :
                    if is_rows_empty ( yfrom, yfrom ) :
                        # DETERMINE EMPTY ROWS END
                        yto = yfrom
                        while yto < STAKAN_CELLS_Y - 1 and is_rows_empty ( yfrom, yto + 1 ) :
                            yto += 1

                        # EAT EMPTY ROWS
                        if yfrom > 0 :
                            descend ( yfrom, yto )

                        yfrom = yto
                    yfrom += 1


            #
            # ACID RAIN BONUS
            #

            def do_acid_rain () :

                @start_async
                def async_rain_drop ( cell_x, cell_y ) :

                    drop_sprite = highlights_layer.new_sprite ( BONUS_ACID_RAIN_DROP_TEXTURE )

                    try :

                        half_size = BONUS_ACID_RAIN_SPLAT_HALF_SIZE
                        drop_sprite.shape = [ -half_size, half_size, half_size, -half_size ]

                        xto, yto = stakan_to_world ( cell_x, cell_y )
                        xto += 0.5 * STAKAN_CELL_SIZE

                        xfrom = xto
                        yfrom = screen_height + half_size * 2

                        y = [ yfrom * ( 1 - y ) + yto * y for y in BONUS_ACID_RAIN_DROP_Y ]
                        drop_sprite.x = xto
                        drop_sprite.y = bezier3 ( y [ 0 ], y [ 1 ], y [ 2 ], y [ 3 ], dt = BONUS_ACID_RAIN_DROP_TIME )
                        a = BONUS_ACID_RAIN_DROP_ALPHA
                        drop_sprite.alpha = bezier3 ( a [ 0 ], a [ 1 ], a [ 2 ], a [ 3 ], dt = BONUS_ACID_RAIN_DROP_TIME )
                        wait ( BONUS_ACID_RAIN_DROP_TIME )

                        @start_async
                        def async_splat ( single_splat ) :

                            @start_async
                            def async_do_splat () :
                                splat_sprites = queue ( [ highlights_layer.new_sprite ( t ) for t in BONUS_ACID_RAIN_SPLAT_TEXTURES ] )
                                for sprite in splat_sprites :
                                    half_size = BONUS_ACID_RAIN_SPLAT_HALF_SIZE
                                    sprite.x = xto
                                    sprite.y = yto
                                    sprite.shape = [ -half_size, half_size, half_size, -half_size ]
                                    s = BONUS_ACID_RAIN_SPLAT_SCALE
                                    sprite.scale = bezier3 ( s [ 0 ], s [ 1 ], s [ 2 ], s [ 3 ], dt = BONUS_ACID_RAIN_SPLAT_TIME )
                                try :
                                    splat_iterations = len ( splat_sprites ) - 1
                                    splat_time = float ( BONUS_ACID_RAIN_SPLAT_TIME ) / splat_iterations
                                    for i in range ( splat_iterations ) :
                                        splat_sprites [ 0 ].alpha = ease_out ( 1, 0, dt = splat_time )
                                        splat_sprites [ 1 ].alpha = ease_out ( 0, 1, dt = splat_time )
                                        wait ( splat_time )
                                        splat_sprites.rotate ( -1 )
                                    splat_sprites [ 0 ].alpha = lerp ( 1, 0, dt = splat_time )
                                    wait ( splat_time )
                                    splat_sprites.rotate ( -1 )

                                finally :
                                    for sprite in splat_sprites :
                                        sprite.kill ()


                            tsplats = []
                            try :
                                if single_splat :
                                    tsplats.append ( async_do_splat () )
                                else :
                                    tsplats.append ( async_do_splat () )
                                    while not stakan_cell_get ( cell_x, cell_y ).is_frag :
                                        wait ( float ( BONUS_ACID_RAIN_SPLAT_TIME ) /             float ( BONUS_ACID_RAIN_SPLATS_SAME_TIME ) )
                                        tsplats.append ( async_do_splat () )

                                for tsplat in tsplats :
                                    wait ( tsplat )

                            finally :
                                for tsplat in tsplats :
                                    stop ( tsplat )


                        tsplat = None

                        try :
                            figure = stakan_cell_get ( cell_x, cell_y )
                            if figure :
                                tsplat = async_splat ( single_splat = False )
                                if not figure.is_frag and not figure.fragmentating :
                                    fragmentate ( figure )
                                while not stakan_cell_get ( cell_x, cell_y ).is_frag :
                                    work_async ()
                                figure = stakan_cell_get ( cell_x, cell_y )
                                figure.sprite.alpha = ease ( end = 0, dt = BONUS_ACID_RAIN_SPLAT_TIME )
                                wait ( BONUS_ACID_RAIN_SPLAT_TIME )
                                stakan_cell_set ( cell_x, cell_y, None )
                            else :
                                tsplat = async_splat ( single_splat = True )
                            wait ( tsplat )

                        finally :
                            stop ( tsplat )

                    finally :
                        drop_sprite.kill ()


                assert not active_figure

                tdrops = []
                try :
                    for cell_x in range ( STAKAN_CELLS_X ) :
                        no_victim_found = True
                        for cell_y in range ( STAKAN_CELLS_Y ) :
                            if stakan_cell_get ( cell_x, cell_y ) :
                                tdrops.append ( async_rain_drop ( cell_x, cell_y ) )
                                no_victim_found = False
                                break
                        if no_victim_found :
                            async_rain_drop ( cell_x, STAKAN_CELLS_Y - 1 )
                        wait ( BONUS_ACID_RAIN_DROP_DELAY )

                    for tdrop in tdrops :
                        wait ( tdrop )
                finally :
                    for tdrop in tdrops :
                        stop ( tdrop )


            #
            # HAIL BONUS
            #

            def do_hail () :

                @start_async
                def async_col_fall ( cell_x, cell_y_begin, cell_y_end ) :

                    @start_async
                    def async_cell_fall ( cell_x, cell_y ) :
                        frag = FigureInStakan ( rand ( figures.values () ), True, cell_x, cell_y )
                        unfreeze ( frag )
                        y = [ ( 1 - y ) * ( 2 * screen_height + frag.sprite.y + 0.5 * STAKAN_CELL_SIZE ) + y * frag.sprite.y for y in BONUS_HAIL_FALL_Y ]
                        frag.sprite.y = bezier3 ( y [ 0 ], y [ 1 ], y [ 2 ], y [ 3 ], dt = BONUS_HAIL_FALL_TIME )
                        wait ( BONUS_HAIL_FALL_TIME )

                        freeze ( frag )


                    tcells = []
                    try :
                        for cell_y in range ( cell_y_end, cell_y_begin - 1, -1 ) :
                            tcells.append ( async_cell_fall ( cell_x, cell_y ) )
                            wait ( BONUS_HAIL_FALL_DELAY )
                        for tcell in tcells :
                            wait ( tcell )
                    finally :
                        for tcell in tcells :
                            stop ( tcell )


                assert not active_figure

                cells_begin_y = 0
                while is_rows_empty ( cells_begin_y, cells_begin_y ) :
                    cells_begin_y += 1
                    if cells_begin_y > STAKAN_CELLS_Y - 1 :
                        return

                tcols = []

                try :

                    for cell_x in range ( STAKAN_CELLS_X ) :
                        col_begin_y = cells_begin_y
                        while not stakan_cell_get ( cell_x, col_begin_y ) :
                            col_begin_y += 1
                            if col_begin_y > STAKAN_CELLS_Y - 1 :
                                break
                        if col_begin_y > cells_begin_y :
                            tcols.append ( async_col_fall ( cell_x, cells_begin_y, col_begin_y-1 ) )
                            wait ( BONUS_HAIL_FALL_DELAY )

                    for tcol in tcols :
                        wait ( tcol )
                finally :
                    for tcol in tcols :
                        stop ( tcol )


            #
            # EARTHQUAKE BONUS
            #

            def do_earthquake () :

                @start_async
                def async_figure_descend ( figure, dy ) :
                    y = [ figure.sprite.y * ( 1 - y ) + ( figure.sprite.y - dy * STAKAN_CELL_SIZE ) * y for y in BONUS_EARTHQUAKE_DESCEND_Y ]
                    figure.sprite.y = bezier3 ( y [ 0 ], y [ 1 ], y [ 2 ], y [ 3 ], dt = BONUS_EARTHQUAKE_DESCEND_TIME )
                    wait ( BONUS_EARTHQUAKE_DESCEND_TIME )
                    freeze ( figure, bind_x = False )


                @start_async
                def async_stakan_shake () :
                    stakan_sprite.x = ease_out ( STAKAN_X, STAKAN_X - BONUS_EARTHQUAKE_STAKAN_SHAKE_X, dt = 0.5 * BONUS_EARTHQUAKE_STAKAN_SHAKE_TIME )
                    wait ( 0.5 * BONUS_EARTHQUAKE_STAKAN_SHAKE_TIME )
                    stakan_sprite.x = ease ( STAKAN_X - BONUS_EARTHQUAKE_STAKAN_SHAKE_X, STAKAN_X + BONUS_EARTHQUAKE_STAKAN_SHAKE_X, dt = BONUS_EARTHQUAKE_STAKAN_SHAKE_TIME, extend = 'extrapolate' )
                    wait ( BONUS_EARTHQUAKE_STAKAN_SHAKE_DELAY )


                assert not active_figure

                #
                # CALC DESCEND OFFSETS, FRAGMENTATE
                #

                for cell_x in range ( STAKAN_CELLS_X ) :
                    dy = 0
                    for cell_y in range ( STAKAN_CELLS_Y - 1, -1, -1 ) :
                        figure = stakan_cell_get ( cell_x, cell_y )
                        if not figure :
                            dy += 1
                        else :
                            if not figure.is_frag and hasattr ( figure, "earthquake_dy" ) and figure.earthquake_dy != dy :
                                old_dy = figure.earthquake_dy
                                frags = fragmentate ( figure )
                                gactions.handle_action ( actions, gactions.ACTION_FRAG, figure.figure, figure.sprite.x, figure.sprite.y )
                                for frag in frags :
                                    frag.earthquake_dy = old_dy
                                frags = None
                                figure = stakan_cell_get ( cell_x, cell_y )
                            figure.earthquake_dy = dy

                #
                # DO DESCEND
                #

                try :
                    ttasks = []
                    ttasks.append ( async_stakan_shake () )
                    for cell_y in range ( STAKAN_CELLS_Y - 1, -1, -1 ) :
                        for cell_x in range ( STAKAN_CELLS_X ) :
                            figure = stakan_cell_get ( cell_x, cell_y )
                            if figure and hasattr ( figure, "earthquake_dy" ) :
                                unfreeze ( figure )
                                figure.cell_y += figure.earthquake_dy
                                ttasks.append ( async_figure_descend ( figure, figure.earthquake_dy ) )
                                del figure.earthquake_dy
                                wait ( BONUS_EARTHQUAKE_DESCEND_DELAY )

                    for ttask in ttasks :
                        wait ( ttask )

                    time = BONUS_EARTHQUAKE_STAKAN_SHAKE_TIME * float ( abs ( stakan_sprite.x - STAKAN_X ) ) / float ( BONUS_EARTHQUAKE_STAKAN_SHAKE_X )
                    stakan_sprite.x = ease ( end = STAKAN_X, dt = time )
                    wait ( time )

                finally :
                    for ttask in ttasks :
                        stop ( ttask )


            #
            # KING OF HILL BONUS
            #

            def do_king_of_hill () :

                @start_async
                def async_slide_away ( figure ) :
                    assert figure.is_frozen
                    slide_sprite = None
                    if figure.is_frag :
                        slide_sprite = highlights_layer.new_sprite ( figure.figure.frag_texture )
                    else :
                        slide_sprite = highlights_layer.new_sprite ( figure.figure.texture )

                    slide_sprite.shape   = figure.sprite.shape
                    slide_sprite.red     = figure.sprite.red
                    slide_sprite.green   = figure.sprite.green
                    slide_sprite.blue    = figure.sprite.blue
                    slide_sprite.alpha   = figure.sprite.alpha

                    slide_sprite.y       = figure.sprite.y
                    slide_sprite.rot     = figure.sprite.rot

                    figure.sprite.alpha  = 0

                    x = [ figure.sprite.x + screen_height * r for r in BONUS_KING_OF_HILL_SLIDE_X ]
                    s = BONUS_KING_OF_HILL_SLIDE_SCALE

                    slide_sprite.x       = bezier3 ( x [ 0 ], x [ 1 ], x [ 2 ], x [ 3 ], dt = BONUS_KING_OF_HILL_SLIDE_TIME )
                    slide_sprite.scale   = bezier3 ( s [ 0 ], s [ 1 ], s [ 2 ], s [ 3 ], dt = BONUS_KING_OF_HILL_SLIDE_TIME )

                    try :
                        wait ( BONUS_KING_OF_HILL_SLIDE_TIME )
                    finally :
                        slide_sprite.kill ()


                assert active_figure
                assert active_figure.is_frozen

                #
                # DETERMINE ROWS TO DESTROY
                #

                yfrom = 1000
                yto   = 0
                for colshape_y in range ( active_figure.cells ) :
                    colrow_empty = True
                    for colshape_x in range ( active_figure.cells ) :
                        if active_figure.colshape () [ colshape_y ] [ colshape_x ] :
                            colrow_empty = False
                            break
                    if colrow_empty :
                        continue
                    yfrom = min ( yfrom, colshape_y + active_figure.cell_y )
                    yto   = max ( yto  , colshape_y + active_figure.cell_y )

                #
                # FRAGMENTATE
                #

                for figure in figures_intersecting_rows ( yfrom, yto ) :
                    fragmentate ( figure )
                    gactions.handle_action ( actions, gactions.ACTION_FRAG, figure.figure, figure.sprite.x, figure.sprite.y )

                #
                # SLIDE AWAY
                #

                for figure in figures_in_rows ( yfrom, yto ) :
                    async_slide_away ( figure )
                    if not figure.is_frag :
                        gactions.handle_action ( actions, gactions.ACTION_SWALLOW, figure.figure, figure.sprite.x, figure.sprite.y )
                    work_async ()

                #
                # DESCEND REST OF STAKAN
                #

                if yfrom > 0 :
                    descend ( yfrom, yto )


            #
            # BUILDER BONUS
            #

            def do_builder () :

                @start_async
                def async_put_brick ( cell_source_x, cell_source_y, cell_y ) :
                    frag = FigureInStakan ( active_figure.figure, True, cell_source_x, cell_y )
                    brick_sprite = highlights_layer.new_sprite ( frag.figure.frag_texture )

                    frag.sprite.red      = active_figure.sprite.red
                    frag.sprite.green    = active_figure.sprite.green
                    frag.sprite.blue     = active_figure.sprite.blue

                    brick_sprite.red     = frag.sprite.red
                    brick_sprite.green   = frag.sprite.green
                    brick_sprite.blue    = frag.sprite.blue

                    brick_sprite.shape   = frag.sprite.shape
                    brick_sprite.x       = frag.sprite.x

                    frag.sprite.alpha    = 0

                    yfrom = frag.sprite.y + STAKAN_CELL_SIZE * ( cell_y - cell_source_y )
                    yto   = frag.sprite.y

                    y = [ yfrom * ( 1.0 - y ) + yto * y for y in BONUS_BUILDER_BRICK_Y ]
                    s = BONUS_BUILDER_BRICK_SCALE
                    r = [ r * 360 for r in BONUS_BUILDER_BRICK_ROTATE ]
                    a = BONUS_BUILDER_BRICK_ALPHA

                    brick_sprite.alpha = bezier3 ( a [ 0 ], a [ 1 ], a [ 2 ], a [ 3 ], dt = BONUS_BUILDER_BRICK_TIME )
                    brick_sprite.y     = bezier3 ( y [ 0 ], y [ 1 ], y [ 2 ], y [ 3 ], dt = BONUS_BUILDER_BRICK_TIME )
                    brick_sprite.scale = bezier3 ( s [ 0 ], s [ 1 ], s [ 2 ], s [ 3 ], dt = BONUS_BUILDER_BRICK_TIME )
                    brick_sprite.rot   = bezier3 ( r [ 0 ], r [ 1 ], r [ 2 ], r [ 3 ], dt = BONUS_BUILDER_BRICK_TIME )

                    try :
                        wait ( BONUS_BUILDER_BRICK_TIME )
                    finally :
                        brick_sprite.kill ()
                        frag.sprite.alpha = 1
                        freeze ( frag )


                assert active_figure
                assert active_figure.is_frozen

                #
                # FILL COLSHAPE OFFSETS
                #

                cell_sources_xy = []

                for colshape_x in range ( active_figure.cells ) :
                    for colshape_y in range ( active_figure.cells - 1, -1, -1 ) :
                        if active_figure.colshape () [ colshape_y ] [ colshape_x ] :
                            cell_sources_xy.append ( ( colshape_x + active_figure.cell_x, colshape_y + active_figure.cell_y ) )

                #
                # LEFT-TO-RIGHT THEN RIGHT-TO-LEFT
                #

                tspawns = []

                try :
                    anybody_spawned = True
                    while anybody_spawned :
                        anybody_spawned = False
                        for cell_source_i in range ( len ( cell_sources_xy ) ) + range ( len ( cell_sources_xy ) - 2, 0, -1 ) :
                            cell_source_x, cell_source_y = cell_sources_xy [ cell_source_i ]
                            for cell_y in range ( STAKAN_CELLS_Y - 1, cell_source_y, -1 ) :
                                if stakan_cell_get ( cell_source_x, cell_y ) :
                                    continue
                                anybody_spawned = True
                                tspawns.append ( async_put_brick ( cell_source_x, cell_source_y, cell_y ) )
                                wait ( BONUS_BUILDER_BRICK_DELAY )
                                break
                    for tspawn in tspawns :
                        wait ( tspawn )
                finally :
                    for tspawn in tspawns :
                        stop ( tspawn )

            #
            # LET THE GAME BEGIN
            #

            figures_generation    = 1
            figures_last_selected = {}
            for figure_type in figures.keys () :
                figures_last_selected [ figure_type ] = 0

            trotate         = None
            tmove_side      = None
            tmove_down      = None
            active_figure   = None
            try :
                while work_async () :

                    #
                    # CHOOSE NEXT FIGURE TYPE
                    #

                    figure_template = rand ( figures.values () )
                    while figures_last_selected [ figure_template.type ] == figures_generation :
                        figure_template = rand ( figures.values () )
                    for figure_type in figures_last_selected :
                        if figures_generation - figures_last_selected [ figure_type ] >= len ( figures.values () ) + FIGURE_SELECTION_THRESHOLD :
                            figure_template = figures [ figure_type ]
                            break
                    figures_generation += 1
                    figures_last_selected [ figure_template.type ] = figures_generation

                    #
                    # TRY TO FIT FIGURE IN STAKAN
                    #

                    cell_y = 0
                    cell_x = ( STAKAN_CELLS_X - figure_template.cells ) / 2
                    if not can_fit ( figure_template.rotations [ 0 ], cell_x, cell_y ) :
                        # GAME OVER
                        wait_missed ( event_stakan_hidden )
                        return

                    #
                    # ACTIVATE ACTIVE BONUSES
                    #

                    if bonus_super_drop.can_be_activated :
                        gbonuses.activate ( bonus_super_drop )
                    elif bonus_super_hit.can_be_activated :
                        gbonuses.activate ( bonus_super_hit )
                    elif bonus_builder.can_be_activated :
                        gbonuses.activate ( bonus_builder )
                    elif bonus_king_of_hill.can_be_activated :
                        gbonuses.activate ( bonus_king_of_hill )

                    #
                    # SPAWN FIGURE IN STAKAN
                    #

                    active_figure = FigureInStakan ( figure_template, False, cell_x, cell_y )
                    y = stakan_sprite.top + 2 * active_figure.cell_half_size
                    active_figure.sprite.y = ease_out ( y, active_figure.sprite.y, dt = FIGURE_APPEAR_TIME )
                    active_figure.sprite.scale = ease_out ( 0, 1, dt = FIGURE_APPEAR_TIME )
                    wait ( FIGURE_APPEAR_TIME )

                    #
                    # PLAY UNTIL FIGURE REACHES GROUND
                    #

                    trotate     = async_rotate    ()
                    tmove_side  = async_move_side ()
                    tmove_down  = async_move_down ()

                    while not active_figure.is_frozen :
                        work_async ()

                    stop ( trotate    )
                    stop ( tmove_side )
                    stop ( tmove_down )

                    #
                    # RESET ACTIVE BONUSES
                    #

                    if bonus_super_drop.is_active :
                        gbonuses.reset      ( bonus_super_drop )
                    if bonus_super_hit.is_active :
                        gbonuses.reset      ( bonus_super_hit )
                    if bonus_builder.is_active :
                        do_builder          ()
                        gbonuses.reset      ( bonus_builder )
                    if bonus_king_of_hill.is_active :
                        do_king_of_hill     ()
                        gbonuses.reset      ( bonus_king_of_hill )

                    active_figure = None

                    need_eating = True

                    while need_eating :

                        need_eating = False

                        eat_rows ()

                        # WAIT ALL ASYNC TASKS TO FINISH
                        gactions.wait_async_tasks ()
                        gbonuses.wait_async_tasks ()

                        #
                        # ACTIVATE PASSIVE BONUSES
                        #

                        if bonus_acid_rain.can_be_activated :
                            gbonuses.activate   ( bonus_acid_rain )
                            do_acid_rain        ()
                            gbonuses.reset      ( bonus_acid_rain )
                        if bonus_hail.can_be_activated :
                            gbonuses.activate   ( bonus_hail )
                            do_hail             ()
                            gbonuses.reset      ( bonus_hail )
                            need_eating         = True
                        if bonus_earthquake.can_be_activated :
                            gbonuses.activate   ( bonus_earthquake )
                            do_earthquake       ()
                            gbonuses.reset      ( bonus_earthquake )
                            need_eating         = True

                        if gbonuses.activation_update ( bonuses ) :
                            need_eating         = True

            finally :
                stop ( trotate    )
                stop ( tmove_side )
                stop ( tmove_down )

                if active_figure :
                    freeze ( active_figure )

                gactions.wait_async_tasks ()
                gbonuses.wait_async_tasks ()


        def stakan_cell_get ( x, y ) :
            return stakan [ y ] [ x ]


        def stakan_cell_set ( x, y, cell ) :
            global stakan
            stakan [ y ] [ x ] = cell


        def stakan_clear_rows ( yfrom, yto ) :
            global stakan
            for row in stakan_rows ( yfrom, yto ) :
                for x in range ( STAKAN_CELLS_X ) :
                    row [ x ] = None


        def stakan_rows ( yfrom, yto ) :
            return stakan [ yfrom : yto + 1 ]


        #
        # CREATE BONUSES
        #

        def bonus_add ( bonus_type, action_type, y_num ) :
            bonus_actions = []
            x = ACTIONS_X + BONUS_STEP_X
            y = ACTIONS_Y - ACTIONS_STEP_Y * y_num
            for figure in figures.values () :
                bonus_actions.append ( gactions.Action ( action_type, figure, x, y ) )
                x += ACTIONS_STEP_X
                work_async ()
            bonus = gbonuses.Bonus ( bonus_type, bonus_actions, ACTIONS_X, y )
            bonuses.append ( bonus )
            for action in bonus_actions :
                action.bonus = bonus
            return bonus


        bonuses = []
        actions = []

        bonus_super_drop    = bonus_add ( gbonuses.BONUS_SUPER_DROP   , gactions.ACTION_DROP   , 0 )
        bonus_super_hit     = bonus_add ( gbonuses.BONUS_SUPER_HIT    , gactions.ACTION_HIT    , 1 )
        bonus_builder       = bonus_add ( gbonuses.BONUS_BUILDER      , gactions.ACTION_GROUND , 2 )
        bonus_king_of_hill  = bonus_add ( gbonuses.BONUS_KING_OF_HILL , gactions.ACTION_ROTATE , 3 )
        bonus_acid_rain     = bonus_add ( gbonuses.BONUS_ACID_RAIN    , gactions.ACTION_FRAG   , 4 )
        bonus_hail          = bonus_add ( gbonuses.BONUS_HAIL         , gactions.ACTION_SWALLOW, 5 )
        bonus_earthquake    = bonus_add ( gbonuses.BONUS_EARTHQUAKE   , gactions.ACTION_FLOAT  , 6 )

        for bonus in bonuses :
            actions += bonus.actions

        # CREATE STAKAN
        global stakan
        stakan = [ [ None for i in range ( STAKAN_CELLS_X ) ] for i in range ( STAKAN_CELLS_Y ) ]

        # WAIT SHOW SIGNAL
        wait_missed ( event_show_game )

        # SHOW ACTIONS
        tbonuses_show = gbonuses.async_show ( bonuses )

        # SHOW STAKAN
        stakan_sprite = stakan_layer.new_sprite ( STAKAN_TEXTURE )
        stakan_sprite.shape = [ -STAKAN_HALF_SIZE_X, STAKAN_HALF_SIZE_Y, STAKAN_HALF_SIZE_X, -STAKAN_HALF_SIZE_Y ]
        x = [ STAKAN_X + x * screen_width for x in STAKAN_APPEAR_X_SHIFT ]
        stakan_sprite.x = bezier3 ( x [ 0 ], x [ 1 ], x [ 2 ], x [ 3 ], dt = STAKAN_APPEAR_TIME )
        wait ( STAKAN_APPEAR_TIME )
        wait ( tbonuses_show )

        # WE'RE SHOWN
        event_stakan_shown ()

        # PLAY GAME
        tgame = async_game_play ()

        # WAIT HIDE SIGNAL
        wait_missed ( event_hide_game )

        # STOP GAME
        stop ( tgame )

        # HIDE ACTIONS
        tbonuses_hide = gbonuses.async_hide ( bonuses )

        # HIDE STAKAN
        x = [ STAKAN_X + x * screen_width for x in STAKAN_DISAPPEAR_X_SHIFT ]
        stakan_sprite.x = bezier3 ( x [ 0 ], x [ 1 ], x [ 2 ], x [ 3 ], dt = STAKAN_DISAPPEAR_TIME )
        wait ( STAKAN_DISAPPEAR_TIME )
        wait ( tbonuses_hide )

        # CLEAN UP
        stakan_sprite.kill ()
        stakan  = None
        for action in actions :
            action.bonus = None
        actions = None
        bonuses = None

        # WE'RE HIDDEN
        event_stakan_hidden ()


    def show_game () :
        skip_missed ( event_stakan_shown   )
        skip_missed ( event_left_shown     )
        skip_missed ( event_right_shown    )
        skip_missed ( event_rotate_shown   )
        skip_missed ( event_down_shown     )
        skip_missed ( event_pause_shown    )
        event_show_game ()
        wait_missed ( event_stakan_shown   )
        wait_missed ( event_left_shown     )
        wait_missed ( event_right_shown    )
        wait_missed ( event_rotate_shown   )
        wait_missed ( event_down_shown     )
        wait_missed ( event_pause_shown    )


    def hide_game () :
        skip_missed ( event_stakan_hidden   )
        skip_missed ( event_left_hidden     )
        skip_missed ( event_right_hidden    )
        skip_missed ( event_rotate_hidden   )
        skip_missed ( event_down_hidden     )
        skip_missed ( event_pause_hidden    )
        event_hide_game ()
        wait_missed ( event_stakan_hidden   )
        wait_missed ( event_left_hidden     )
        wait_missed ( event_right_hidden    )
        wait_missed ( event_rotate_hidden   )
        wait_missed ( event_down_hidden     )
        wait_missed ( event_pause_hidden    )

    @start_async
    def async_catch_left ( keys ) :
        while work_async () :
            keys.left = False
            wait ( event_left_push )
            keys.left = True
            wait ( event_left_pop )

    @start_async
    def async_catch_right ( keys ) :
        while work_async () :
            keys.right = False
            wait ( event_right_push )
            keys.right = True
            wait ( event_right_pop )

    @start_async
    def async_catch_rotate ( keys ) :
        while work_async () :
            keys.rotate = False
            wait ( event_rotate_push )
            keys.rotate = True
            wait ( event_rotate_pop )

    @start_async
    def async_catch_down ( keys ) :
        while work_async () :
            keys.down = False
            wait ( event_down_push )
            keys.down = True
            wait ( event_down_pop )

    # KEYS

    keys                    = Keys ()

    # EVENTS

    event_hide_game         = Event ()
    event_stakan_hidden     = Event ()
    event_left_hidden       = Event ()
    event_right_hidden      = Event ()
    event_rotate_hidden     = Event ()
    event_down_hidden       = Event ()
    event_pause_hidden      = Event ()

    event_show_game         = Event ()
    event_stakan_shown      = Event ()
    event_left_shown        = Event ()
    event_right_shown       = Event ()
    event_rotate_shown      = Event ()
    event_down_shown        = Event ()
    event_pause_shown       = Event ()

    event_left_push         = Event ()
    event_left_pop          = Event ()
    event_right_push        = Event ()
    event_right_pop         = Event ()
    event_rotate_push       = Event ()
    event_rotate_pop        = Event ()
    event_down_push         = Event ()
    event_down_pop          = Event ()
    event_pause_push        = Event ()
    event_pause_pop         = Event ()

    # KEYS

    tkeys = [ gkey.async_work ( KEY_LEFT_TEXTURE, KEY_LEFT_X, KEY_LEFT_Y, KEY_LEFT_DELAY
                              , event_hide_game, event_left_hidden
                              , event_show_game, event_left_shown
                              , event_left_push, event_left_pop
                              , key_left )
            , gkey.async_work ( KEY_RIGHT_TEXTURE, KEY_RIGHT_X, KEY_RIGHT_Y, KEY_RIGHT_DELAY
                              , event_hide_game, event_right_hidden
                              , event_show_game, event_right_shown
                              , event_right_push, event_right_pop
                              , key_right )
            , gkey.async_work ( KEY_ROTATE_TEXTURE, KEY_ROTATE_X, KEY_ROTATE_Y, KEY_ROTATE_DELAY
                              , event_hide_game, event_rotate_hidden
                              , event_show_game, event_rotate_shown
                              , event_rotate_push, event_rotate_pop
                              , key_up )
            , gkey.async_work ( KEY_DOWN_TEXTURE, KEY_DOWN_X, KEY_DOWN_Y, KEY_DOWN_DELAY
                              , event_hide_game, event_down_hidden
                              , event_show_game, event_down_shown
                              , event_down_push, event_down_pop
                              , key_down )
            , gkey.async_work ( KEY_PAUSE_TEXTURE, KEY_PAUSE_X, KEY_PAUSE_Y, KEY_PAUSE_DELAY
                              , event_hide_game, event_pause_hidden
                              , event_show_game, event_pause_shown
                              , event_pause_push, event_pause_pop
                              , key_back )
            ]

    tkey_catchers = [ async_catch_left   ( keys )
                    , async_catch_right  ( keys )
                    , async_catch_rotate ( keys )
                    , async_catch_down   ( keys )
                    ]

    # GAME

    tgame = async_work_game ()

    # WORK

    show_game ()
    wait ( event_pause_push )
    hide_game ()

    # CLEAN UP

    for ttask in tkeys + tkey_catchers :
        stop ( ttask )
    stop ( tgame )

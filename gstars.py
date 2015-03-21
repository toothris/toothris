# -*- coding: cp1251 -*-

# BASE
from bapi import *

# GAME
import glayers


# CONSTS


STARS_MAX_COUNT         = 50


STAR_TEXTURES = \
[ "res/ui_menu/064x064_star1.png"
, "res/ui_menu/064x064_star2.png"
, "res/ui_menu/064x064_star3.png"
, "res/ui_menu/064x064_star4.png"
]
STAR_SIZE               = screen_height * 0.05
STAR_SCALE_MIN          = 0.4
STAR_SCALE_MAX          = 1
STAR_ROTATE_TIME_MIN    = 1
STAR_ROTATE_TIME_MAX    = 5
STAR_ROTATE_CW_AND_CCW  = False
STAR_START_DELAY_MIN    = 0
STAR_START_DELAY_MAX    = 5
STAR_SCALE_TIME_MIN     = 1
STAR_SCALE_TIME_MAX     = 3
STAR_SCALE_DELAY_MIN    = 0
STAR_SCALE_DELAY_MAX    = 1
STAR_MORPH_TIME_MIN     = 0.5
STAR_MORPH_TIME_MAX     = 2

EXPLOSION_TEXTURES = \
[ "res/ui_menu/064x064_splat1.png"
, "res/ui_menu/064x064_splat2.png"
, "res/ui_menu/064x064_splat3.png"
, "res/ui_menu/064x064_splat4.png"
]
EXPLOSION_SCALE        = [ 0, 0.1, 3  , 1.5 ]
EXPLOSION_ROTATE       = [ 0, 0.5, 0.9, 1   ]
EXPLOSION_SHRINK_TIME  = 0.5
EXPLOSION_GROW_TIME    = 1.0
EXPLOSION_FADE_TIME    = 0.3


# ALIASES

stars_layer      = layer ( glayers.STARS            )
explosions_layer = layer ( glayers.STARS_EXPLOSIONS )


def prefetch () :
    for texture in STAR_TEXTURES :
        stars_layer.prefetch_sprites      ( texture, STARS_MAX_COUNT )
    for texture in EXPLOSION_TEXTURES :
        explosions_layer.prefetch_sprites ( texture, STARS_MAX_COUNT )


@start_async
def async_show () :

    @start_async
    def async_star () :
        if len ( STAR_TEXTURES ) == 0 :
            return

        shape = [ -STAR_SIZE, STAR_SIZE, STAR_SIZE, -STAR_SIZE ]

        star_sprites      = queue ( [ stars_layer.new_sprite      ( t ) for t in STAR_TEXTURES      ] )
        explosion_sprites = queue ( [ explosions_layer.new_sprite ( t ) for t in EXPLOSION_TEXTURES ] )

        star = star_sprites [ 0 ]
        star.scale = 0

        for sprite in star_sprites :
            if sprite != star :
                sprite.x        = lambda : star.x
                sprite.y        = lambda : star.y
                sprite.scale    = lambda : star.scale
                sprite.rot      = lambda : star.rot
            sprite.alpha        = 0
            sprite.shape        = shape

        explosion = explosion_sprites [ 0 ]
        explosion.scale = 0

        for sprite in explosion_sprites :
            if sprite != explosion :
                sprite.scale    = lambda : explosion.scale
                sprite.rot      = lambda : explosion.rot
            sprite.x            = lambda : star.x
            sprite.y            = lambda : star.y
            sprite.alpha        = 0
            sprite.shape        = shape

        event_respawn = Event ()
        tmorph = None
        tscale = None
        tclick = None
        try :
            while work_async () :
                scale       = rand ( STAR_SCALE_MIN         , STAR_SCALE_MAX        )
                scale_time  = rand ( STAR_SCALE_TIME_MIN    , STAR_SCALE_TIME_MAX   )
                scale_delay = rand ( STAR_SCALE_DELAY_MIN   , STAR_SCALE_DELAY_MAX  )
                start_delay = rand ( STAR_START_DELAY_MIN   , STAR_START_DELAY_MAX  )
                rotate_time = rand ( STAR_ROTATE_TIME_MIN   , STAR_ROTATE_TIME_MAX  )
                morph_time  = rand ( STAR_MORPH_TIME_MIN    , STAR_MORPH_TIME_MAX   )

                if STAR_ROTATE_CW_AND_CCW and rand ( ( True, False ) ) :
                    rotate_time *= -1.0

                if scale > screen_width or scale > screen_height :
                    continue

                x_bound = screen_width  * ( 1.0 - scale * STAR_SIZE )
                y_bound = screen_height * ( 1.0 - scale * STAR_SIZE )
                x = rand ( - x_bound, x_bound )
                y = rand ( - y_bound, y_bound )

                star.x, star.y = x, y
                star.rot = lerp ( 0, 360, dt = rotate_time, extend = 'extrapolate' )

                @start_async
                def async_morph () :
                    if len ( star_sprites ) > 1 and morph_time > 0.0 :
                        while work_async () :
                            star_sprites [ 0 ].alpha = ease_out ( 1, 0, dt = morph_time )
                            star_sprites [ 1 ].alpha = ease_out ( 0, 1, dt = morph_time )
                            wait ( morph_time )
                            star_sprites.rotate ( -1 )

                    elif len ( star_sprites ) == 1 :
                        star_sprites [ 0 ].alpha = 1

                @start_async
                def async_scale () :
                    wait ( start_delay )
                    star.scale = ease_out ( 0, scale, dt = scale_time )
                    wait ( scale_time + scale_delay )
                    star.scale = ease_in  ( scale, 0, dt = scale_time )
                    wait ( scale_time )
                    event_respawn ()

                @start_async
                def async_catch_click () :

                    def under_cursor () :
                        mouse_x, mouse_y = mouse_pos ()
                        return  star.left   < mouse_x \
                           and  star.right  > mouse_x \
                           and  star.top    > mouse_y \
                           and  star.bottom < mouse_y

                    while work_async () :
                        wait ( stars_layer.key_click.push )
                        while not under_cursor () :
                            wait ( stars_layer.key_click.push )
                        stars_layer.handled_key_click.push ()

                        stop ( tscale )

                        s = [ float ( scale ) * p for p in EXPLOSION_SCALE  ]
                        r = [ 360.0           * p for p in EXPLOSION_ROTATE ]

                        star.scale = lerp ( star.scale, 0, dt = EXPLOSION_SHRINK_TIME * star.scale / scale )
                        explosion.scale = bezier3 ( s [ 0 ], s [ 1 ], s [ 2 ], s [ 3 ], dt = EXPLOSION_GROW_TIME )
                        explosion.rot   = bezier3 ( r [ 0 ], r [ 1 ], r [ 2 ], r [ 3 ], dt = EXPLOSION_GROW_TIME )

                        explosion_iterations = len ( explosion_sprites ) - 1
                        explosion_time = float ( EXPLOSION_GROW_TIME - EXPLOSION_FADE_TIME ) / explosion_iterations
                        for i in range ( explosion_iterations ) :
                            explosion_sprites [ 0 ].alpha = ease_out ( 1, 0, dt = explosion_time )
                            explosion_sprites [ 1 ].alpha = ease_out ( 0, 1, dt = explosion_time )
                            wait ( explosion_time )
                            explosion_sprites.rotate ( -1 )
                        explosion_sprites [ 0 ].alpha = lerp ( 1, 0, dt = EXPLOSION_FADE_TIME )
                        wait ( EXPLOSION_FADE_TIME )
                        explosion_sprites.rotate ( -1 )

                        event_respawn ()

                if not working ( tmorph ) :
                    tmorph = async_morph ()

                if not working ( tclick ) :
                    tclick = async_catch_click ()

                tscale = async_scale ()
                wait ( event_respawn )
                stop ( tscale )

        finally :
            stop ( tscale )
            stop ( tmorph )
            stop ( tclick )
            for sprite in explosion_sprites :
                sprite.kill ()
            for sprite in star_sprites :
                sprite.kill ()


    tstars = None
    try :
        tstars = [ async_star () for i in range ( STARS_MAX_COUNT ) ]
        while work_async () :
            wait ( 100000 )
    finally :
        for tstar in tstars :
            stop ( tstar )

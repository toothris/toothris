# -*- coding: cp1251 -*-

# BASE
from bapi import *

# GAME
import glayers

# CONSTS

KEYS_MAX_COUNT          = 10

KEY_SIZE                = 0.1 * screen_height
KEY_APPEAR_TIME         = 0.5
KEY_APPEAR_SCALE        = [ 0, 0.5, 2.0, 1 ]
KEY_APPEAR_ROTATE       = [ 0, 1.6, 1.8, 2 ]
KEY_DISAPPEAR_TIME      = 0.5
KEY_DISAPPEAR_SCALE     = [ 1, 2.0, 0.5, 0 ]
KEY_DISAPPEAR_ROTATE    = [ 0, 0.2, 0.4, 2 ]
KEY_FOCUS_SCALE         = 0.9
KEY_FOCUS_PERIOD        = 0.3
KEY_ROT_AMP             = 7
KEY_ROT_PERIOD          = 1
KEY_PUSH_TIME           = 0.3
KEY_PUSH_SCALE          = [ 1, 0.7, 0.5, 0.7 ]
KEY_POP_TIME            = 0.3
KEY_POP_SCALE           = [ 0.7, 1.0, 1.2, 1 ]


SELECTION_TEXTURES      = \
[ "res/game/064x064_selected1.png"
, "res/game/064x064_selected2.png"
, "res/game/064x064_selected3.png"
, "res/game/064x064_selected4.png"
]
SELECTION_ROT_AMP       = 2
SELECTION_ROT_PERIOD    = 0.2
SELECTION_MORPH_TIME    = 0.5
SELECTION_SCALE         = 1.3


# ALIASES

keys_layer      = layer ( glayers.KEYS           )
selection_layer = layer ( glayers.KEYS_SELECTION )


def prefetch () :
    for texture in SELECTION_TEXTURES :
        selection_layer.prefetch_sprites ( texture, KEYS_MAX_COUNT )


def prefetch_keys ( texture, count ) :
    keys_layer.prefetch_sprites ( texture, count )


@start_async
def async_work ( key_texture, x, y, delay
               , event_hide, event_hidden
               , event_show, event_shown
               , event_push
               , event_pop
               , virtual_key
               ) :

    key_sprite          = keys_layer.new_sprite ( key_texture )
    selection_sprites   = queue ( [ selection_layer.new_sprite ( t ) for t in SELECTION_TEXTURES ] )

    key_sprite.shape    = [ -KEY_SIZE, KEY_SIZE, KEY_SIZE, -KEY_SIZE ]
    key_sprite.x        = x
    key_sprite.y        = y
    key_sprite.scale    = 0

    for sprite in selection_sprites :
        sprite.x        = x
        sprite.y        = y
        sprite.scale    = SELECTION_SCALE
        sprite.alpha    = 0
        sprite.shape    = key_sprite.shape
        sprite.rot      = ease_in ( -SELECTION_ROT_AMP, SELECTION_ROT_AMP, dt = SELECTION_ROT_PERIOD, extend = 'extrapolate' )

    focus_left          = x - KEY_SIZE
    focus_right         = x + KEY_SIZE
    focus_top           = y + KEY_SIZE
    focus_bottom        = y - KEY_SIZE


    def show () :
        wait ( delay )
        s = [ s for s in KEY_APPEAR_SCALE ]
        r = [ r * 360 for r in KEY_APPEAR_ROTATE ]
        key_sprite.scale    = bezier3 ( s [ 0 ], s [ 1 ], s [ 2 ], s [ 3 ], dt = KEY_APPEAR_TIME )
        key_sprite.rot      = bezier3 ( r [ 0 ], r [ 1 ], r [ 2 ], r [ 3 ], dt = KEY_APPEAR_TIME )
        wait ( KEY_APPEAR_TIME )
        key_sprite.rot      = ease_in ( -KEY_ROT_AMP, KEY_ROT_AMP, dt = KEY_ROT_PERIOD, extend = 'extrapolate' )


    def hide () :
        wait ( delay )
        r = [ key_sprite.rot   + r * 360 for r in KEY_DISAPPEAR_ROTATE ]
        s = [ key_sprite.scale * s       for s in KEY_DISAPPEAR_SCALE  ]
        key_sprite.scale    = bezier3 ( s [ 0 ], s [ 1 ], s [ 2 ], s [ 3 ], dt = KEY_DISAPPEAR_TIME )
        key_sprite.rot      = bezier3 ( r [ 0 ], r [ 1 ], r [ 2 ], r [ 3 ], dt = KEY_DISAPPEAR_TIME )
        for sprite in selection_sprites :
            sprite.alpha    = lerp ( sprite.alpha, 0, dt = sprite.alpha * min ( KEY_DISAPPEAR_TIME, SELECTION_MORPH_TIME ) )
        wait ( KEY_DISAPPEAR_TIME )


    def isfocused () :
        mouse_x, mouse_y = mouse_pos ()
        return  focus_left   < mouse_x \
           and  focus_right  > mouse_x \
           and  focus_top    > mouse_y \
           and  focus_bottom < mouse_y


    @start_async
    def async_live () :

        @start_async
        def async_focus () :

            @start_async
            def async_focus_got () :
                wait ( SELECTION_MORPH_TIME )
                selection_sprites [ 0 ].alpha = ease_out ( 0, 1, dt = SELECTION_MORPH_TIME )
                wait ( SELECTION_MORPH_TIME )
                while work_async () :
                    selection_sprites [ 0 ].alpha = ease_out ( 1, 0, dt = SELECTION_MORPH_TIME )
                    selection_sprites [ 1 ].alpha = ease_out ( 0, 1, dt = SELECTION_MORPH_TIME )
                    wait ( SELECTION_MORPH_TIME )
                    selection_sprites.rotate ( -1 )


            @start_async
            def async_focus_lost () :
                time_max = 0

                for sprite in selection_sprites :
                    time = SELECTION_MORPH_TIME * sprite.alpha
                    sprite.alpha = lerp ( sprite.alpha, 0, dt = time )
                    time_max = max ( time_max, time )

                wait ( time_max )


            tfocusgot   = None
            tfocuslost  = None
            try :
                while work_async () :
                    if isfocused () and not working ( tfocusgot ) :
                        stop ( tfocuslost )
                        tfocusgot = async_focus_got ()
                    if not isfocused () and not working ( tfocuslost ) :
                        stop ( tfocusgot )
                        tfocuslost = async_focus_lost ()
            finally :
                stop ( tfocusgot )
                stop ( tfocuslost )


        @start_async
        def async_push () :
            s = [ s for s in KEY_PUSH_SCALE ]
            s [ 0 ] = key_sprite.scale
            key_sprite.scale = bezier3 ( s [ 0 ], s [ 1 ], s [ 2 ], s [ 3 ], dt = KEY_PUSH_TIME )
            wait ( KEY_PUSH_TIME )


        @start_async
        def async_pop ( play_pushed_anim ) :
            if play_pushed_anim :
                s = [ s for s in KEY_POP_SCALE ]
                s [ 0 ] = key_sprite.scale
                key_sprite.scale = bezier3 ( s [ 0 ], s [ 1 ], s [ 2 ], s [ 3 ], dt = KEY_POP_TIME )
                wait ( KEY_POP_TIME )
            while work_async () :
                while not isfocused () :
                    work_async ()
                key_sprite.scale = ease_out ( 1, KEY_FOCUS_SCALE, dt = KEY_FOCUS_PERIOD, extend = 'extrapolate' )
                while isfocused () :
                    work_async ()
                key_sprite.scale = lerp ( key_sprite.scale, 1, dt = KEY_FOCUS_PERIOD * ( 1.0 - key_sprite.scale ) )


        @start_async
        def async_pushpop () :
            tpress = async_pop ( False )
            try:
                while work_async () :
                    wait ( event_push )
                    stop ( tpress )
                    tpress = async_push ()
                    wait ( event_pop )
                    stop ( tpress )
                    tpress = async_pop ( True )
            finally :
                stop ( tpress )


        @start_async
        def async_catch_click () :
            wait ( keys_layer.key_click.push )
            while not isfocused () :
                wait ( keys_layer.key_click.push )
            stop ( tcatch_virtual_key )
            keys_layer.handled_key_click.push ()
            event_push ()
            wait ( keys_layer.key_click.pop )
            keys_layer.handled_key_click.pop ()
            event_pop ()


        @start_async
        def async_catch_virtual_key () :
            wait ( virtual_key.push )
            stop ( tcatch_click )
            event_push ()
            wait ( virtual_key.pop )
            event_pop ()


        tfocus              = async_focus ()
        tpushpop            = async_pushpop ()
        tcatch_click        = async_catch_click ()
        tcatch_virtual_key  = async_catch_virtual_key ()
        try :
            while work_async () :
                if not working ( tcatch_click ) :
                    wait ( tcatch_virtual_key )
                    tcatch_click        = async_catch_click ()
                    tcatch_virtual_key  = async_catch_virtual_key ()
                if not working ( tcatch_virtual_key ) :
                    wait ( tcatch_click )
                    tcatch_click        = async_catch_click ()
                    tcatch_virtual_key  = async_catch_virtual_key ()

        finally :
            stop ( tfocus )
            stop ( tpushpop )
            stop ( tcatch_click )
            stop ( tcatch_virtual_key )


    tlive = None
    try:
        while work_async    () :
            wait_missed     ( event_show )
            show            ()
            event_shown     ()

            tlive = async_live ()

            wait_missed     ( event_hide )
            stop            ( tlive )
            hide            ()
            event_hidden    ()

    finally:
        stop ( tlive )
        key_sprite.kill ()
        for sprite in selection_sprites :
            sprite.kill ()

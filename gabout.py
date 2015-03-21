# -*- coding: cp1251 -*-

# BASE
from bapi import *

# GAME
import gbutton
import glayers

# CONSTS

LOGO_TEXTURE            = "res/ui_about/256x256_logo.png"
LOGO_SIZE_X             = 0.5 * screen_height
LOGO_SIZE_Y             = 0.5 * screen_height
LOGO_POS_X              = 0
LOGO_POS_Y              = 0.2 * screen_height
LOGO_ROTATION_PERIODS   = 5
LOGO_APPEAR_TIME        = 2
LOGO_APPEAR_SCALE       = [ 0, 0.1, 2.5, 1 ]
LOGO_APPEAR_ROTATION    = [ 0, 0.5, 0.95, 1 ]
LOGO_FLOAT_ROTATION     = 2
LOGO_FLOAT_PERIOD       = 2
LOGO_HIDE_TIME          = 2
LOGO_HIDE_SCALE         = [ 1, 2.5, 0.1, 0 ]
LOGO_HIDE_ROTATION      = [ 0, 0.05, 0.5, 1 ]

BUTTON_EXIT_TEXTURE     = "res/ui_menu/256x064_exit.png"
BUTTON_NUMBER_OFFSET    = -2


# ALIASES

logo_layer = layer ( glayers.LOGO )


def prefetch () :
    logo_layer.prefetch_sprites ( LOGO_TEXTURE        , 1 )
    gbutton.prefetch_buttons    ( BUTTON_EXIT_TEXTURE , 1 )


def show () :

    @start_async
    def async_work_logo () :

        sprite = logo_layer.new_sprite ( LOGO_TEXTURE )

        sprite.shape = [ - LOGO_SIZE_X, LOGO_SIZE_Y, LOGO_SIZE_X, - LOGO_SIZE_Y ]
        sprite.x = LOGO_POS_X
        sprite.y = LOGO_POS_Y
        sprite.scale = 0

        wait_missed ( event_show_menu )

        scale = LOGO_APPEAR_SCALE
        rot = [ rot * LOGO_ROTATION_PERIODS * 360.0 for rot in LOGO_APPEAR_ROTATION ]
        rot [ 3 ] += LOGO_FLOAT_ROTATION

        sprite.scale = bezier3 ( scale [ 0 ], scale [ 1 ], scale [ 2 ], scale [ 3 ], dt = LOGO_APPEAR_TIME )
        sprite.rot   = bezier3 ( rot   [ 0 ], rot   [ 1 ], rot   [ 2 ], rot   [ 3 ], dt = LOGO_APPEAR_TIME )

        wait ( LOGO_APPEAR_TIME )

        sprite.scale = 1
        sprite.rot   = ease_in ( LOGO_FLOAT_ROTATION, -LOGO_FLOAT_ROTATION, dt = LOGO_FLOAT_PERIOD, extend = 'extrapolate' )

        event_logo_shown ()

        wait_missed ( event_hide_menu )

        scale = LOGO_HIDE_SCALE
        rot = [ rot * LOGO_ROTATION_PERIODS * 360.0 for rot in LOGO_HIDE_ROTATION ]
        rot [ 0 ] = sprite.rot

        sprite.scale = bezier3 ( scale [ 0 ], scale [ 1 ], scale [ 2 ], scale [ 3 ], dt = LOGO_HIDE_TIME )
        sprite.rot   = bezier3 ( rot   [ 0 ], rot   [ 1 ], rot   [ 2 ], rot   [ 3 ], dt = LOGO_HIDE_TIME )

        wait ( LOGO_HIDE_TIME )

        sprite.kill ()
        event_logo_hidden ()

    def async_work_button ( texture, number, event_clicked, event_click_handled, event_hidden, event_shown ) :
        return gbutton.async_work ( texture, number, BUTTON_NUMBER_OFFSET, buttons_context
                                  , event_hide_menu, event_hidden
                                  , event_show_menu, event_shown
                                  , event_clicked, event_click_handled )

    def hide_menu () :
        skip_missed ( event_exit_hidden )
        skip_missed ( event_logo_hidden )
        event_hide_menu ()
        wait_missed ( event_exit_hidden )
        wait_missed ( event_logo_hidden )

    def show_menu () :
        skip_missed ( event_exit_shown )
        skip_missed ( event_logo_shown )
        event_show_menu ()
        wait_missed ( event_exit_shown )
        wait_missed ( event_logo_shown )

    @start_async
    def async_click_exit () :
        while work_async () :
            wait ( event_exit_clicked )
            hide_menu ()
            event_exit ()
            event_exit_click_handled ()

    # EVENTS

    event_exit                  = Event ()

    event_hide_menu             = Event ()
    event_logo_hidden           = Event ()
    event_exit_hidden           = Event ()

    event_show_menu             = Event ()
    event_logo_shown            = Event ()
    event_exit_shown            = Event ()

    event_exit_clicked          = Event ()

    event_exit_click_handled    = Event ()

    # TASKS

    buttons_context = gbutton.Context ()

    texit = async_work_button ( BUTTON_EXIT_TEXTURE, 0
                , event_exit_clicked
                , event_exit_click_handled
                , event_exit_hidden
                , event_exit_shown )

    tclick_exit = async_click_exit ()

    tlogo = async_work_logo ()

    # WORK

    show_menu ()

    wait ( event_exit )

    # CLEAN-UP

    stop ( tlogo )
    stop ( tclick_exit )
    stop ( texit )

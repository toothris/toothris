# -*- coding: utf-8 -*-

# BASE
from bapi import *

# GAME
import gbutton

# CONSTS

BUTTON_OPTIONS_TEXTURE  = "res/ui_menu/256x064_options.png"
BUTTON_EXIT_TEXTURE     = "res/ui_menu/256x064_exit.png"
BUTTON_NUMBER_OFFSET    = 0.5


def prefetch () :
    gbutton.prefetch_buttons ( BUTTON_OPTIONS_TEXTURE , 1 )
    gbutton.prefetch_buttons ( BUTTON_EXIT_TEXTURE    , 1 )


def show () :

    def async_work_button ( texture, number, event_clicked, event_click_handled, event_hidden, event_shown ) :
        return gbutton.async_work ( texture, number, BUTTON_NUMBER_OFFSET, buttons_context
                                  , event_hide_menu, event_hidden
                                  , event_show_menu, event_shown
                                  , event_clicked, event_click_handled )

    def hide_menu () :
        skip_missed ( event_options_hidden )
        skip_missed ( event_exit_hidden )
        event_hide_menu ()
        wait_missed ( event_options_hidden )
        wait_missed ( event_exit_hidden )

    def show_menu () :
        skip_missed ( event_options_shown )
        skip_missed ( event_exit_shown )
        event_show_menu ()
        wait_missed ( event_options_shown )
        wait_missed ( event_exit_shown )

    @start_async
    def async_click_options () :
        while work_async () :
            wait ( event_options_clicked )
            event_options_click_handled ()

    @start_async
    def async_click_exit () :
        while work_async () :
            wait ( event_exit_clicked )
            hide_menu ()
            event_exit ()
            event_exit_click_handled ()

    # EVENTS

    event_exit                      = Event ()

    event_hide_menu                 = Event ()
    event_options_hidden            = Event ()
    event_exit_hidden               = Event ()

    event_show_menu                 = Event ()
    event_options_shown             = Event ()
    event_exit_shown                = Event ()

    event_options_clicked           = Event ()
    event_exit_clicked              = Event ()

    event_options_click_handled     = Event ()
    event_exit_click_handled        = Event ()

    # TASKS

    buttons_context = gbutton.Context ()

    toptions = async_work_button ( BUTTON_OPTIONS_TEXTURE , 0
                    , event_options_clicked
                    , event_options_click_handled
                    , event_options_hidden
                    , event_options_shown )
    texit    = async_work_button ( BUTTON_EXIT_TEXTURE    , 1
                    , event_exit_clicked
                    , event_exit_click_handled
                    , event_exit_hidden
                    , event_exit_shown )

    tclick_options  = async_click_options ()
    tclick_exit     = async_click_exit ()

    # WORK

    show_menu ()

    wait ( event_exit )

    # CLEAN-UP

    stop ( tclick_options )
    stop ( tclick_exit )

    stop ( toptions )
    stop ( texit )

# -*- coding: utf-8 -*-

# BASE
from bapi import *

# GAME
import gabout
import gbackground
import gbutton
import ggame
import goptions
import gstars

# CONSTS

STARS_COUNT             = 50

BUTTON_NEW_GAME_TEXTURE = "res/ui_menu/256x064_new_game.png"
BUTTON_OPTIONS_TEXTURE  = "res/ui_menu/256x064_options.png"
BUTTON_ABOUT_TEXTURE    = "res/ui_menu/256x064_about.png"
BUTTON_EXIT_TEXTURE     = "res/ui_menu/256x064_quit.png"
BUTTON_NUMBER_OFFSET    = 1.5
BUTTONS_APPEAR_DELAY    = 1.5


def prefetch () :
    gbutton.prefetch_buttons ( BUTTON_NEW_GAME_TEXTURE , 1 )
    gbutton.prefetch_buttons ( BUTTON_OPTIONS_TEXTURE  , 1 )
    gbutton.prefetch_buttons ( BUTTON_ABOUT_TEXTURE    , 1 )
    gbutton.prefetch_buttons ( BUTTON_EXIT_TEXTURE     , 1 )


def show () :

    def async_work_button ( texture, number, event_clicked, event_click_handled, event_hidden, event_shown ) :
        return gbutton.async_work ( texture, number, BUTTON_NUMBER_OFFSET, buttons_context
                                  , event_hide_menu, event_hidden
                                  , event_show_menu, event_shown
                                  , event_clicked, event_click_handled )

    def hide_menu () :
        skip_missed ( event_new_game_hidden )
        skip_missed ( event_options_hidden  )
        skip_missed ( event_about_hidden    )
        skip_missed ( event_exit_hidden     )
        event_hide_menu ()
        wait_missed ( event_exit_hidden     )
        wait_missed ( event_about_hidden    )
        wait_missed ( event_options_hidden  )
        wait_missed ( event_new_game_hidden )

    def show_menu () :
        skip_missed ( event_new_game_shown )
        skip_missed ( event_options_shown  )
        skip_missed ( event_about_shown    )
        skip_missed ( event_exit_shown     )
        event_show_menu ()
        wait_missed ( event_exit_shown     )
        wait_missed ( event_about_shown    )
        wait_missed ( event_options_shown  )
        wait_missed ( event_new_game_shown )

    @start_async
    def async_click_new_game () :
        while work_async () :
            wait ( event_new_game_clicked )
            hide_menu ()
            ggame.show ()
            show_menu ()
            event_new_game_click_handled ()

    @start_async
    def async_click_options () :
        while work_async () :
            wait ( event_options_clicked )
            hide_menu ()
            goptions.show ()
            show_menu ()
            event_options_click_handled ()

    @start_async
    def async_click_about () :
        while work_async () :
            wait ( event_about_clicked )
            hide_menu ()
            gabout.show  ()
            show_menu ()
            event_about_click_handled ()

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
    event_new_game_hidden           = Event ()
    event_options_hidden            = Event ()
    event_about_hidden              = Event ()
    event_exit_hidden               = Event ()

    event_show_menu                 = Event ()
    event_new_game_shown            = Event ()
    event_options_shown             = Event ()
    event_about_shown               = Event ()
    event_exit_shown                = Event ()

    event_new_game_clicked          = Event ()
    event_options_clicked           = Event ()
    event_about_clicked             = Event ()
    event_exit_clicked              = Event ()

    event_new_game_click_handled    = Event ()
    event_options_click_handled     = Event ()
    event_about_click_handled       = Event ()
    event_exit_click_handled        = Event ()

    # TASKS

    tback  = gbackground.async_show ()
    tstars = gstars.async_show      ()

    buttons_context = gbutton.Context ()

    tnew_game   = async_work_button ( BUTTON_NEW_GAME_TEXTURE   , 0
                    , event_new_game_clicked
                    , event_new_game_click_handled
                    , event_new_game_hidden
                    , event_new_game_shown )
    toptions    = async_work_button ( BUTTON_OPTIONS_TEXTURE    , 1
                    , event_options_clicked
                    , event_options_click_handled
                    , event_options_hidden
                    , event_options_shown )
    tabout      = async_work_button ( BUTTON_ABOUT_TEXTURE      , 2
                    , event_about_clicked
                    , event_about_click_handled
                    , event_about_hidden
                    , event_about_shown )
    texit       = async_work_button ( BUTTON_EXIT_TEXTURE       , 3
                    , event_exit_clicked
                    , event_exit_click_handled
                    , event_exit_hidden
                    , event_exit_shown )

    tclick_new_game = async_click_new_game  ()
    tclick_options  = async_click_options   ()
    tclick_about    = async_click_about     ()
    tclick_exit     = async_click_exit      ()

    # WORK

    wait ( BUTTONS_APPEAR_DELAY )
    show_menu ()

    wait ( event_exit )

    # CLEAN-UP

    stop ( tnew_game )
    stop ( toptions )
    stop ( tabout )
    stop ( texit )

    stop ( tclick_new_game )
    stop ( tclick_options )
    stop ( tclick_about )
    stop ( tclick_exit )

    stop ( tstars )
    stop ( tback )

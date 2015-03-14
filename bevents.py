# -*- coding: cp1251 -*-

# LIBS
import pickle
import pygame
import random
import sys
import time

# BASE
import bconf
import btasks


# CONSTS

# PYGAME INTERNAL CODES
MOUSE_BUTTON_LEFT       = 1
MOUSE_BUTTON_MIDDLE     = 2
MOUSE_BUTTON_RIGHT      = 3
MOUSE_WHEEL_UP          = 4
MOUSE_WHEEL_DOWN        = 5
KEY_UP                  = 273
KEY_DOWN                = 274
KEY_LEFT                = 276
KEY_RIGHT               = 275
KEY_ESC                 = 27

# EVENTS LOGGING
EVENTS_FILE_NAME        = "events.log"


# VIRTUAL KEYS

class VirtualKey :
    def __init__ ( self ) :
        self.push       = btasks.Event ()
        self.pop        = btasks.Event ()


key_click               = VirtualKey ()
key_up                  = VirtualKey ()
key_down                = VirtualKey ()
key_left                = VirtualKey ()
key_right               = VirtualKey ()
key_back                = VirtualKey ()

# HARDWARE MAPPING

mouse_mapping           = \
{   MOUSE_BUTTON_LEFT   : key_click
}

keyboard_mapping        = \
{   KEY_LEFT            : key_left
,   KEY_RIGHT           : key_right
,   KEY_UP              : key_up
,   KEY_DOWN            : key_down
,   KEY_ESC             : key_back
}

# DEMO EVENTS

frame_tag               = 0

events_recorded         = {}
events_to_play          = {}

mouse_pos_recorded      = {}
mouse_pos_to_play       = {}

mouse_pos_prev          = ( 10000, 10000 )
mouse_pos               = ( 10000, 10000 )

random_seed             = time.time ()

class DemoEvent () :
    def __init__ ( self, pygame_event ) :
        self.type   = pygame_event.type
        if hasattr ( pygame_event, "key" ) :
            self.key    = pygame_event.key
        if hasattr ( pygame_event, "button" ) :
            self.button = pygame_event.button

# INIT

def init () :
    global events_to_play
    global mouse_pos_to_play
    global random_seed

    if bconf.EVENTS_PLAY :
        f = open ( EVENTS_FILE_NAME, "rb" )
        random_seed         = pickle.load ( f )
        events_to_play      = pickle.load ( f )
        mouse_pos_to_play   = pickle.load ( f )
        f.close ()

    random.seed ( random_seed )

# DONE

def done () :
    if bconf.EVENTS_RECORD :
        f = open ( EVENTS_FILE_NAME, "wb" )
        pickle.dump ( random_seed        , f )
        pickle.dump ( events_recorded    , f )
        pickle.dump ( mouse_pos_recorded , f )
        f.close ()

# HANDLER

def handle () :

    global frame_tag
    global mouse_pos
    global mouse_pos_prev

    # NEXT FRAME

    frame_tag += 1

    # OBTAIN MOUSE POS

    if bconf.EVENTS_PLAY :
        if frame_tag in mouse_pos_to_play :
            mouse_pos = mouse_pos_to_play [ frame_tag ]
    else :
        mouse_pos = pygame.mouse.get_pos ()

    # RECORD MOUSE POS

    if bconf.EVENTS_RECORD :
        if mouse_pos [ 0 ] != mouse_pos_prev [ 0 ] \
        or mouse_pos [ 1 ] != mouse_pos_prev [ 1 ] :
            mouse_pos_recorded [ frame_tag ] = mouse_pos
            mouse_pos_prev = mouse_pos

    # OBTAIN EVENTS QUEUE

    events = []
    if bconf.EVENTS_PLAY :
        if frame_tag in events_to_play :
            events = events_to_play [ frame_tag ]
        for event in pygame.event.get () :
            if event.type == pygame.QUIT :
                return False
    else :
        events = pygame.event.get ()

    # RECORD EVENTS QUEUE

    if bconf.EVENTS_RECORD and len ( events ) > 0 :
        events_recorded [ frame_tag ] = [ DemoEvent ( event ) for event in events ]

    # HANDLE EVENTS QUEUE

    for event in events :

        if event.type == pygame.QUIT :
            return False

        if event.type == pygame.KEYUP :
            if event.key in keyboard_mapping :
                keyboard_mapping [ event.key ].pop ()

        if event.type == pygame.KEYDOWN :
            if event.key in keyboard_mapping :
                keyboard_mapping [ event.key ].push ()

        if event.type == pygame.MOUSEBUTTONUP :
            if event.button in mouse_mapping :
                mouse_mapping [ event.button ].pop ()

        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button in mouse_mapping :
                mouse_mapping [ event.button ].push ()

    return True

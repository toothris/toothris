# -*- coding: cp1251 -*-

# LIBS
import collections
import math
import pygame
import rabbyt
import random

# BASE
import bevents
import brender
import bsprites
import btasks

#
# MINIMAL MEAN VALUE
#

TOLERANCE = 0.01

#
# COLLECTIONS ALIASES
#

def queue ( l ) :
    return collections.deque ( l )

#
# MATH ALIASES
#

def floor ( f ) :
    return int ( math.floor ( f ) )

def ceil ( f ) :
    return int ( math.ceil ( f ) )

def sin ( degrees ) :
    return math.sin ( math.radians ( degrees ) )

def cos ( degrees ) :
    return math.cos ( math.radians ( degrees ) )

#
# PYGAME ALIASES
#

def mouse_pos () :
    return brender.screen_to_world ( bevents.mouse_pos )

#
# RABBYT ALIASES
#

def bezier3 ( p0, p1, p2, p3, ** kws ) :
    if kws [ 'dt' ] > TOLERANCE :
        return rabbyt.bezier3 ( p0, p1, p2, p3, ** kws )
    else :
        return p3

def lerp ( start = None, end = None, ** kws ) :
    assert end != None
    if kws [ 'dt' ] > TOLERANCE :
        if start == None :
            return rabbyt.lerp ( end = end, ** kws )
        else :
            return rabbyt.lerp ( start, end, ** kws )
    else :
        return end

def ease_out ( start = None, end = None, ** kws ) :
    assert end != None
    if kws [ 'dt' ] > TOLERANCE :
        if start == None :
            return rabbyt.ease_out ( end = end, ** kws )
        else :
            return rabbyt.ease_out ( start, end, ** kws )
    else :
        return end

def ease_in ( start = None, end = None, ** kws ) :
    assert end != None
    if kws [ 'dt' ] > TOLERANCE :
        if start == None :
            return rabbyt.ease_in ( end = end, ** kws )
        else :
            return rabbyt.ease_in ( start, end, ** kws )
    else :
        return end

def ease ( start = None, end = None, ** kws ) :
    assert end != None
    if kws [ 'dt' ] > TOLERANCE :
        if start == None :
            return rabbyt.ease ( end = end, ** kws )
        else :
            return rabbyt.ease ( start, end, ** kws )
    else :
        return end

#
# RANDOM ALIASES
#

def rand ( * args ) :
    if len ( args ) == 2 :
        return random.uniform ( args [ 0 ], args [ 1 ] )
    elif len ( args ) == 1 :
        return random.choice ( args [ 0 ] )
    else :
        raise RuntimeError ( "rand args error" )

#
# EVENTS ALIASES
#

key_up      = bevents.key_up
key_down    = bevents.key_down
key_left    = bevents.key_left
key_right   = bevents.key_right
key_back    = bevents.key_back

#
# RENDER ALIASES
#

screen_width  = brender.width
screen_height = brender.height

#
# SPRITES ALIASES
#

def layer ( index ) :
    return bsprites.layer ( index )

def prefetch_all () :
    bsprites.prefetch ()

def unfetch_all () :
    bsprites.unfetch ()

#
# TASKS ALIASES
#

Event = btasks.Event

priority_realtime   = btasks.priority_realtime
priority_high       = btasks.priority_high
priority_medium     = btasks.priority_medium
priority_low        = btasks.priority_low

PRIORITY_DEFAULT    = priority_low

def current_task () :
    return btasks.current_task ()

def wait_missed ( event ) :
    btasks.wait_missed ( event )

def wait ( arg ) :
    if isinstance ( arg, type ( TOLERANCE ) ) and arg < TOLERANCE :
        return
    btasks.wait ( arg )

def skip_missed ( event ) :
    btasks.skip_missed ( event )

def start_async ( f ) :
    return btasks.start_async ( f )

def stop ( task ) :
    btasks.stop ( task )

def working ( task ) :
    return btasks.working ( task )

def work_async () :
    return btasks.work_async ()

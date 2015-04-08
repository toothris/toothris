# Copyright 2008, 2015 Oleg Plakhotniuk
#
# This file is part of Toothris.
#
# Toothris is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Toothris is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Toothris.  If not, see <http://www.gnu.org/licenses/>.

# BASE
from bapi import *

# GAME
import gfigures
import glayers

# CONSTS

ACTIONS_MAX_COUNT_PER_TYPE      = 20
ACTIONS_MAX_HIGHLIGHTS_PER_TYPE = 20
ACTION_HALF_SIZE                = 0.07 * screen_height
ACTION_LIVE_SCALE_MIN           = 0.9
ACTION_LIVE_SCALE_MAX           = 1.1
ACTION_LIVE_SCALE_PERIOD        = 1
ACTION_APPEAR_SCALE             = [ 0, 0.5, 2, 1 ]
ACTION_APPEAR_TIME              = 0.5
ACTION_APPEAR_DELAY             = 0.05
ACTION_DISAPPEAR_SCALE          = [ 1, 2, 0.5, 0 ]
ACTION_DISAPPEAR_TIME           = 0.5
ACTION_DISAPPEAR_DELAY          = 0.05
ACTION_RESET_ALPHA              = 0.3
ACTION_RESET_RADIUS             = [ 0.0, 0.2, 1.2, 1 ]
ACTION_RESET_SCALE              = [ 1.0, 3.0, 2.0, 0 ]
ACTION_RESET_TIME               = 0.5
ACTION_RESET_DELAY              = 0.05
ACTION_HANDLE_RADIUS            = [ 0.0, 0.2, 1.2, 1 ]
ACTION_HANDLE_SCALE             = [ 0.0, 5.0, 1.5, 1 ]
ACTION_HANDLE_TIME              = 0.7
ACTION_HANDLE_DELAY             = 0
ACTION_DROP                     = "drop"
ACTION_FLOAT                    = "float"
ACTION_FRAG                     = "frag"
ACTION_GROUND                   = "ground"
ACTION_HIT                      = "hit"
ACTION_ROTATE                   = "rotate"
ACTION_SWALLOW                  = "swallow"
ACTIONS_TEXTURES                = \
{   ACTION_DROP                 : "res/game/128x128_event_drop.png"
,   ACTION_FLOAT                : "res/game/128x128_event_float.png"
,   ACTION_FRAG                 : "res/game/128x128_event_frag.png"
,   ACTION_GROUND               : "res/game/128x128_event_ground.png"
,   ACTION_HIT                  : "res/game/128x128_event_hit.png"
,   ACTION_ROTATE               : "res/game/128x128_event_rotate.png"
,   ACTION_SWALLOW              : "res/game/128x128_event_swallow.png"
}

FIGURES_MAX_COUNT_PER_TYPE      = 20
FIGURES_MAX_HIGHLIGHTS_PER_TYPE = 20
FIGURE_HALF_SIZE                = 0.05 * screen_height

# ALIASES

actions_layer                   = layer ( glayers.ACTIONS )
figures_layer                   = layer ( glayers.ACTIONS_FIGURES )
highlights_actions_layer        = layer ( glayers.ACTIONS_HIGHLIGHTS )
highlights_figures_layer        = layer ( glayers.ACTIONS_HIGHLIGHTS_FIGURES )

# VARIABLES

ttasks                          = []

# PREFETCH

def prefetch () :
    for texture in ACTIONS_TEXTURES.values () :
        actions_layer.prefetch_sprites            ( texture, ACTIONS_MAX_COUNT_PER_TYPE )
        highlights_actions_layer.prefetch_sprites ( texture, ACTIONS_MAX_HIGHLIGHTS_PER_TYPE )
    for figure in gfigures.figures.values () :
        figures_layer.prefetch_sprites            ( figure.texture, FIGURES_MAX_COUNT_PER_TYPE )
        highlights_figures_layer.prefetch_sprites ( figure.texture, FIGURES_MAX_HIGHLIGHTS_PER_TYPE )

# ACTIONS

def new_action_sprites ( actions_layer, figures_layer, action_type, figure ) :
        action_sprite          = actions_layer.new_sprite ( ACTIONS_TEXTURES [ action_type ] )
        action_sprite.shape    = [ -ACTION_HALF_SIZE, ACTION_HALF_SIZE, ACTION_HALF_SIZE, -ACTION_HALF_SIZE ]

        figure_sprite          = figures_layer.new_sprite ( figure.texture )
        figure_sprite.shape    = [ -FIGURE_HALF_SIZE, FIGURE_HALF_SIZE, FIGURE_HALF_SIZE, -FIGURE_HALF_SIZE ]
        figure_sprite.x        = lambda : action_sprite.x + figure.center_x * FIGURE_HALF_SIZE * 2
        figure_sprite.y        = lambda : action_sprite.y + figure.center_y * FIGURE_HALF_SIZE * 2
        figure_sprite.scale    = lambda : action_sprite.scale
        figure_sprite.alpha    = lambda : action_sprite.alpha

        return action_sprite, figure_sprite


class Action :
    def __init__ ( self, action_type, figure, x, y ) :
        self.action_type            = action_type
        self.figure_type            = figure.type
        self.is_handled             = False

        self.action_sprite, self.figure_sprite = new_action_sprites ( actions_layer, figures_layer, action_type, figure )

        self.action_sprite.x        = x
        self.action_sprite.y        = y
        self.action_sprite.scale    = 0
        self.action_sprite.alpha    = ACTION_RESET_ALPHA


    def __del__ ( self ) :
        self.figure_sprite.kill ()
        self.action_sprite.kill ()


def handle_action ( actions, action_type, figure, xfrom, yfrom ) :

    @start_async
    def async_handle ( action, xfrom, yfrom ) :
        highlight_action_sprite, highlight_figure_sprite = new_action_sprites ( highlights_actions_layer, highlights_figures_layer, action.action_type, gfigures.figures [ action.figure_type ] )

        x                               = [ ( 1 - x ) * xfrom + x * action.action_sprite.x for x in ACTION_HANDLE_RADIUS ]
        y                               = [ ( 1 - y ) * yfrom + y * action.action_sprite.y for y in ACTION_HANDLE_RADIUS ]
        s                               = ACTION_HANDLE_SCALE
        action.is_handled               = True

        highlight_action_sprite.x       = bezier3 ( x [ 0 ], x [ 1 ], x [ 2 ], x [ 3 ], dt = ACTION_HANDLE_TIME )
        highlight_action_sprite.y       = bezier3 ( y [ 0 ], y [ 1 ], y [ 2 ], y [ 3 ], dt = ACTION_HANDLE_TIME )
        highlight_action_sprite.scale   = bezier3 ( s [ 0 ], s [ 1 ], s [ 2 ], s [ 3 ], dt = ACTION_HANDLE_TIME )
        wait ( ACTION_HANDLE_TIME )

        if action.bonus :
            action.bonus.activation_update ()

        action.action_sprite.alpha      = 1

        highlight_figure_sprite.kill ()
        highlight_action_sprite.kill ()


    for action in actions :
        if action.action_type == action_type and action.figure_type == figure.type and not action.is_handled :
            ttasks.append ( async_handle ( action, xfrom, yfrom ) )
            wait ( ACTION_HANDLE_DELAY )
            return


def reset_action ( actions, xto, yto ) :

    @start_async
    def async_reset ( action ) :
        highlight_action_sprite, highlight_figure_sprite = new_action_sprites ( highlights_actions_layer, highlights_figures_layer, action.action_type, gfigures.figures [ action.figure_type ] )

        x                               = [ ( 1 - x ) * action.action_sprite.x + x * xto for x in ACTION_RESET_RADIUS ]
        y                               = [ ( 1 - y ) * action.action_sprite.y + y * yto for y in ACTION_RESET_RADIUS ]
        s                               = ACTION_RESET_SCALE
        action.is_handled               = False

        highlight_action_sprite.x       = bezier3 ( x [ 0 ], x [ 1 ], x [ 2 ], x [ 3 ], dt = ACTION_RESET_TIME )
        highlight_action_sprite.y       = bezier3 ( y [ 0 ], y [ 1 ], y [ 2 ], y [ 3 ], dt = ACTION_RESET_TIME )
        highlight_action_sprite.scale   = bezier3 ( s [ 0 ], s [ 1 ], s [ 2 ], s [ 3 ], dt = ACTION_RESET_TIME )

        action.action_sprite.alpha      = ACTION_RESET_ALPHA

        wait ( ACTION_RESET_TIME )

        highlight_figure_sprite.kill ()
        highlight_action_sprite.kill ()

    tactions = []
    for action in actions :
        if action.is_handled :
            tactions.append ( async_reset ( action ) )
            wait ( ACTION_RESET_DELAY )
    for taction in tactions :
        wait ( taction )
    tactions = None


def are_done ( actions ) :
    for action in actions :
        if not action.is_handled :
            return False
    return True


def wait_async_tasks () :
    global ttasks
    for ttask in ttasks :
        wait ( ttask )
    ttasks = []


@start_async
def async_show ( actions ) :

    @start_async
    def async_do_show ( action ) :
        s                           = [ s for s in ACTION_APPEAR_SCALE ]
        s [ 3 ]                     = ACTION_LIVE_SCALE_MIN
        action.action_sprite.scale  = bezier3 ( s [ 0 ], s [ 1 ], s [ 2 ], s [ 3 ], dt = ACTION_APPEAR_TIME )
        wait ( ACTION_APPEAR_TIME )
        action.action_sprite.scale  = ease ( ACTION_LIVE_SCALE_MIN, ACTION_LIVE_SCALE_MAX, dt = ACTION_LIVE_SCALE_PERIOD, extend = 'extrapolate' )


    tactions = []
    for action in actions :
        tactions.append ( async_do_show ( action ) )
        wait ( ACTION_APPEAR_DELAY )
    for taction in tactions :
        wait ( taction )
    tactions = None


@start_async
def async_hide ( actions ) :

    @start_async
    def async_do_hide ( action ) :
        s                               = [ s for s in ACTION_DISAPPEAR_SCALE ]
        s [ 0 ]                         = action.action_sprite.scale
        action.action_sprite.scale      = bezier3 ( s [ 0 ], s [ 1 ], s [ 2 ], s [ 3 ], dt = ACTION_DISAPPEAR_TIME )
        wait ( ACTION_DISAPPEAR_TIME )


    tactions = []
    for action in actions :
        tactions.append ( async_do_hide ( action ) )
        wait ( ACTION_DISAPPEAR_DELAY )
    for taction in tactions :
        wait ( taction )
    tactions = None

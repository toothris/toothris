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
import glayers

# CONSTS

BUTTONS_MAX_COUNT           = 10

BUTTON_SIZE_X               = 0.5   * screen_height
BUTTON_SIZE_Y               = 0.125 * screen_height
BUTTON_SPACING              = 0.1   * screen_height
BUTTON_APPEAR_DELAY         = 0.1
BUTTON_APPEAR_TIME          = 0.5
BUTTON_X_AMPLITUDE          = 0.05  * screen_width
BUTTON_FLOAT_PERIOD         = 3
BUTTON_FOCUS_SCALE          = 0.9
BUTTON_FOCUS_PERIOD         = 0.3
BUTTON_CLICK_FADE_TIME      = 0.3

SELECTION_TEXTURES  = \
[ "res/ui_menu/256x064_selected1.png"
, "res/ui_menu/256x064_selected2.png"
, "res/ui_menu/256x064_selected3.png"
, "res/ui_menu/256x064_selected4.png"
]
SELECTION_ROT_AMP           = 2
SELECTION_ROT_PERIOD        = 0.2
SELECTION_MORPH_TIME        = 0.5


# ALIASES

buttons_layer   = layer ( glayers.BUTTONS           )
selection_layer = layer ( glayers.BUTTONS_SELECTION )


def prefetch () :
    for texture in SELECTION_TEXTURES :
        selection_layer.prefetch_sprites ( texture, BUTTONS_MAX_COUNT )


def prefetch_buttons ( texture, count ) :
    buttons_layer.prefetch_sprites ( texture, count )


class Context :
    def __init__ ( self ) :
        self.button_blocked = False


@start_async
def async_work ( button_texture, number, number_offset, context
               , event_hide_button, event_button_hidden
               , event_show_button, event_button_shown
               , event_button_clicked, event_click_handled ) :

    shape = [ - BUTTON_SIZE_X, BUTTON_SIZE_Y, BUTTON_SIZE_X, - BUTTON_SIZE_Y ]

    sprites_selection = queue ( [ selection_layer.new_sprite ( texture ) for texture in SELECTION_TEXTURES ] )

    sprite_button = buttons_layer.new_sprite ( button_texture )
    sprite_button.shape = shape

    for sprite in sprites_selection :
        sprite.shape = shape
        sprite.alpha = 0
        sprite.x = lambda : sprite_button.x
        sprite.y = lambda : sprite_button.y
        sprite.rot = ease_out ( -SELECTION_ROT_AMP, SELECTION_ROT_AMP, dt = SELECTION_ROT_PERIOD, extend = 'extrapolate' )

    x0 = -screen_width - BUTTON_SIZE_X
    x1 = -2 * BUTTON_X_AMPLITUDE
    x2 = -BUTTON_X_AMPLITUDE
    x3 = 0
    x4 = BUTTON_X_AMPLITUDE
    x5 = 2 * BUTTON_X_AMPLITUDE

    center_x = 0
    center_y = ( number_offset - number ) * ( 2.0 * BUTTON_SIZE_Y + BUTTON_SPACING )

    focus_left   = center_x - BUTTON_SIZE_X
    focus_right  = center_x + BUTTON_SIZE_X
    focus_top    = center_y + BUTTON_SIZE_Y + 0.49 * BUTTON_SPACING
    focus_bottom = center_y - BUTTON_SIZE_Y - 0.50 * BUTTON_SPACING

    sprite_button.x = -screen_width - BUTTON_SIZE_X
    sprite_button.y = center_y

    @start_async
    def async_show_button () :


        @start_async
        def async_float () :
            while work_async () :
                sprite_button.x = bezier3 ( x4, x1, x3, x2, dt = 0.5 * BUTTON_FLOAT_PERIOD )
                wait ( 0.5 * BUTTON_FLOAT_PERIOD )
                sprite_button.x = bezier3 ( x2, x5, x3, x4, dt = 0.5 * BUTTON_FLOAT_PERIOD )
                wait ( 0.5 * BUTTON_FLOAT_PERIOD )


        def isfocused () :
            mouse_x, mouse_y = mouse_pos ()
            return  focus_left   < mouse_x \
               and  focus_right  > mouse_x \
               and  focus_top    > mouse_y \
               and  focus_bottom < mouse_y


        def button_fade ( scale = 1, time_scale = 0.5 * BUTTON_FLOAT_PERIOD, alpha = 0, time_alpha = SELECTION_MORPH_TIME ) :
            max_time = 0

            time = abs ( sprite_button.scale - scale ) * time_scale
            max_time = max ( time, max_time )
            sprite_button.scale = ease_out ( sprite_button.scale, scale, dt = time )

            for sprite in sprites_selection :
                time = abs ( sprite.alpha ) * time_alpha
                max_time = max ( time, max_time )
                sprite.alpha = ease_out ( sprite.alpha, alpha, dt = time )

            wait ( max_time )


        @start_async
        def async_focus_got () :
            button_fade ( scale = 1 )
            sprite_button.scale = ease_out ( 1, BUTTON_FOCUS_SCALE, dt = BUTTON_FOCUS_PERIOD, extend = 'extrapolate' )
            wait ( SELECTION_MORPH_TIME )
            sprites_selection [ 0 ].alpha = ease_out ( 0, 1, dt = SELECTION_MORPH_TIME )
            wait ( SELECTION_MORPH_TIME )
            while work_async () :
                sprites_selection [ 0 ].alpha = ease_out ( 1, 0, dt = SELECTION_MORPH_TIME )
                sprites_selection [ 1 ].alpha = ease_out ( 0, 1, dt = SELECTION_MORPH_TIME )
                wait ( SELECTION_MORPH_TIME )
                sprites_selection.rotate ( -1 )


        @start_async
        def async_focus_lost () :
            button_fade ( scale = 1 )


        @start_async
        def async_catch_clicks () :
            while work_async () :
                wait ( buttons_layer.key_click.push )
                if isfocused () and not context.button_blocked :
                    buttons_layer.handled_key_click.push ()
                    context.button_blocked = True
                    stop ( tfocus_got )
                    stop ( tfocus_lost )
                    button_fade ( scale = 0,  time_scale = BUTTON_CLICK_FADE_TIME )

                    skip_missed ( event_click_handled )
                    event_button_clicked ()
                    wait_missed ( event_click_handled )

                    button_fade ( scale = 1 )
                    context.button_blocked = False


        tfloat      = async_float ()
        tclick      = async_catch_clicks ()
        tfocus_lost = None
        tfocus_got  = None

        try :
            while work_async () :

                if not context.button_blocked :

                    if not isfocused () and not working ( tfocus_lost ) :
                        stop ( tfocus_got )
                        tfocus_lost = async_focus_lost ()

                    if isfocused () and not working ( tfocus_got ) :
                        stop ( tfocus_lost )
                        tfocus_got = async_focus_got ()

        finally :
            stop ( tfocus_got )
            stop ( tfocus_lost )
            stop ( tclick )
            stop ( tfloat )


    try:
        tshow = None
        thide = None
        while work_async () :
            wait_missed ( event_show_button )

            wait ( number * BUTTON_APPEAR_DELAY )
            sprite_button.x = bezier3 ( x0, x1, x3, x4, dt = BUTTON_APPEAR_TIME )
            wait ( BUTTON_APPEAR_TIME )
            tshow = async_show_button ()

            event_button_shown ()

            wait_missed ( event_hide_button )

            wait ( number * BUTTON_APPEAR_DELAY )
            stop ( tshow )

            sprite_button.x = bezier3 ( sprite_button.x, x3, x1, x0, dt = BUTTON_APPEAR_TIME )
            wait ( BUTTON_APPEAR_TIME )
            sprite_button.x = -screen_width - BUTTON_SIZE_X
            sprite_button.y = center_y
            sprite_button.scale = 1

            event_button_hidden ()
            context.button_blocked = False

    finally :
        stop ( tshow )
        stop ( thide )
        sprite_button.kill ()
        for sprite in sprites_selection :
            sprite.kill ()

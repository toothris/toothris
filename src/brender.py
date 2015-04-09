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

# LIBS
import pygame
import rabbyt

# BASE
from bconf import BCONF
import bprofile
import bsprites
import btasks

#
# X         - RIGHT
# Y         - UP
# CENTER    - 0,0
# SIZE      - -width...width, height...-height
#

REPORT_FRAMES = 100

# GLOBALS
aspect  = float ( BCONF.width ) / float ( BCONF.height )
width   = 4.0
height  = 3.0
window  = None


def screen_to_world ( xy ) :
    return  ( 2 * width  * ( ( float ( xy [ 0 ] ) / BCONF.width  ) - 0.5 )
            ,-2 * height * ( ( float ( xy [ 1 ] ) / BCONF.height ) - 0.5 ) )


def world_to_screen ( xy ) :
    return  ( ( float ( xy [ 0 ] ) + width  ) * 0.5 * BCONF.width
            , ( float (-xy [ 1 ] ) + height ) * 0.5 * BCONF.height )


def init () :
    global window
    flags = pygame.OPENGL | pygame.DOUBLEBUF
    if BCONF.fullscreen :
        flags |= pygame.FULLSCREEN

    pygame.display.init ()
    window = pygame.display.set_mode ( ( BCONF.width, BCONF.height ), flags )
    rabbyt.set_viewport ( ( BCONF.width, BCONF.height ), ( -width, height, width, -height ) )
    rabbyt.set_default_attribs ()


def done () :
    pygame.display.quit ()


@btasks.start_async_realtime
def async_render () :
    frame = 0
    if BCONF.render :
        while btasks.work_async () :
            bprofile.begin ( "render" )
            bsprites.render ()
            pygame.display.flip ()
            if BCONF.frames :
                pygame.image.save(window, BCONF.frames % frame)
                if frame % REPORT_FRAMES == 0 :
                    print 'frame %i' % frame
                frame += 1
            if frame == BCONF.stopframe :
                raise Exception ( 'stop frame reached' )
            bprofile.end ( "render" )

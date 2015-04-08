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

# PREREQUISITES
import bimport
bimport.check ( "pygame" )
bimport.check ( "rabbyt" )
bimport.check ( "OpenGL" )

# LIBS
import gc
import pygame
import rabbyt
import sys

# BASE
from bapi import *
from bconf import BCONF
import bevents
import bmusic
import bprofile
import brender
import bsprites

# GAME
import glogic

gc.disable ()
gc.set_debug ( gc.DEBUG_LEAK )

bevents.init ()
brender.init ()
bmusic.init ()

# START LOGIC
trender     = brender.async_render          ()
tevents     = bsprites.async_catch_events   ()
tlogic      = glogic.async_logic            ()
fps_clock   = pygame.time.Clock             ()

try :
    # MAIN LOOP
    time = 0
    time_step = 1.0 / float ( BCONF.fps )
    while working ( tlogic ) :
        time += time_step
        rabbyt.set_time ( time )
        btasks.run ()
        if not bevents.handle () :
            break
        fps_clock.tick ( BCONF.fps if BCONF.keepfps else 0 )

finally :
    stop ( tlogic  )
    stop ( trender )
    stop ( tevents )

    bevents.done ()
    brender.done ()
    bmusic.done ()

    bprofile.stats ()

    print "target fps   : " + str ( BCONF.fps )
    print "average fps  : " + str ( int ( fps_clock.get_fps () ) )

    assert len ( gc.garbage ) == 0

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

# BASE
from bconf import BCONF


def init () :
    if BCONF.music :
        pygame.mixer.init ()
        pygame.mixer.music.load ( BCONF.music )
        pygame.mixer.music.play ()


def done () :
    if BCONF.music :
        pygame.mixer.quit ()

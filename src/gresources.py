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
import gabout
import gactions
import gbackground
import gbonuses
import gbutton
import ggame
import gkey
import gmenu
import goptions
import gstars


def load () :
    gactions.prefetch     ()
    gabout.prefetch       ()
    gbackground.prefetch  ()
    gbonuses.prefetch     ()
    gbutton.prefetch      ()
    ggame.prefetch        ()
    gkey.prefetch         ()
    gmenu.prefetch        ()
    goptions.prefetch     ()
    gstars.prefetch       ()

    prefetch_all ()

def unload () :
    unfetch_all ()

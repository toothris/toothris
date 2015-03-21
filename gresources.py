# -*- coding: utf-8 -*-

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

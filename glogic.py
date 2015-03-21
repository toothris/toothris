# -*- coding: cp1251 -*-

# BASE
from bapi import *

# GAME
import gintro
import gmenu
import goutro
import gresources


# LOGIC
@start_async
def async_logic () :
    gresources.load ()

    gintro.show     ()
    gmenu.show      ()
    goutro.show     ()

    gresources.unload ()

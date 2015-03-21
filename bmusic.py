# -*- coding: utf-8 -*-

# LIBS
import pygame

# BASE
from bconf import BCONF


def init () :
    pygame.mixer.init ()
    if BCONF.music :
        pygame.mixer.music.load ( BCONF.music )
        pygame.mixer.music.play ()


def done () :
    pygame.mixer.quit ()

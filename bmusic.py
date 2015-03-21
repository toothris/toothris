# -*- coding: utf-8 -*-

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

# -*- coding: utf-8 -*-

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


# GLOBALS
aspect  = float ( BCONF.width ) / float ( BCONF.height )
width   = 4.0
height  = 3.0


def screen_to_world ( xy ) :
    return  ( 2 * width  * ( ( float ( xy [ 0 ] ) / BCONF.width  ) - 0.5 )
            ,-2 * height * ( ( float ( xy [ 1 ] ) / BCONF.height ) - 0.5 ) )


def world_to_screen ( xy ) :
    return  ( ( float ( xy [ 0 ] ) + width  ) * 0.5 * BCONF.width
            , ( float (-xy [ 1 ] ) + height ) * 0.5 * BCONF.height )


def init () :
    flags = pygame.OPENGL | pygame.DOUBLEBUF
    if BCONF.fullscreen :
        flags |= pygame.FULLSCREEN

    pygame.display.init ()
    window = pygame.display.set_mode ( ( BCONF.width, BCONF.height ), flags )
    rabbyt.set_viewport ( ( BCONF.width, BCONF.height ), ( -width, height, width, -height ) )
    rabbyt.set_default_attribs ()


def done () :
    print 'render done'
    pygame.display.quit ()


@btasks.start_async_realtime
def async_render () :
    #count = 0
    if BCONF.render :
        while btasks.work_async () :
            bprofile.begin ( "render" )
            bsprites.render ()
            pygame.display.flip ()
            #TODO
            #pygame.image.save(window, "shot%i.png" % count)
            #count += 1
            bprofile.end ( "render" )

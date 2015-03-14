# -*- coding: cp1251 -*-

# LIBS
import pygame
import rabbyt

# BASE
import bconf
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
aspect  = float ( bconf.WIDTH ) / float ( bconf.HEIGHT )
width   = 4.0
height  = 3.0


def screen_to_world ( xy ) :
    return  ( 2 * width  * ( ( float ( xy [ 0 ] ) / bconf.WIDTH  ) - 0.5 )
            ,-2 * height * ( ( float ( xy [ 1 ] ) / bconf.HEIGHT ) - 0.5 ) )


def world_to_screen ( xy ) :
    return  ( ( float ( xy [ 0 ] ) + width  ) * 0.5 * bconf.WIDTH
            , ( float (-xy [ 1 ] ) + height ) * 0.5 * bconf.HEIGHT )


@btasks.start_async_realtime
def async_render () :
    flags = pygame.OPENGL | pygame.DOUBLEBUF
    if bconf.FULLSCREEN :
        flags |= pygame.FULLSCREEN

    pygame.init ()
    window = pygame.display.set_mode ( ( bconf.WIDTH, bconf.HEIGHT ), flags )
    rabbyt.set_viewport ( ( bconf.WIDTH, bconf.HEIGHT ), ( -width, height, width, -height ) )
    rabbyt.set_default_attribs ()

    #count = 0
    if bconf.RENDER :
        while btasks.work_async () :
            bprofile.begin ( "render" )
            bsprites.render ()
            pygame.display.flip ()
            #TODO
            #pygame.image.save(window, "shot%i.png" % count)
            #count += 1
            bprofile.end ( "render" )

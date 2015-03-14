# -*- coding: cp1251 -*-

# BASE
from bapi import *

# GAME
import gactions
import glayers

# CONSTS

BONUSES_MAX_COUNT_PER_TYPE          = 5
BONUSES_MAX_HIGHLIGHTS_PER_TYPE     = 5
BONUS_HALF_SIZE                     = 0.07 * screen_height
BONUS_LIVE_SCALE_MIN                = 0.9
BONUS_LIVE_SCALE_MAX                = 1.1
BONUS_LIVE_SCALE_PERIOD             = 1
BONUS_APPEAR_SCALE                  = [ 0, 0.5, 2, 1 ]
BONUS_APPEAR_TIME                   = 0.5
BONUS_APPEAR_DELAY                  = 0.05
BONUS_DISAPPEAR_SCALE               = [ 1, 2, 0.5, 0 ]
BONUS_DISAPPEAR_TIME                = 0.5
BONUS_DISAPPEAR_DELAY               = 0.05
BONUS_RESET_ALPHA                   = 0.3
BONUS_RESET_SCALE                   = [ 2, 5, 0.5, 1 ]
BONUS_RESET_TIME                    = 0.5
BONUS_ACTIVATE_SCALE                = [ 1, 0.5, 5, 3 ]
BONUS_ACTIVATE_TIME                 = 0.5
BONUS_ACTIVATE_ROT_PERIOD           = 0.1
BONUS_ACTIVATE_ROT_AMP              = 5
BONUS_PREACTIVATE_TIME              = 0.5
BONUS_PREACTIVATE_DELAY             = 0.1
BONUS_SUPER_DROP                    = "super_drop"
BONUS_SUPER_HIT                     = "super_hit"
BONUS_BUILDER                       = "builder"
BONUS_KING_OF_HILL                  = "king_of_hill"
BONUS_ACID_RAIN                     = "acid_rain"
BONUS_HAIL                          = "hail"
BONUS_EARTHQUAKE                    = "earthquake"
BONUSES_TEXTURES                    = \
{   BONUS_SUPER_DROP                : "res/game/128x128_bonus_super_drop.png"
,   BONUS_SUPER_HIT                 : "res/game/128x128_bonus_super_hit.png"
,   BONUS_BUILDER                   : "res/game/128x128_bonus_builder.png"
,   BONUS_KING_OF_HILL              : "res/game/128x128_bonus_king_of_hill.png"
,   BONUS_ACID_RAIN                 : "res/game/128x128_bonus_acid_rain.png"
,   BONUS_HAIL                      : "res/game/128x128_bonus_hail.png"
,   BONUS_EARTHQUAKE                : "res/game/128x128_bonus_earthquake.png"
}

# ALIASES

bonuses_layer                       = layer ( glayers.BONUSES )
highlights_bonuses_layer            = layer ( glayers.BONUSES_HIGHLIGHTS )

# VARIABLES

ttasks                              = []

# PREFETCH

def prefetch () :
    for texture in BONUSES_TEXTURES.values () :
        bonuses_layer.prefetch_sprites              ( texture, BONUSES_MAX_COUNT_PER_TYPE )
        highlights_bonuses_layer.prefetch_sprites   ( texture, BONUSES_MAX_HIGHLIGHTS_PER_TYPE )

# BONUSES

class Bonus :
    def __init__ ( self, bonus_type, actions, x, y ) :
        self.can_be_activated       = False
        self.is_active              = False
        self.actions                = list ( actions )
        self.bonus_type             = bonus_type
        self.bonus_sprite           = bonuses_layer.new_sprite ( BONUSES_TEXTURES [ bonus_type ] )
        self.bonus_sprite.shape     = [ -BONUS_HALF_SIZE, BONUS_HALF_SIZE, BONUS_HALF_SIZE, -BONUS_HALF_SIZE ]
        self.bonus_sprite.x         = x
        self.bonus_sprite.y         = y
        self.bonus_sprite.scale     = 0
        self.bonus_sprite.alpha     = BONUS_RESET_ALPHA

        self.highlight_sprite       = highlights_bonuses_layer.new_sprite ( BONUSES_TEXTURES [ bonus_type ] )
        self.highlight_sprite.shape = self.bonus_sprite.shape
        self.highlight_sprite.x     = self.bonus_sprite.x
        self.highlight_sprite.y     = self.bonus_sprite.y
        self.highlight_sprite.scale = 0
        self.highlight_sprite.alpha = 0


    def __del__ ( self ) :
        self.actions = None
        self.bonus_sprite.kill ()
        self.highlight_sprite.kill ()

    def activation_update ( self ) :
        activation_update ( [ self ] )


def activation_update ( bonuses ) :

    @start_async
    def async_activation_update ( bonus ) :
        bonus.bonus_sprite.alpha = ease ( end = 1, dt = BONUS_PREACTIVATE_TIME )
        bonus.can_be_activated = True
        gactions.reset_action ( bonus.actions, bonus.bonus_sprite.x, bonus.bonus_sprite.y )


    is_anybody_activated = False
    for bonus in bonuses :
        if not bonus.can_be_activated and gactions.are_done ( bonus.actions ) :
            ttasks.append ( async_activation_update ( bonus ) )
            is_anybody_activated = True
    return is_anybody_activated


def activate ( bonus ) :
    assert bonus.can_be_activated
    bonus.is_active = True
    s = [ s for s in BONUS_ACTIVATE_SCALE ]
    s [ 0 ] = bonus.bonus_sprite.scale
    bonus.bonus_sprite.scale     = 0
    bonus.bonus_sprite.alpha     = 0
    bonus.highlight_sprite.alpha = 1
    bonus.highlight_sprite.scale = bezier3 ( s [ 0 ], s [ 1 ], s [ 2 ], s [ 3 ], dt = BONUS_ACTIVATE_TIME )
    wait ( BONUS_ACTIVATE_TIME )
    bonus.highlight_sprite.rot = ease ( end = -BONUS_ACTIVATE_ROT_AMP, dt = 0.5 * BONUS_ACTIVATE_ROT_PERIOD )
    wait ( 0.5 * BONUS_ACTIVATE_ROT_PERIOD )
    bonus.highlight_sprite.rot = ease ( -BONUS_ACTIVATE_ROT_AMP, BONUS_ACTIVATE_ROT_AMP, dt = BONUS_ACTIVATE_ROT_PERIOD, extend = 'extrapolate' )


def reset ( bonus ) :
    assert bonus.can_be_activated
    bonus.can_be_activated = False
    bonus.is_active        = False
    s = [ s for s in BONUS_RESET_SCALE ]
    s [ 0 ] = bonus.highlight_sprite.scale
    s [ 3 ] = BONUS_LIVE_SCALE_MIN
    bonus.highlight_sprite.scale  = bezier3 ( s [ 0 ], s [ 1 ], s [ 2 ], s [ 3 ], dt = BONUS_RESET_TIME )
    bonus.highlight_sprite.rot    = ease ( end = 0, dt = BONUS_RESET_TIME * abs ( bonus.bonus_sprite.rot ) )
    bonus.highlight_sprite.alpha  = ease ( end = BONUS_RESET_ALPHA, dt = BONUS_RESET_TIME )
    wait ( BONUS_RESET_TIME )
    bonus.highlight_sprite.scale  = 0
    bonus.highlight_sprite.alpha  = 0
    bonus.bonus_sprite.alpha      = BONUS_RESET_ALPHA
    bonus.bonus_sprite.scale      = ease ( BONUS_LIVE_SCALE_MIN, BONUS_LIVE_SCALE_MAX, dt = BONUS_LIVE_SCALE_PERIOD, extend = 'extrapolate' )



@start_async
def async_show ( bonuses ) :

    @start_async
    def async_do_show ( bonus ) :
        s = [ s for s in BONUS_APPEAR_SCALE ]
        s [ 3 ] = BONUS_LIVE_SCALE_MIN
        bonus.bonus_sprite.scale = bezier3 ( s [ 0 ], s [ 1 ], s [ 2 ], s [ 3 ], dt = BONUS_APPEAR_TIME )
        wait ( BONUS_APPEAR_TIME )
        bonus.bonus_sprite.scale  = ease ( BONUS_LIVE_SCALE_MIN, BONUS_LIVE_SCALE_MAX, dt = BONUS_LIVE_SCALE_PERIOD, extend = 'extrapolate' )


    tbonuses = []
    for bonus in bonuses :
        tbonuses.append ( async_do_show ( bonus ) )
        tbonuses.append ( gactions.async_show ( bonus.actions ) )
        wait ( BONUS_APPEAR_DELAY )

    for tbonus in tbonuses :
        wait ( tbonus )
    tbonuses = None


@start_async
def async_hide ( bonuses ) :

    @start_async
    def async_do_hide ( bonus ) :
        s = [ s for s in BONUS_DISAPPEAR_SCALE ]
        s [ 0 ] = bonus.bonus_sprite.scale
        bonus.bonus_sprite.scale = bezier3 ( s [ 0 ], s [ 1 ], s [ 2 ], s [ 3 ], dt = BONUS_DISAPPEAR_TIME )
        s [ 0 ] = bonus.highlight_sprite.scale
        bonus.highlight_sprite.scale = bezier3 ( s [ 0 ], s [ 1 ], s [ 2 ], s [ 3 ], dt = BONUS_DISAPPEAR_TIME )
        wait ( BONUS_DISAPPEAR_TIME )


    tbonuses = []
    for bonus in bonuses :
        tbonuses.append ( async_do_hide ( bonus ) )
        tbonuses.append ( gactions.async_hide ( bonus.actions ) )
        wait ( BONUS_DISAPPEAR_DELAY )

    for tbonus in tbonuses :
        wait ( tbonus )
    tbonuses = None


def wait_async_tasks () :
    global ttasks
    for ttask in ttasks :
        wait ( ttask )
    ttasks = []

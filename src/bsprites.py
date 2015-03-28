# -*- coding: utf-8 -*-

# LIBS
import copy
import os
import pygame
import rabbyt
import weakref

# BASE
import bevents
import btasks
import btexture

# PACKED RESOURCES
try :
    import res
except :
    res = None


# CONSTS
PACK_TEXTURE_SIZE   = 512
PACK_TEXTURE_FILTER = True
PACK_TEXTURE_MIPMAP = True

# GLOBALS
sorted_live_sprites = []
live_sprites        = {}
sprites_tag         = 0
texture_packs       = []
layers              = []


class SpriteInPack ( rabbyt.sprites.Sprite ) :

    def __init__ ( self, texture_in_pack ) :
        if not isinstance ( texture_in_pack, TextureInPack ) :
            raise RuntimeError ( "texture must be TextureInPack instance" )
        assert texture_in_pack.pack ()

        if texture_in_pack.pack ().texture_id == -1 :
            raise RuntimeError ( "unprefetched texture" )

        rabbyt.sprites.Sprite.__init__ ( self, texture_in_pack.pack ().texture_id, [ -1, 1, 1, -1 ], texture_in_pack.coords )

        global sprites_tag
        sprites_tag          += 1
        self.tag             = sprites_tag
        self.texture_in_pack = weakref.ref ( texture_in_pack )


    def layer_index ( self ) :
        assert self.texture_in_pack
        return self.texture_in_pack ().layer_index


    def spawn ( self ) :
        self.x      = 0
        self.y      = 0
        self.xy     = ( 0, 0 )
        self.scale  = 1
        self.rot    = 0
        self.red    = 1
        self.green  = 1
        self.blue   = 1
        self.alpha  = 1
        self.shape  = [ -1, 1, 1, -1 ]

        live_sprites [ self.tag ] = self

        global live_sprites_changed
        live_sprites_changed = True

        return self


    def kill ( self ) :
        if self.tag not in live_sprites :
            raise RuntimeError ( "sprite " + str ( self ) + " already killed" )

        assert self.texture_in_pack ()

        del live_sprites [ self.tag ]
        self.texture_in_pack ().sprites_pool.append ( self )

        global live_sprites_changed
        live_sprites_changed = True


class TextureInPack :

    def __init__ ( self, pack, coords, texture_name ) :
        self.pack           = weakref.ref ( pack )
        self.coords         = coords
        self.count          = 0
        self.sprites_pool   = []
        self.name           = texture_name
        self.layer_index    = -1


    def prefetch ( self ) :
        self.sprites_pool   += [ SpriteInPack ( self ) for i in range ( self.count ) ]


    def available_sprites ( self ) :
        return len ( self.sprites_pool )


    def new_sprite ( self ) :
        if self.available_sprites () == 0 :
            raise RuntimeError ( "out of free sprites for texture " + self.name
                         + " in pack " + str ( self.pack() ) + " ( " + str ( self.count ) + " allocated )" )

        return self.sprites_pool.pop ().spawn ()


class TexturePack :

    def __init__ ( self ) :
        self.texture_id     = -1
        self.texture_pack   = btexture.Pack ( ( PACK_TEXTURE_SIZE, PACK_TEXTURE_SIZE ) )
        texture_packs.append ( self )


    def __del__ ( self ) :
        self.unfetch ()


    def add ( self, texture ) :
        if not isinstance ( texture, type ( "" ) ) :
            raise RuntimeError ( "texture file name is expected" )

        if self.texture_id != -1 :
            raise RuntimeError ( "trying to add new texture after loading to video memory" )

        def fix_coords ( coords ) :
            return  [       min ( coords[0][0], coords[1][0], coords[2][0], coords[3][0] ) \
                    , 1.0 - min ( coords[0][1], coords[1][1], coords[2][1], coords[3][1] ) \
                    ,       max ( coords[0][0], coords[1][0], coords[2][0], coords[3][0] ) \
                    , 1.0 - max ( coords[0][1], coords[1][1], coords[2][1], coords[3][1] ) ]

        try :
            texture_name = texture
            if res and "lookup" in dir ( res ) and texture in res.lookup :
                r = res.lookup [ texture ]
                texture = pygame.image.fromstring ( r.data, r.size, r.format, r.flipped )
            else :
                if not os.path.isfile ( texture ) :
                    raise RuntimeError ( "texture file " + texture + " not found" )
            coords = self.texture_pack.pack ( texture )
            return TextureInPack ( self, fix_coords ( coords ), texture_name )
        except ValueError :
            return None


    def isprefetched ( self ) :
        return self.texture_id != -1


    def prefetch ( self ) :
        if not self.isprefetched () :
            data = pygame.image.tostring ( self.texture_pack.image, 'RGBA', True )
            size = self.texture_pack.image.get_size ()
            self.texture_id = rabbyt.load_texture ( data, size, 'RGBA', PACK_TEXTURE_FILTER, PACK_TEXTURE_MIPMAP )


    def unfetch ( self ) :
        if self.isprefetched () :
            rabbyt.unload_texture ( self.texture_id )


def add_to_pack ( texture ) :
    # TRY ADD TO EXISTING PACKS FIRST
    for pack in texture_packs :
        added = pack.add ( texture )
        if added :
            return added

    # CREATE NEW PACK
    pack  = TexturePack ()
    added = pack.add ( texture )
    if added :
        return added
    else :
        raise RuntimeError ( "texture " + texture + " is too large to be added to pack" )


def render () :
    global live_sprites_changed
    global sorted_live_sprites
    if live_sprites_changed :
        live_sprites_changed = False
        sorted_live_sprites = list ( live_sprites.values () )
        sorted_live_sprites.sort ( cmp = lambda s1, s2 : cmp ( s1.layer_index (), s2.layer_index () ) )

    rabbyt.render_unsorted ( sorted_live_sprites )


class Layer :

    def __init__ ( self, index ) :
        self.index              = index
        self.textures           = {}        # TEXTURE NAME  -> TEXTURE IN PACK
        self.key_click          = bevents.VirtualKey ()
        self.handled_key_click  = bevents.VirtualKey ()


    def __del__ ( self ) :
        self.unfetch ()


    def prefetch_sprites ( self, texture, count ) :
        if not isinstance ( texture, type ( "" ) ) :
            raise RuntimeError ( "texture file name is expected" )
        if not isinstance ( count, type ( 1 ) ) :
            raise RuntimeError ( "count must be integer number" )

        if texture not in self.textures :
            self.textures [ texture ] = add_to_pack ( texture )
            self.textures [ texture ].layer_index = self.index

        self.textures [ texture ].count += count


    def available_sprites ( self, texture ) :
        if not isinstance ( texture, type ( "" ) ) :
            raise RuntimeError ( "texture file name is expected" )
        if texture not in self.textures :
            raise RuntimeError ( "texture " + texture + " not prefetched for layer " + str ( self ) )

        return self.textures [ texture ].available_sprites ()


    def prefetch ( self ) :
        for texture in self.textures.values () :
            texture.prefetch ()


    def unfetch ( self ) :
        self.textures.clear ()


    def new_sprite ( self, texture ) :
        if not isinstance ( texture, type ( "" ) ) :
            raise RuntimeError ( "texture file name is expected" )

        # MUST BE LOADED
        if not texture in self.textures :
            raise RuntimeError ( "texture " + texture + " must be loaded first" )

        return self.textures [ texture ].new_sprite ()


def layer ( index ) :
    if not isinstance ( index, type ( 1 ) ) :
        raise RuntimeError ( "layer index must be a number" )
    if index < 0 :
        raise RuntimeError ( "layer index must be a positive number" )

    global layers
    if index >= len ( layers ) :
        start_idx = len ( layers )
        layers += [ Layer ( start_idx + i ) for i in range ( index - len ( layers ) + 1 ) ]

    return layers [ index ]


def prefetch () :
    for pack in texture_packs :
        pack.prefetch ()
    for layer in layers :
        layer.prefetch ()


def unfetch () :
    assert len ( live_sprites ) == 0
    global sorted_live_sprites
    sorted_live_sprites = []
    for layer in layers :
        layer.unfetch ()
    del texture_packs [ 0 : len ( texture_packs ) ]


@btasks.start_async
def async_catch_events () :

    @btasks.start_async
    def async_catch_click ( push_or_pop ) :
        while True :
            btasks.wait ( getattr ( bevents.key_click, push_or_pop ) )
            for layer in reversed ( layers ) :
                getattr    ( layer.handled_key_click, push_or_pop ).skip_missed ()
                getattr    ( layer.key_click        , push_or_pop ) ()
                if getattr ( layer.handled_key_click, push_or_pop ).missed () :
                    break


    tpush = async_catch_click ( "push" )
    tpop  = async_catch_click ( "pop"  )

    try :
        while True :
            btasks.wait ( 10000 )

    finally :
        btasks.stop ( tpush )
        btasks.stop ( tpop  )

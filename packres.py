# -*- coding: cp1251 -*-

# PREREQUISITES
import bimport
bimport.check ( "pygame" )

# LIBS
import os
import pygame
import string

# CONSTS

TAB_SIZE            = 4
CHARS_PER_LINE      = 16
IMAGE_EXTENSION     = 'png'
RESOURCES_FOLDER    = 'res'
IMAGE_FORMAT        = 'RGBA'
IMAGE_FLIPPED       = True

# RESOURCES PACKER

def pack_folder ( path ) :
    for name in os.listdir ( path ) :
        curpath = path + '/' + name
        if name.endswith ( '.' + IMAGE_EXTENSION ) and os.path.isfile ( curpath ) :
            files.append ( curpath )
        else :
            if os.path.isdir ( curpath ) :
                pack_folder ( curpath )

files = []
if os.path.isdir ( RESOURCES_FOLDER ) :
    pack_folder ( RESOURCES_FOLDER )
else :
    print "resources folder " + path + " does not exists"

trans = {}
for i in range ( 256 ) :
    if i < 16 :
        trans [ i ] = hex ( i ).replace ( '0x', '\\x0' )
    else :
        trans [ i ] = hex ( i ).replace ( '0x', '\\x' )

def write_to_file ( f, s ) :
    si = iter ( s )
    while True :
        out = " " * TAB_SIZE + "\""
        chars = ""
        try :
            for i in range ( CHARS_PER_LINE ) :
                chars += trans [ ord ( si.next () ) ]
        except StopIteration :
            break
        finally :
            if len ( chars ) :
                out += chars + "\"\\\n"
                f.write ( out )

def filename_to_id ( name ) :
    return name.lower().replace ( '/', '_' ).replace ( '.' + IMAGE_EXTENSION, '' )

files.sort ()
for name in files :
    print "processing " + name
    image = pygame.image.load ( name )
    image_str = pygame.image.tostring ( image, IMAGE_FORMAT, IMAGE_FLIPPED )
    id_name = filename_to_id ( name )
    f = open ( id_name + '.py', 'w' )
    f.write ( "name    = \"" + name + "\"\n" )
    f.write ( "format  = \"" + IMAGE_FORMAT + "\"\n" )
    f.write ( "flipped = " + str ( IMAGE_FLIPPED ) + "\n" )
    f.write ( "size    = " + str ( image.get_size () ) + "\n" )
    f.write ( "data    = \\\n" )
    write_to_file ( f, image_str )
    f.write ( "\n" )
    f.close ()
print "flushing buffers"

f = open ( RESOURCES_FOLDER + '.py', 'w' )
for name in files :
    f.write ( "import " + filename_to_id ( name ) + "\n" )
f.write ( "\nlookup = \\\n" )

ch = "{"
for name in files :
    module_name = filename_to_id ( name )
    f.write ( " " * TAB_SIZE + ch + " " + module_name + ".name : " + module_name + "\n" )
    ch = ","
f.write ( " " * TAB_SIZE + "}\n" )
f.close ()

# PREREQUISITES
import bimport
bimport.check ( "py2exe" )

# LIBS
from distutils.core import setup
import py2exe

# BASE
import bprofile

# CONSTS

VERSION          = "0.3.0.1"             # PUBLIC.STABLE.INNER.INNER
DESCRIPTION      = "my tetris game"
NAME             = "toothris"
PACK_RESOURCES   = True

# SETUP

bprofile.MEASURES_MIN_COUNT = 0

bprofile.begin ( "total" )

if PACK_RESOURCES :
    bprofile.begin ( "pack resources" )
    import packres
    bprofile.end ( "pack resources" )
else :
    f = open ( "res.py", "w" )
    f.close ()

bprofile.begin ( "build executable" )
setup \
(   version     = VERSION
,   description = DESCRIPTION
,   name        = NAME
,   options     = { "py2exe" :
        { "compressed"   : 1
        , "optimize"     : 2
        , "ascii"        : 1
        , "bundle_files" : 1
        } }
,   zipfile     = None
,   script_args = [ "py2exe" ]
,   windows     = [ "start.py" ]
)

bprofile.end ( "build executable" )

bprofile.end ( "total" )

bprofile.stats ()

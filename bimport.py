# -*- coding: cp1251 -*-

def check ( p ) :
    try:
        __import__ ( p )
    except:
        raise RuntimeError ( "package <%s> must be installed" % p )

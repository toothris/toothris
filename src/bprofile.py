# Copyright 2008, 2015 Oleg Plakhotniuk
#
# This file is part of Toothris.
#
# Toothris is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Toothris is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Toothris.  If not, see <http://www.gnu.org/licenses/>.

# LIBS
import pygame


# CONSTS

MEASURES_MIN_COUNT = 200


class Profiler :

    def __init__ ( self, name ) :
        self.name       = name
        self.time_min   = 999999
        self.time_max   = 0
        self.time_total = 0
        self.measures   = - MEASURES_MIN_COUNT
        self.clock      = pygame.time.Clock ()
        self.measuring  = False
        self.profilers  = {}


    def begin ( self ) :
        if self.measuring :
            raise RuntimeError ( "trying to start already started profiler" )

        self.clock.tick ()
        self.measuring = True


    def end ( self ) :
        if not self.measuring :
            raise RuntimeError ( "trying to stop not started profiler" )

        self.clock.tick ()
        self.measuring  = False
        self.measures   += 1
        if self.measures > 0 :
            self.time_total += self.clock.get_time ()
            self.time_min   = min ( self.time_min, self.clock.get_time () )
            self.time_max   = max ( self.time_max, self.clock.get_time () )


    def time_avg ( self ) :
        return float ( self.time_total ) / max ( self.measures, 1 )


root_profilers  = {}
stack_profilers = []


def begin ( name ) :
    global stack_profiler
    global root_profilers

    if not isinstance ( name, type ( "" ) ) :
        raise RuntimeError ( "string name expected" )
    if name == "" :
        raise RuntimeError ( "name must not be empty" )

    if len ( stack_profilers ) > 0 :
        profilers = stack_profilers [ len ( stack_profilers ) - 1 ].profilers
    else :
        profilers = root_profilers

    if name in profilers :
        profiler = profilers [ name ]
    else :
        profiler = Profiler ( name )
        profilers [ name ] = profiler

    profiler.begin ()
    stack_profilers.append ( profiler )


def end ( name ) :
    global stack_profilers

    if not isinstance ( name, type ( "" ) ) :
        raise RuntimeError ( "string name expected" )
    if len ( stack_profilers ) == 0 :
        raise RuntimeError ( "no profiler currently running" )
    if name == "" :
        raise RuntimeError ( "name must not be empty" )

    last_profiler = stack_profilers [ len ( stack_profilers ) - 1 ]
    if name != last_profiler.name :
        raise RuntimeError ( "trying to stop profiler " + name + \
            " before profiler " + last_profiler.name )

    stack_profilers.pop ().end ()


def stats_profilers ( profilers, indent = 0 ) :

    if len ( profilers ) == 0 :
        return


    def padded_str ( value, max_len = 0, left_padding = True ) :

        if isinstance ( value, type ( "" ) ) :
            str_value = value
        elif isinstance ( value, type ( 0 ) ) :
            str_value = str ( value )
        elif isinstance ( value, type ( 0.0 ) ) :
            str_value = "%(number).2f" % { "number" : value }

        spaces = max ( 0, max_len - len ( str_value ) )
        if left_padding :
            return " " * spaces + str_value
        else :
            return str_value + " " * spaces

    longest_name = max ( [ len ( padded_str ( p.name )       ) for p in profilers.values () ] )
    longest_min  = max ( [ len ( padded_str ( p.time_min   ) ) for p in profilers.values () ] )
    longest_max  = max ( [ len ( padded_str ( p.time_max   ) ) for p in profilers.values () ] )
    longest_avg  = max ( [ len ( padded_str ( p.time_avg() ) ) for p in profilers.values () ] )
    longest_msr  = max ( [ len ( padded_str ( p.measures   ) ) for p in profilers.values () ] )

    names = profilers.keys ()
    names.sort ()
    for name in names :
        profiler = profilers [ name ]

        if profiler.measures > 0 :
            print " " * 4 * indent  + padded_str ( profiler.name      , longest_name, False )   + \
                " : min = "         + padded_str ( profiler.time_min  , longest_min  )          + \
                " max = "           + padded_str ( profiler.time_max  , longest_max  )          + \
                " avg = "           + padded_str ( profiler.time_avg(), longest_avg  )          + \
                " frames = "        + padded_str ( profiler.measures  , longest_msr  )
        else :
            print " " * 4 * indent  + padded_str ( profiler.name      , longest_name, False )   + \
                " : not enough frames to profile ( " + str ( -profiler.measures ) + " left )"

        stats_profilers ( profiler.profilers, indent + 1 )


def stats () :
    print "profilers stats:"
    stats_profilers ( root_profilers )

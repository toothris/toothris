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

import optparse

parser = optparse.OptionParser(prog='toothris', usage='%prog [options]',
                               version='%prog 1.0.1')
parser.add_option('', '--width', default=800, type='int', dest='width',
                  help='Drawing area width.')
parser.add_option('', '--height', default=600, type='int', dest='height',
                  help='Drawing area height.')
parser.add_option('', '--fullscreen', default=False, dest='fullscreen',
                  action='store_true', help='Fullscreen mode.')
parser.add_option('', '--fps', default=60, type='int', dest='fps',
                  help='Target frames per second.')
parser.add_option('', '--freefps', default=True, dest='keepfps',
                  action='store_false', help='Don\'t maintain target FPS.')
parser.add_option('', '--norender', default=True, dest='render',
                  action='store_false', help='Don\'t draw anything.')
parser.add_option('', '--replay', default=False, dest='replay',
                  action='store_true', help='Replay events from file.')
parser.add_option('', '--record', default=False, dest='record',
                  action='store_true', help='Records events to file.')
parser.add_option('', '--events', default='toothris.events', dest='events',
                  help='Events file name.')
parser.add_option('', '--music', default='', dest='music',
                  help='Music file name.')
parser.add_option('', '--frames', default='', dest='frames',
                  help='Save each frame to file.')
parser.add_option('', '--stopframe', default=9999999, type='int',
                  dest='stopframe', help='Save each frame to file.')
(BCONF, args) = parser.parse_args()

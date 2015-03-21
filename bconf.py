# -*- coding: utf-8 -*-

import optparse

parser = optparse.OptionParser()
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
parser.add_option('', '--figures', default=3, type='int', dest='figures', 
                  help='Choose next figure out of N oldest ones.')
(BCONF, args) = parser.parse_args()

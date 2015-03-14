#Copyright (c) 2006 Simon Wittber
#
#Permission is hereby granted, free of charge, to any person
#obtaining a copy of this software and associated documentation files
#(the "Software"), to deal in the Software without restriction,
#including without limitation the rights to use, copy, modify, merge,
#publish, distribute, sublicense, and/or sell copies of the Software,
#and to permit persons to whom the Software is furnished to do so,
#subject to the following conditions:
#
#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
#BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
#ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
#CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

"""

This module contains facilites for working with and creating textures.

The Coords class is used for generating and manipulating texture coordinates.
Dont use it in an inner loop, its __getitem__ method is very slow.

The PackNode can recursively pack rectanges into a larger rectangle. The Pack
class uses the PackNode class to pack smaller images into one larger image.
This is useful for storing multiple images as one larger OpenGL texture which
helps avoid texture swaps.

"""

import pygame

class Coords(object):
    """
    A type for managing texture coordinates.
    Use * and / for scaling, + and - for translating.
    """
    __slots__ = ('lrbt',)
    def __init__(self, lrbt=(0.0,1.0,0.0,1.0)):
        self.lrbt = list(lrbt)

    def __repr__(self):
        return repr((self[0],self[1],self[2],self[3]))

    def __imul__(self, scalar):
        self.lrbt[:] = [i * scalar for i in self.lrbt]
        return self

    def __idiv__(self, scalar):
        self.lrbt[:] = [i / scalar for i in self.lrgb]
        return self

    def __iadd__(self, vec2):
        self.lrbt[0] += vec2[0]
        self.lrbt[1] += vec2[0]
        self.lrbt[2] += vec2[1]
        self.lrbt[3] += vec2[1]
        return self

    def __isub__(self, vec2):
        self.lrbt[0] -= vec2[0]
        self.lrbt[1] -= vec2[0]
        self.lrbt[2] -= vec2[1]
        self.lrbt[3] -= vec2[1]
        return self

    def __mul__(self, scalar):
        return Coords([i * scalar for i in self.lrbt])

    def __div__(self, scalar):
        return Coords([i / scalar for i in self.lrbt])

    def __add__(self, vec2):
        return Coords((self.lrbt[0]+vec2[0],self.lrbt[1]+vec2[0],self.lrbt[2]+vec2[1],self.lrbt[3]+vec2[1]))

    def __sub__(self, vec2):
        return Coords((self.lrbt[0]-vec2[0],self.lrbt[1]-vec2[0],self.lrbt[2]-vec2[1],self.lrbt[3]-vec2[1]))

    def __getitem__(self, i):
        """
        Index 0 is bottom left coordinate.
        Index 1 is top left coordinate.
        Index 2 is top right coordinate.
        Index 3 is bottom right coordinate.
        """
        if i == 0:
            return self.lrbt[0], self.lrbt[2]
        elif i == 1:
            return self.lrbt[0], self.lrbt[3]
        elif i == 2:
            return self.lrbt[1], self.lrbt[3]
        elif i == 3:
            return self.lrbt[1], self.lrbt[2]
        else:
            raise IndexError


class PackNode(object):
    """
    Creates an area which can recursively pack smaller areas into itself.
    """
    def __init__(self, area):
        """
        Creates an area (w,h) which will smaller areas can be packed into via
        the insert method.
        """
        #if tuple contains two elements, assume they are width and height, and origin is (0,0)
        if len(area) == 2:
            area = (0,0,area[0],area[1])
        self.area = area

    def __repr__(self):
        return "<%s %s>" % (self.__class__.__name__, str(self.area))

    def get_width(self):
        return self.area[2] - self.area[0]
    width = property(fget=get_width)

    def get_height(self):
        return self.area[3] - self.area[1]
    height = property(fget=get_height)

    def insert(self, area):
        """
        Insert an area into the current area. Returns a new Node representing
        the new area.
        Returns None if no space is available for the new area.
        """
        if hasattr(self, 'child'):
            a = self.child[0].insert(area)
            if a is None: return self.child[1].insert(area)
            return a

        area = PackNode(area)
        if area.width <= self.width and area.height <= self.height:
            self.child = [None,None]
            self.child[0] = PackNode((self.area[0]+area.width, self.area[1], self.area[2], self.area[1] + area.height))
            self.child[1] = PackNode((self.area[0], self.area[1]+area.height, self.area[2], self.area[3]))
            return PackNode((self.area[0], self.area[1], self.area[0]+area.width, self.area[1]+area.height))


class Pack(object):
    """
    The Pack class uses the PackNode class to paste smaller images into a
    larger image.
    """
    def __init__(self, size=(512,512)):
        """
        The size keyword specifies the size of the larger image, which
        smaller images will be packed into.
        Once packing is complete, the .image attribute will contain a pygame
        Surface which can be saved.
        """
        self.tree = PackNode(size)
        self.image = pygame.Surface(size, pygame.SRCALPHA, 32)
        self.wr = 1.0 / float(size[0])
        self.hr = 1.0 / float(size[1])

    def pack(self, img):
        """
        Pack a smaller image into the larger image, and return a 4 tuple of
        normalized coordinates which contain the location of the pasted
        image. If no space is left in the parent image, ValueError is raised.
        """
        wr = self.wr
        hr = self.hr
        if not isinstance(img, pygame.Surface):
            img = pygame.image.load(img).convert(32, pygame.SRCALPHA)
            img = img.convert_alpha(img)
        uv = self.tree.insert(img.get_size())
        if uv is None: raise ValueError('Pack size too small.')
        area = tuple(uv.area)
        self.image.blit(img, area)
        uv = area[0] * wr, area[1] * hr, area[2] * wr, area[3] * hr
        return (uv[0],uv[1]),(uv[0], uv[3]), (uv[2],uv[3]), (uv[2], uv[1])



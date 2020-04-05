from esper import World
from engine import Scene

from OpenGL import *
from OpenGL.GL import *

import numpy

class MainMenu(Scene):
    def __init__(self):
        self._triangle = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self._triangle)
        glBufferData(
                GL_ARRAY_BUFFER,
                numpy.array(
                    [0.5, 0.5, -0.5, 0.5, -0.5, -0.5, 0.5, -0.5],
                    dtype='float32'),
                GL_STATIC_DRAW)

    def __del__(self):
        glDeleteBuffers(1, self._triangle)

    def process(self):
        self._render()

    def _render(self):
        glClearColor(0, 0.5, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT)
        glBindBuffer(GL_ARRAY_BUFFER, self._triangle)



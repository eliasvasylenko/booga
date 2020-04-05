from esper import World
from engine import Scene

from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLEW import *
from OpenGL.arrays import *

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

        vertex_shader = shaders.compileShader("""#version 140
            in vec2 LVertexPos2D;
            void main() {
                gl_Position = vec4( LVertexPos2D.x, LVertexPos2D.y, 0, 1 );
            }""", GL_VERTEX_SHADER)

        fragment_shader = shaders.compileShader("""#version 140
            out vec4 LFragment;
            void main() {
                LFragment = vec4( 1.0, 1.0, 1.0, 1.0 );
            }""", GL_FRAGMENT_SHADER)

        self._triangle_shader = shaders.compileProgram(vertex_shader, fragment_shader)

    def __del__(self):
        glDeleteBuffers(1, self._triangle)

    def process(self):
        self._render()

    def _render(self):
        glClearColor(0, 0.5, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(self._triangle_shader)
        glEnableVertexAttribArray(pos2d)
        
        glBindBuffer(GL_ARRAY_BUFFER, self._triangle)
        glVertexAttribPointer(pos2d, 2, GL_FLAOT, GL_FALSE, 2 * 8, NULL)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self._triangle_indices)
        glDrawElements(GL_TRIANGLE_FAN, 4, GL_UNSIGNED_INT, NULL)

        glDisableVertexAttribArray(pos2d)

        glUseProgram(None)


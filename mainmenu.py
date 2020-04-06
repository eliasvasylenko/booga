from esper import World
from engine import Scene

from OpenGL import *
from OpenGL.GL import *
from OpenGL.arrays import *
from OpenGL.GL.shaders import *

import numpy

class MainMenu(Scene):
    def __init__(self):
        self._vertex_shader = compileShader("""#version 330
            in vec2 LVertexPos2D;
            void main() {
                gl_Position = vec4( LVertexPos2D.x, LVertexPos2D.y, 0, 1 );
            }""", GL_VERTEX_SHADER)

        self._fragment_shader = compileShader("""#version 330
            out vec4 LFragment;
            void main() {
                LFragment = vec4( 1.0, 1.0, 0.0, 1.0 );
            }""", GL_FRAGMENT_SHADER)

        self._triangle = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self._triangle)
        glBufferData(
                GL_ARRAY_BUFFER,
                numpy.array(
                    [0.5, 0.5, -0.5, 0.5, -0.5, -0.5, 0.5, -0.5],
                    dtype='float32'),
                GL_STATIC_DRAW)
        
        self._triangle_indices = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self._triangle_indices)
        glBufferData(
                GL_ELEMENT_ARRAY_BUFFER,
                numpy.array(
                    [0, 1, 2, 3],
                    dtype='int32'),
                GL_STATIC_DRAW)
        
        self._vao = glGenVertexArrays(1);
        glBindVertexArray(self._vao);

        self._triangle_shader = compileProgram(self._vertex_shader, self._fragment_shader)
        self._vertex_location = glGetAttribLocation(self._triangle_shader, 'LVertexPos2D')


        glVertexAttribPointer(
                self._vertex_location, 2, GL_FLOAT, GL_FALSE,
                2 * ctypes.sizeof(ctypes.c_float), None)
        glEnableVertexAttribArray(self._vertex_location)

    def __del__(self):
        glDeleteBuffers(1, self._triangle)
        glDeleteShader(self._vertex_shader)
        glDeleteShader(self._fragment_shader)

    def process(self):
        self._render()

    def _render(self):
        glClearColor(0, 0.5, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(self._triangle_shader)
        
        glBindVertexArray(self._vao);

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self._triangle_indices)
        glDrawElements(GL_TRIANGLE_FAN, 4, GL_UNSIGNED_INT, None)

        glUseProgram(0)


from esper import World
from engine import Scene

from OpenGL import *
from OpenGL.GL import *
from OpenGL.arrays import *
from OpenGL.GL.shaders import *

import numpy
import math

class MainMenu(Scene):
    def __init__(self):
        vertex_shader = compileShader("""#version 330
            in vec2 LVertexPos;
            uniform mat3 LTransform;
            void main() {
                vec3 v3 = vec3( LVertexPos, 1 ) * LTransform;
                gl_Position = vec4( v3[0], v3[1], 0, 1 );
            }""", GL_VERTEX_SHADER)

        fragment_shader = compileShader("""#version 330
            out vec4 LFragment;
            void main() {
                LFragment = vec4( 1.0, 1.0, 0.0, 1.0 );
            }""", GL_FRAGMENT_SHADER)

        self._triangle_shader = compileProgram(vertex_shader, fragment_shader)
        vertex_location = glGetAttribLocation(self._triangle_shader, 'LVertexPos')
        self._transform = glGetUniformLocation(self._triangle_shader, 'LTransform')

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

        glVertexAttribPointer(
                vertex_location, 2, GL_FLOAT, GL_FALSE,
                2 * ctypes.sizeof(ctypes.c_float), None)
        glEnableVertexAttribArray(vertex_location)

        self._ang = 0

    def __del__(self):
        glDeleteBuffers(1, self._triangle)
        glDeleteProgram(self._triangle_shader)

    def process(self):
        self._render()

    def _render(self):
        glClearColor(0, 0.5, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT)

        self._ang += 0.01

        glUseProgram(self._triangle_shader)
        glBindVertexArray(self._vao)
        glUniformMatrix3fv(self._transform, 1, False,
                numpy.array(
                    [[math.cos(self._ang), -math.sin(self._ang), 0.4],
                     [math.sin(self._ang), math.cos(self._ang), 0],
                     [0, 0, 1]]))
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self._triangle_indices)
        glDrawElements(GL_TRIANGLE_FAN, 4, GL_UNSIGNED_INT, None)

        glUseProgram(0)


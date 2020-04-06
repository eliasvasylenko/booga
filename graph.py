import esper
from phys import Position, Angle
import numpy as np
from OpenGL.GL import *
import ctypes

class Transformation:
    def __init__(self, matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=np.float32)):
        self.matrix = matrix

class Mesh:
    def __init__(self, vertex_list, mode):
        self.vertex_list = vertex_list
        self.mode = mode

class Meshes:
    def __init__(self, *meshes):
        self.meshes = meshes

class Camera:
    def __init__(self, depth, proj):
        self.depth = depth
        self.proj = proj

class VertexBuffers:
    def __init__(self):
        self.vbos = []

class GraphicsProcessor(esper.Processor):
    def process(self):
        for ent, (trans, pos, ang) in self.world.get_components(Transformation, Position, Angle):
            cosa = np.cos(ang.a)
            sina = np.sin(ang.a)
            trans.matrix = np.array([[cosa, -sina, pos.x, 0],
                                     [sina, cosa, pos.y, 0],
                                     [0, 0, 1, 0],
                                     [0, 0, 0, 1]],
                                    dtype=np.float32)
            trans.matrix = np.linalg.inv(trans.matrix)

        buff = GLuint()
        glGenBuffers(1, ctypes.pointer(buff))
        glDeleteBuffers(1, ctypes.pointer(buff))
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glMultMatrixf(np_matrix_to_c_array(
            np.array([[0.005, 0, 0, 0],
                      [0, 0.005, 0, 0],
                      [0, 0, 1, 0],
                      [-1, -1, 0, 1]])))

        for ent, (meshes, trans) in self.world.get_components(Meshes, Transformation):
            for mesh in meshes.meshes:
                glPushMatrix()
                glMultMatrixf(np_matrix_to_c_array(trans.matrix))
                mesh.vertex_list.draw(mesh.mode)
                glPopMatrix()

def np_matrix_to_c_array(arr):
    if (not (arr.flags["C_CONTIGUOUS"] or
             arr.flags["F_CONTIGUOUS"]) or
            (arr.dtype != np.float32)):
        arr = np.ascontiguousarray(arr, dtype=np.float32)

    return arr.ctypes.data_as(ctypes.POINTER(ctypes.c_float * arr.size))[0]

# Way to make our engine work for lots of different types of shader ...

# Shaders do not all have to have the same attributes, uniforms, etc. Attributes with the same semantic meaning have the same name, and no set location. So to query what data needs to be put into the shader we just have to query the known attribute/uniform names and see whether they are present. From this we can pull the correct info from the appropriate component! Or we can even select from a set of related shaders based on which components (and therefore which attributes/uniforms) are present. Or we can have default values for some uniforms. Or we can do any number of other things! Material system?

# Definitely not necessary to implement all this out of the gate (or ever) but useful to at least think about how to structure code to allow it to evolve into something more sophisticated if that becomes necessary.

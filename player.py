import phys
import pyglet
import graph

def create_player(world, x, y):
    world.create_entity(
        phys.Position(x, y),
        phys.Velocity(0, 0),
        phys.Angle(0),
        graph.Meshes(graph.Mesh(
            pyglet.graphics.vertex_list(3,
                ('v2i', (-10, -10, 0, 20, 10, -10))),
            pyglet.gl.GL_TRIANGLE_FAN)))

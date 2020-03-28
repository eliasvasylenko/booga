import esper
import phys

class Shape:
    def __init__(self, points):
        self.points = points

class Mesh:
    def __init__(self, shape, mode):
        self.shape = shape
        self.mode = mode

class Meshes:
    def __init__(self, meshes):
        self.meshes = meshes

class Camera:
    def __init__(self, depth, proj):
        self.depth = depth
        self.proj = proj

class GraphicsProcessor(esper.Processor):
    def process(self):
        for ent, (meshes, pos, ang) in self.world.get_components(Meshes, phys.Position, phys.Angle):
            for mesh in meshes:
                verts = 
                pyglet.graphics.draw(


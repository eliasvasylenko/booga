import esper
import phys

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

class GraphicsProcessor(esper.Processor):
    def process(self):
        for ent, (meshes, pos, ang) in self.world.get_components(Meshes, phys.Position, phys.Angle):
            for mesh in meshes.meshes:
                mesh.vertex_list.draw(mesh.mode)


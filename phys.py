import esper

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Velocity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Acceleration:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PhysicalProcessor(esper.Processor):
    def process(self):
        for ent, (acc, vel) in self.world.get_components(Acceleration, Velocity):
            vel.x += acc.x
            vel.y += acc.y
        for ent, (vel, pos) in self.world.get_components(Velocity, Position):
            pos.x += vel.x
            pos.y += vel.y

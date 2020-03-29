import esper

class Age:
    def __init__(self):
        self.age = 0

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

class Angle:
    def __init__(self, a):
        self.a = a

class AngularVelocity:
    def __init__(self, a):
        self.a = a

class AngularAcceleration:
    def __init__(self, a):
        self.a = a

class PhysicalProcessor(esper.Processor):
    def process(self):
        for ent, (acc, vel) in self.world.get_components(Acceleration, Velocity):
            vel.x += acc.x
            vel.y += acc.y
        for ent, (vel, pos) in self.world.get_components(Velocity, Position):
            pos.x += vel.x
            pos.y += vel.y
        for ent, (ang_acc, ang_vel) in self.world.get_components(AngularAcceleration, AngularVelocity):
            ang_vel.a += ang_acc.a
        for ent, (vel, pos) in self.world.get_components(AngularVelocity, Angle):
            ang.a += ang_vel.a
        for ent, (age) in self.world.get_components(Age):
            age.age++

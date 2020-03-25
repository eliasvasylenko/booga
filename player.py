import phys

def create_player(world, x, y):
    world.create_entity(phys.Position(x, y),
                        phys.Velocity(0, 0))

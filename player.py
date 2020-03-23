import geom

def create_player(world, x, y):
    world.create_entity(geom.Position(x, y),
                        geom.Velocity(0, 0))

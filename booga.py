import sdl2
from sdl2 import ext
from sdl2.ext import Window

from esper import World
from player import create_player
from phys import PhysicalProcessor
from expr import Expression, Prop
from graph import Mesh, Meshes, Camera, GraphicsProcessor

if (sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO) != 0):
    error = sdl2.SDL_GetError()
    print(f'SDL_Init failed {error}')

window = sdl2.SDL_CreateWindow(
    b'Hello, Lindsey!',
    sdl2.SDL_WINDOWPOS_UNDEFINED, sdl2.SDL_WINDOWPOS_UNDEFINED,
    640, 480, 0)
sdl2.SDL_ShowWindow(window)

world = World()
world.add_processor(PhysicalProcessor())
world.add_processor(GraphicsProcessor())

create_player(world, 1, 1)
create_player(world, -10, 10)
create_player(world, -10, -10)
create_player(world, 10, -10)

running = True
while running:
    events = ext.get_events()
    for event in events:
        if event.type == sdl2.SDL_QUIT:
            running = False
            break
    world.process()

js = sdl2.joystick.SDL_NumJoysticks()
print(f'Joy! {js}')

class Add(Expression):
    def _eval(self, *addends):
        print('adding!')
        return sum(addends)


one = Prop(10)

two = Prop(7)

three = Prop(31)

add = Add(one, two, three)

print(add.eval())
print(add.eval())

two.mod(11)

print(add.eval())
print(add.eval())

sdl2.SDL_DestroyWindow(window)
sdl2.SDL_Quit()

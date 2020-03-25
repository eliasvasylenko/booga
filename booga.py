import pyglet
from pyglet.window import key
from pyglet.window import mouse
import esper
import player
import phys

print('Hello, Lindsey!')

window = pyglet.window.Window()
image = pyglet.resource.image('kitten.png')

world = esper.World()
world.add_processor(phys.PhysicalProcessor())

player.create_player(world, 100, 100)

@window.event
def on_draw():
    world.process()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print(f'The left mouse button was pressed. ({x}, {y})')

pyglet.app.run()

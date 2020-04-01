from pyglet import window, app, resource
from pyglet.window import key, mouse, Window

from esper import World
from player import create_player
from phys import PhysicalProcessor
from expr import Expression, Prop
from graph import Mesh, Meshes, Camera, GraphicsProcessor

print('Hello, Lindsey!')

window = Window()

world = World()
world.add_processor(PhysicalProcessor())
world.add_processor(GraphicsProcessor())

create_player(world, 1, 1)
create_player(world, -10, 10)
create_player(world, -10, -10)
create_player(world, 10, -10)

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

app.run()



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


from sdl2 import *
from OpenGL import *
from OpenGL.GL import *
import ctypes
from expr import Expression, Prop

class Game:
    def __init__(self):
        init = SDL_Init(SDL_INIT_EVERYTHING)
        if (init != 0):
            error = SDL_GetError()
            raise Exception(f'SDL_Init failed {error}')

        self._window = SDL_CreateWindow(
            b'Hello, Lindsey!',
            SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,
            0, 0, SDL_WINDOW_FULLSCREEN_DESKTOP | SDL_WINDOW_OPENGL)
        if (self._window == None):
            error = SDL_GetError()
            raise Exception(f'SDL_CreateWindow failed {error}')

        SDL_ShowWindow(self._window)

        self._init_video()

        self._init_joysticks()

    def quit(self):
        SDL_DestroyWindow(self._window)
        SDL_Quit()

    def _init_video(self):
        SDL_GL_SetAttribute(SDL_GL_ACCELERATED_VISUAL, 1)
        SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 4)
        SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 5)
        SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1)
        SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 24)

        self._maincontext = SDL_GL_CreateContext(self._window)
        if (self._maincontext == None):
            raise Exception('Failed to create OpenGL context')

        SDL_GL_SetSwapInterval(1)

        w = ctypes.c_int()
        h = ctypes.c_int()
        SDL_GetWindowSize(self._window, w, h)
        print(f'Window size {w.value}, {h.value}')

        glViewport(0, 0, w.value, h.value)
        glClearColor(0, 0.5, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT)
        SDL_GL_SwapWindow(self._window)

    def _init_joysticks(self):
        js = joystick.SDL_NumJoysticks()
        print(f'Joy! {js}')

game = Game()

SDL_Delay(1000)

game.quit()

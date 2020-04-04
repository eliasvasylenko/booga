from sdl2 import *
from OpenGL import *
from OpenGL.GL import *
import ctypes
from expr import Expression, Prop

class Game:
    def __init__(self):
        init = SDL_Init(SDL_INIT_EVERYTHING)
        if init != 0:
            error = SDL_GetError()
            raise Exception(f'SDL_Init failed {error}')

        self._window = SDL_CreateWindow(
            b'Hello, Lindsey!',
            SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,
            0, 0, SDL_WINDOW_FULLSCREEN_DESKTOP | SDL_WINDOW_OPENGL)
        if self._window == None:
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
        SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 2)
        SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1)
        SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 24)

        self._maincontext = SDL_GL_CreateContext(self._window)
        if self._maincontext == None:
            error = SDL_GetError()
            raise Exception(f'Failed to create OpenGL context {error}')

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

    def start(self):
        running = True
        event = SDL_Event()

        while running:
            while SDL_PollEvent(ctypes.byref(event)) != 0:
                if event.type == SDL_QUIT:
                    running = False
                elif event.type == SDL_WINDOWEVENT:
                    self._on_window_event(event.window)
                elif event.type == SDL_KEYDOWN:
                    self._on_key_down_event(event.key)
                elif event.type == SDL_KEYUP:
                    self._on_key_up_event(event.key)

        self.quit()

    def _on_window_event(self, window):
        pass

    def _on_key_down_event(self, key):
        pass

    def _on_key_up_event(self, key):
        pass

Game().start()

from sdl2 import *
from OpenGL import *
from OpenGL.GL import *
import ctypes
from expr import Expression, Prop
from enum import Enum

class Engine:
    def __init__(self):
        init = SDL_Init(SDL_INIT_EVERYTHING)
        if init != 0:
            error = SDL_GetError()
            raise Exception(f'{error}')

        self._init_video()

        self._init_joysticks()
    
    def quit(self):
        SDL_DestroyWindow(self._window)
        SDL_Quit()

    def _init_window(self):
        self._window = SDL_CreateWindow(
            b'Hello, Lindsey!',
            SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,
            640, 480, SDL_WINDOW_OPENGL | SDL_WINDOW_RESIZABLE)
        if self._window == None:
            error = SDL_GetError()
            raise Exception(f'{error}')

        SDL_ShowWindow(self._window)
        self._fullscreen_mode = SDL_WINDOW_FULLSCREEN_DESKTOP
        self._refresh_window()

    def _init_video(self):
        self._init_window()

        SDL_GL_SetAttribute(SDL_GL_ACCELERATED_VISUAL, 1)
        SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 4)
        SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 2)
        SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1)
        SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 24)

        self._maincontext = SDL_GL_CreateContext(self._window)
        if self._maincontext == None:
            error = SDL_GetError()
            raise Exception(f'{error}')

        SDL_GL_SetSwapInterval(1)

    def _on_window_event(self, scene, window):
        self._refresh_window()

    def _set_fullscreen_real(self):
        self._fullscreen_mode = SDL_WINDOW_FULLSCREEN
        self._refresh_window()

    def _set_fullscreen_fake(self):
        self._fullscreen_mode = SDL_WINDOW_FULLSCREEN_DESKTOP
        self._refresh_window()

    def _toggle_fullscreen(self):
        self._set_fullscreen(not self._is_fullscreen())

    def _is_fullscreen(self):
        return (SDL_GetWindowFlags(self._window) &
            (SDL_WINDOW_FULLSCREEN | SDL_WINDOW_FULLSCREEN_DESKTOP)) != 0

    def _set_fullscreen(self, setting):
        if setting == self._is_fullscreen():
            return
        window_mode = self._fullscreen_mode if setting else 0
        SDL_SetWindowFullscreen(self._window, window_mode)
        self._refresh_window()

    def _refresh_window(self):
        w = ctypes.c_int()
        h = ctypes.c_int()
        SDL_GetWindowSize(self._window, w, h)
        glViewport(0, 0, w.value, h.value)

    def _init_joysticks(self):
        js = joystick.SDL_NumJoysticks()

    def open_scene(self, scene):
        event = SDL_Event()

        while not scene is None:
            while SDL_PollEvent(ctypes.byref(event)) != 0:
                if event.type == SDL_QUIT:
                    scene.quit()
                elif event.type == SDL_WINDOWEVENT:
                    self._on_window_event(scene, event.window)
                elif event.type == SDL_KEYDOWN:
                    self._on_key_down_event(scene, event.key)
                elif event.type == SDL_KEYUP:
                    self._on_key_up_event(scene, event.key)
    
            scene.process()
            SDL_GL_SwapWindow(self._window)

            if scene.has_next_scene():
                scene = scene.next_scene()

    def _on_key_down_event(self, scene, key):
        if key.keysym.sym == SDLK_F11:
            self._toggle_fullscreen()
        elif key.keysym.sym == SDLK_ESCAPE:
            scene.back()

    def _on_key_up_event(self, scene, key):
        pass

    def _peek_channel(self):
        pass

class Scene:
    def quit(self):
        self._next_scene = None

    def back(self):
        self.quit()

    def has_next_scene(self):
        return hasattr(self, '_next_scene')

    def next_scene(self):
        next_scene = self._next_scene
        del self._next_scene
        return next_scene

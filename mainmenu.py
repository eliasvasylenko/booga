class MainMenu:
    def __init__(self):
        self._running = True

    def close(self):
        self._running = False

    def is_running(self):
        return self._running

    def process(self):
        pass

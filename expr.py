class Observable:
    def __init__(self):
        self.obs = set()

    def _trigger(self):
        for ob in self.obs:
            ob()

    def add_observer(self, observer):
        self.obs.add(observer)

    def remove_observer(self, observer):
        self.obs.add(observer)

class Value(Observable):
    def __init__(self):
        super().__init__()

    def eval(self):
        return self

    def _make_dirty(self):
        self._trigger()

class Prop(Observable):
    def __init__(self, value):
        super().__init__()
        self.__value = value

    def eval(self):
        return self.__value

    def mod(self, value):
        if self.__value != value:
            self.__value = value
            self._trigger()

_DIRTY = object()

class Expression(Observable):
    def __init__(self, *deps):
        super().__init__()
        self.__value = _DIRTY
        for dep in deps:
            dep.add_observer(self._make_dirty)
        self.__deps = deps

    def eval(self):
        if (self.__value == _DIRTY):
            self.__value = self._eval(*[d.eval() for d in self.__deps])
        return self.__value

    def _set_dependencies(self, *deps):
        for dep in self.__deps:
            dep.remove_observer(self._make_dirty)
        for dep in deps:
            dep.add_observer(self._make_dirty)
        self.__deps = deps
        self._make_dirty()

    def _make_dirty(self):
        if (self.__value != _DIRTY):
            self.__value = _DIRTY
            self._trigger()

class LazyProp(Expression):
    def __init(self, func):
        self.__func = func

    def _eval(self):
        return self.__func()

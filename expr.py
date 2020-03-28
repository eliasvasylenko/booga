class Expression:
    def __init__(self, value=DIRTY):
        self.__value = value

    def eval(self):
        if (__value == DIRTY):
            __value = _eval(*[d.eval() for d in __deps])
        return __value

    def _set_dependencies(self, deps*):
        for dep in __deps:
            dep.remove_dependent(self._make_dirty)
        for dep in deps:
            dep.add_dependent(self,_make_dirty)
        __deps = deps
        _make_dirty()

    def _make_dirty(self):
        __value = DIRTY

    def add_dependent(self, dependent):


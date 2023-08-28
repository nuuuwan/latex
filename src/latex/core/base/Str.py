from latex.core.base.Texable import Texable


class Str(Texable):
    def __init__(self, s: str):
        assert isinstance(s, str)
        Texable.__init__(self, s)

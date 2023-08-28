from latex.core.base.Join import Join
from latex.core.base.Tag import Tag
from latex.core.base.Texable import Texable


class Italic(Texable):
    def __init__(self, *children):
        for child in children:
            assert isinstance(child, Texable)
        tex = Tag('textit', Join(*children))
        Texable.__init__(self, tex)

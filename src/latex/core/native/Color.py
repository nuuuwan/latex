from latex.core.base.Join import Join
from latex.core.base.Str import Str
from latex.core.base.Tag import Tag
from latex.core.base.Texable import Texable


class Color(Texable):
    def __init__(self, color, *children):
        for child in children:
            assert isinstance(child, Texable)

        tex = Tag('textcolor', [Str(color), Join(*children)])

        Texable.__init__(self, tex)

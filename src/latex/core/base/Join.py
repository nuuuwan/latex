from latex.core.base.Texable import Texable


class Join(Texable):
    def __init__(self, *children):
        for child in children:
            assert isinstance(child, Texable)
        tex = ' '.join([child.tex for child in children])
        Texable.__init__(self, tex)

from latex.core.base.Texable import Texable


class Bold(Texable):
    def __init__(self, *children):
        for child in children:
            assert isinstance(child, Texable)
        tex = '\\textbf{' + ' '.join([child.tex for child in children]) + '}'
        Texable.__init__(self, tex)

from latex.core.base.Texable import Texable


class BeginEnd(Texable):
    def __init__(self, tag_name: str, *children: list):
        Texable.__init__(
            self,
            *(
                [
                    '\\begin{%s}' % tag_name,
                ]
                + list(children)
                + ['\\end{%s}' % tag_name]
            )
        )

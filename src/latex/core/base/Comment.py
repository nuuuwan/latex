from latex.core.base.Texable import Texable

LINE_WIDTH = 64


class Comment(Texable):
    def __init__(self, *lines: list[str]):
        Texable.__init__(self, *['% ' + line for line in lines])

    @staticmethod
    def line():
        return Comment('-' * LINE_WIDTH)

    @staticmethod
    def title(*lines: list[str]):
        return Texable(
            Comment.line(),
            Comment(*lines),
            Comment.line(),
        )

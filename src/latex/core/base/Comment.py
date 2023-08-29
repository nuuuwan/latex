from latex.core.base.Texable import Texable

LINE_WIDTH = 64


class Comment(Texable):
    def __init__(self, *lines: list[str]):
        Texable.__init__(self, *['% ' + line for line in lines])

    @staticmethod
    def line(line_width: int = 0):
        line_width = line_width or LINE_WIDTH
        return Comment('-' * line_width)

    @staticmethod
    def title(*lines: list[str]):
        return Texable(
            Comment.line(),
            Comment(*lines),
            Comment.line(),
        )

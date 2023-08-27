from latex.core.base.Tag import Tag
from latex.core.base.Texable import Texable


class Title(Texable):
    def __init__(self, title: str, author: str = "", date: str = " "):
        Texable.__init__(
            self,
            Tag("title", title),
            Tag("author", author),
            Tag("date", date),
            Tag("maketitle"),
        )

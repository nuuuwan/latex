from latex.core.base.Tag import Tag
from latex.core.base.Texable import Texable
from latex.core.native.Document import Document
from latex.core.native.DocumentClass import DocumentClass
from latex.core.native.Title import Title


class LatexBook(Texable):
    def __init__(self, title: str, author: str, *children):
        Texable.__init__(
            self,
            DocumentClass('book'),
            Document(
                Title(title, author, ' '),
                Tag('tableofcontents'),
                *children,
            ),
        )

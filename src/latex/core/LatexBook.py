from latex.core.base.Texable import Texable
from latex.core.native.Document import Document
from latex.core.native.DocumentClass import DocumentClass
from latex.core.native.Title import Title
from latex.core.base.Tag import Tag


class LatexBook(Texable):
    def __init__(self, title, *children):
        Texable.__init__(
            self,
            DocumentClass('book'),
            Document(
                Title(title, 'Test Author', ' '),
                Tag('tableofcontents'),
                *children,
            ),
        )

from latex.core.base.Tag import Tag
from latex.core.base.Texable import Texable


class DocumentSection(Texable):
    def __init__(self, tag_name: str, name: str, *children):
        Texable.__init__(self, Tag(tag_name, name), *children)

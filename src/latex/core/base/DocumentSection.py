from latex.core.base.Comment import Comment
from latex.core.base.Tag import Tag
from latex.core.base.Texable import Texable

TAG_NAME_TO_LEVEL = dict(
    part=0,
    chapter=1,
    section=2,
    subsection=3,
    subsubsection=4,
)


class DocumentSection(Texable):
    def __init__(self, tag_name: str, name: str, *children):
        level = TAG_NAME_TO_LEVEL[tag_name]
        line_width = 2 ** (6 - level)
        Texable.__init__(
            self, Comment.line(line_width), Tag(tag_name, name), *children
        )

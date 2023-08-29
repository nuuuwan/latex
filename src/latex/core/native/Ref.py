from latex.core.base.Join import Join
from latex.core.base.Str import Str
from latex.core.base.Tag import Tag
from latex.core.base.Texable import Texable
from latex.core.native.Italic import Italic


class Ref(Texable):
    def __init__(self, label_name: str):
        Texable.__init__(
            self,
            Join(
                Tag('autoref', label_name),
                Italic(
                    Str(", p."),
                    Tag('pageref', label_name),
                    Str(""),
                ),
            ),
        )

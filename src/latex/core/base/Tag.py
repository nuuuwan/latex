from latex.core.base.Texable import Texable


class Tag(Texable):
    def __init__(
        self, tag_name: str, tag_value: str = "", options: str = None
    ):
        assert tag_name

        if options and tag_value:
            tex = '\\%s[%s]{%s}' % (tag_name, options, tag_value)
        elif tag_value != "":
            tex = '\\%s{%s}' % (tag_name, tag_value)
        else:
            tex = '\\%s' % tag_name

        Texable.__init__(self, tex)

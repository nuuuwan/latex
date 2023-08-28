from latex.core.base.Texable import Texable


def render_tag_value(tag_value) -> str:
    assert tag_value

    if isinstance(tag_value, Texable):
        return '{%s}' % (tag_value.tex)

    if isinstance(tag_value, list):
        return ''.join([render_tag_value(x) for x in tag_value])

    return '{%s}' % (str(tag_value))


class Tag(Texable):
    def __init__(
        self, tag_name: str, tag_value: str = "", options: str = None
    ):
        assert tag_name

        tex = '\\%s' % (tag_name)

        if options:
            tex += '[%s]' % (options)

        if tag_value:
            tex += render_tag_value(tag_value)

        Texable.__init__(self, tex)

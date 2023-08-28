from latex.core.base.Texable import Texable


class Tag(Texable):
    def __init__(
        self, tag_name: str, tag_value: str = "", options: str = None
    ):
        assert tag_name

        tex = '\\%s' % (tag_name)

        if options:
            tex += '[%s]' % (options)

        if tag_value:
            if isinstance(tag_value, Texable):
                tex += '{%s}' % (tag_value.tex)
            elif isinstance(tag_value, str):
                tex += '{%s}' % (tag_value)
            elif isinstance(tag_value, list):
                for item in tag_value:
                    if isinstance(item, Texable):
                        tex += '{%s}' % (item.tex)
                    elif isinstance(item, str):
                        tex += '{%s}' % (item)
                    else:
                        raise TypeError(
                            'Tag value must be a Texable or a string'
                        )

        Texable.__init__(self, tex)

from latex.core.base.BeginEnd import BeginEnd
from latex.core.base.Tag import Tag
from latex.core.base.Texable import Texable


class Items(BeginEnd):
    def __init__(self, *item_texable_list: list):
        for item_texable in item_texable_list:
            assert isinstance(item_texable, Texable)
            assert len(item_texable.tex.strip()) > 0
        items = [
            Tag('item', item_texable.tex)
            for item_texable in item_texable_list
        ]
        BeginEnd.__init__(self, 'itemize', *items)

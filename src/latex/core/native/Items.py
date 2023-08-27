from latex.core.base.BeginEnd import BeginEnd
from latex.core.base.Tag import Tag


class Items(BeginEnd):
    def __init__(self, *inner: list):
        items = [Tag('item', item) for item in inner]
        BeginEnd.__init__(self, 'itemize', *items)

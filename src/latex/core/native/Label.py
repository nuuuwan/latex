from latex.core.base.Tag import Tag


class Label(Tag):
    def __init__(self, label_name: str):
        Tag.__init__(self, 'label', label_name)

from latex.core.base.Tag import Tag


class Index(Tag):
    def __init__(self, label_name: str):
        Tag.__init__(self, 'index', label_name)

from latex.core.base.Tag import Tag


class Ref(Tag):
    def __init__(self, label_name: str):
        Tag.__init__(self, 'ref', label_name)

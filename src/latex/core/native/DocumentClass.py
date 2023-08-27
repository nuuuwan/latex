from latex.core.base.Tag import Tag


class DocumentClass(Tag):
    def __init__(self, class_name: str, options: str = None):
        Tag.__init__(self, 'documentclass', class_name, options)

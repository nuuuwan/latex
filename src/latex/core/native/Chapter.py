from latex.core.base.DocumentSection import DocumentSection


class Chapter(DocumentSection):
    def __init__(self, name: str, *children):
        DocumentSection.__init__(self, "chapter", name, *children)

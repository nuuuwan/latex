from latex.core.base.DocumentSection import DocumentSection


class Section(DocumentSection):
    def __init__(self, name: str, *children):
        DocumentSection.__init__(self, "section", name, *children)

from latex.core.base.DocumentSection import DocumentSection


class Part(DocumentSection):
    def __init__(self, name: str, *children):
        DocumentSection.__init__(self, "part", name, *children)

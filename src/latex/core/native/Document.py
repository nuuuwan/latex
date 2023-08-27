from latex.core.base.BeginEnd import BeginEnd


class Document(BeginEnd):
    def __init__(self, *children: list):
        BeginEnd.__init__(self, 'document', *children)

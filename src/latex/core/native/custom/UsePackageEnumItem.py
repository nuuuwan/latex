from latex.core.base.Tag import Tag
from latex.core.base.Texable import Texable
from latex.core.native.UsePackage import UsePackage

MAX_LIST_DEPTH = 20


class UsePackageEnumItem(Texable):
    def __init__(self):
        children = [
            UsePackage('enumitem'),
            Tag('setlistdepth', MAX_LIST_DEPTH),
            Tag('renewlist', ['itemize', 'itemize', MAX_LIST_DEPTH]),
        ]
        for i in range(MAX_LIST_DEPTH):
            children.append(
                Tag(
                    'setlist',
                    'label=\\textbullet',
                    f'itemize,{i+1}',
                )
            )
        Texable.__init__(self, *children)

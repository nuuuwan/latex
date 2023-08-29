from latex.core.base.Comment import Comment
from latex.core.base.Dict import Dict
from latex.core.base.Tag import Tag
from latex.core.base.Texable import Texable
from latex.core.native.custom.UsePackageEnumItem import UsePackageEnumItem
from latex.core.native.Document import Document
from latex.core.native.DocumentClass import DocumentClass
from latex.core.native.Title import Title
from latex.core.native.UsePackage import UsePackage


class LatexBook(Texable):
    @staticmethod
    def packages() -> Texable:
        return Texable(
            Comment.title('Packages'),
            UsePackage('amssymb'),
            UsePackage('dirtytalk'),
            UsePackage('imakeidx'),
            Tag('makeindex'),
            UsePackage('hyperref'),
            Comment.line(),
            UsePackage('graphicx'),
            UsePackage('xcolor'),
            Tag('definecolor', ['slmaroon', 'RGB', '148,30,50']),
            Tag('definecolor', ['slorange', 'RGB', '223,117,0']),
            Tag('definecolor', ['slyellow', 'RGB', '247,183,24']),
            Tag('definecolor', ['slteal', 'RGB', '0,95,86']),
            Comment.line(),
            UsePackageEnumItem(),
            UsePackage(
                'geometry',
                Dict(
                    paperheight='11.5in',
                    paperwidth='8.5in',
                    left='1in',
                    right='1in',
                    top='0.8in',
                    bottom='0.8in',
                ),
            ),
            UsePackage('parskip', Dict(skip='0.1in', indent='0.0in')),
            UsePackage('fancyhdr'),
            Tag('pagestyle', 'fancy'),
            Tag('fancyhead', ' ', 'R'),
            Tag('fancyhead', ' ', 'L'),
            Tag('renewcommand', [Tag('headrulewidth'), '0pt']),
        )

    @staticmethod
    def document(title: str, author: str, *children) -> Texable:
        return Texable(
            Comment.title('Document'),
            Document(
                Title(title, author, ' '),
                Tag('tableofcontents'),
                *(list(children) + [Tag('printindex')]),
            ),
        )

    def __init__(self, title: str, author: str, *children):
        Texable.__init__(
            self,
            DocumentClass('book', '10pt, openany'),
            LatexBook.packages(),
            LatexBook.document(title, author, *children),
        )

from latex.core.base.Dict import Dict
from latex.core.base.Tag import Tag
from latex.core.base.Texable import Texable
from latex.core.native.Document import Document
from latex.core.native.DocumentClass import DocumentClass
from latex.core.native.Title import Title
from latex.core.native.UsePackage import UsePackage


class LatexBook(Texable):
    def __init__(self, title: str, author: str, *children):
        Texable.__init__(
            self,
            DocumentClass('book', '12pt, openany'),
            UsePackage('graphicx'),
            UsePackage('xcolor'),
            UsePackage('dirtytalk'),
            UsePackage('hyperref'),
            # UsePackage('libertine'),
            # UsePackage('fontenc', 'T1'),
            UsePackage('enumitem'),
            Tag('setlistdepth', 10),
            '\\renewlist{itemize}{itemize}{20}',
            '\\setlist[itemize,1]{label=\\textbullet}',
            '\\setlist[itemize,2]{label=\\textbullet}',
            '\\setlist[itemize,3]{label=\\textbullet}',
            '\\setlist[itemize,4]{label=\\textbullet}',
            '\\setlist[itemize,5]{label=\\textbullet}',
            '\\setlist[itemize,6]{label=\\textbullet}',
            '\\setlist[itemize,7]{label=\\textbullet}',
            '\\setlist[itemize,8]{label=\\textbullet}',
            '\\setlist[itemize,9]{label=\\textbullet}',
            '\\setlist[itemize,10]{label=\\textbullet}',
            UsePackage(
                'geometry',
                Dict(
                    paperheight='11.5in',
                    paperwidth='8.5in',
                    left='1.5in',
                    right='1.5in',
                    top='1in',
                    bottom='1in',
                ),
            ),
            UsePackage('parskip', Dict(skip='0.1in', indent='0.0in')),
            UsePackage('fancyhdr'),
            Tag('pagestyle', 'fancy'),
            Tag('fancyhead', ' ', 'R'),
            Tag('fancyhead', ' ', 'L'),
            '\\renewcommand{\\headrulewidth}{0pt}',
            Document(
                Title(title, author, ' '),
                Tag('tableofcontents'),
                *children,
            ),
        )

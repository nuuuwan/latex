from utils import File, Log

log = Log('latex')


class Texable:
    def __init__(self, *children: list):
        self.children = children

    @property
    def tex_lines(self) -> list[str]:
        lines = []
        for child in self.children:
            if isinstance(child, str):
                lines.append(child)
            elif isinstance(child, Texable):
                lines.extend(child.tex_lines)
            else:
                raise TypeError('child must be str or Texable')
        return lines

    @property
    def tex(self) -> str:
        return '\n'.join(self.tex_lines)

    def write(self, path):
        assert path.endswith('.tex')
        content = self.tex
        n = len(content)
        File(path).write(content)
        log.info(f'Wrote {path} ({n:,}B).')

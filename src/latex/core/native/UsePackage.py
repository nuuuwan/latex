from latex.core.base.Tag import Tag


class UsePackage(Tag):
    def __init__(self, package_name: str, options: str = None):
        Tag.__init__(self, 'usepackage', package_name, options)

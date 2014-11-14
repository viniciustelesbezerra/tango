class Category:

    def __init__(self, **kargs):
        self.name = kargs.get('name', 'x')

    def __unicode__(self):
        return self.name


class Page:

    def __init__(self, **kargs):
        self.category = kargs.get('category', 'x')
        self.title = kargs.get('title', 'x')
        self.url = kargs.get('url', 'x')
        self.views = kargs.get('views', 'x')

    def __unicode__(self):
        return self.title

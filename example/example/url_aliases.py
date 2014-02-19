class ExampleURLAliasModule(object):
    def resolve(self, path):
        if path == 'foo/':
            return 'bar/'
        # if path == 'foo/test/':
        #     return 'bar/test/'

    def reverse(self, path):
        if path == 'bar/':
            return 'foo/'
        # if path == 'bar/test/':
        #     return 'foo/test/'

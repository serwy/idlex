## Observable Dictionary
## Author: Roger D. Serwy
## Date:   2018-03-20
##
## 2018-08-15
## Modified for IDLEX for ExecDict


class ObservableDict(dict):

    def pre_get(self, key): pass
    def post_get(self, key, value): pass
    def pre_update(self, up, before): pass
    def post_update(self, up, before): pass
    def pre_del(self, before): pass
    def post_del(self, before): pass

    def __getitem__(self, key):
        self.pre_get(key)
        value = dict.__getitem__(self, key)
        self.post_get(key, value)
        return value

    def __setitem__(self, key, value):
        self.update({key: value})  # allow for multiple input changes

    def __delitem__(self, key):
        if key in self:   
            before = {key:self[key]}
        else:
            before = {}  # well, this will raise an error
        self.pre_del(before)
        dict.__delitem__(self, key)
        self.post_del(before)

    def update(self, *E, **F):
        updict = dict(*E, **F)
        before = {k:self[k] for k in updict if k in self}
        self.pre_update(updict, before)
        dict.update(self, updict)
        self.post_update(updict, before)

    def clear(self):
        before = self.copy()
        self.pre_del(before)
        dict.clear(self)
        self.post_del(before)


class ExecDict(ObservableDict):
    def __init__(self, *args, **kw):
        self.written = set()
        super().__init__(*args, **kw)

    def post_update(self, up, before):
        self.written.update(up.keys())


execdict = ExecDict()

if __name__ == '__main__':
    import types
    # basic tests
    o = ObservableDict()

    def pre_get(self, d):
        print('pre_get', d)

    def pre_update(d, b):
        print('pre_update', d, b)

    def post_del(b):
        print('post_del', b)

    o.pre_get = types.MethodType(pre_get, o)

    #o.pre_get = pre_get
    o.pre_update = pre_update
    o.post_del = post_del

    o['a'] = 123
    o['b'] = 456

    o.update(c=1, d=2)

    o['a']


def from_object(obj):
    if not hasattr(obj, '__dict__'):
        return obj
    d = {}
    for elem in vars(obj):
        d[elem] = from_object(getattr(obj, elem))
    return d


def to_object(d, cls):
    obj = cls()
    for elem in d:
        setattr(obj, elem, d[elem])
    return obj

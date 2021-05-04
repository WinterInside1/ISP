import inspect

from CustomSerializer.serialiser.function_serialiser.func_serializer import serialize_function


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


def serialize_obj(obj) -> dict:

    if obj is None:
        return None
    if isinstance(obj, (int, float, bool, str)):
        return obj
    if type(obj) == bytes:
        return list(obj)
    if isinstance(obj, (list, tuple)):
        lst = []
        for elem in obj:
            lst.append(serialize_obj(elem))
        return lst
    if type(obj) == dict:
        dct = {}
        for key in obj:
            dct[key] = serialize_obj(obj[key])
        return dct
    if inspect.isroutine(obj):
        return serialize_function(obj)
    dct = {}
    for key, val in inspect.getmembers(obj):
        if callable(val):
            if not "__" in val.__name__:
                dct[key] = serialize_function(val)
        else:
            dct[key] = serialize_obj(val)
    return dct


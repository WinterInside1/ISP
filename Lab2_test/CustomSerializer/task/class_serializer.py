import inspect
import json

from CustomSerializer.task.basic_serializer_creator import JsonSerializer
from CustomSerializer.task.func_serializer import serialize_function, deserialize_function, serialize_obj
from build.lib.CustomSerializer.task import class_serializer


def serialize_class(classes) -> dict:
    if classes.__class__.__name__ == "type":
        dct = {'__type__': 'class', '__class__': classes}
        for attr in dir(classes):
            print(attr)
            if not attr.startswith('__'):
                val = getattr(classes, attr)
                if "<class 'type'>" in str(val.__class__):
                    dct[attr] = serialize_class(val)
                elif "<class '__main__." in str(val.__class__):
                    dct[attr] = serialize_obj(val)
                elif callable(val):
                    if len(inspect.getfullargspec(val).args) > 1:
                        dct[attr] = serialize_function(val)
                else:
                    dct[attr] = val
        return dct


def deserialize_class(dct):
    vars = {}
    for attributed in dct:
        if not isinstance(dct[attributed], dict) and not attributed.startswith('__'):
            vars[attributed] = dct[attributed]
        elif isinstance(dct[attributed], dict) and not attributed.startswith('__'):
            if dct[attributed]['__type__'] == 'function':
                vars[attributed] = deserialize_function(dct[attributed])

    return type("User", (object,), vars)


def class_dumps(classes) -> str:
    dct = serialize_class(classes)
    return json.dumps(dct, indent=4)


def class_dump(classes, fp: str):
    s = class_dumps(classes)
    f = open(fp, "w")
    f.write(s)
    f.close()


def class_loads(s: str) -> object:
    dct = json.loads(s)
    func = deserialize_class(dct)
    return func


def class_load(fp: str):
    f = open(fp, "r")
    s = f.read()
    f.close()
    return class_loads(s)


class foo():

    def test(self,b,k):

        return b+k
    x = 76234


a = serialize_class(foo)
class_dump(foo, "/Users/dimabeliy/ISP/Lab2_test/test1.txt")

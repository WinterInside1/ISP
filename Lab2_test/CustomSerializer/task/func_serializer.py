import inspect
import json
import types

from CustomSerializer.task.my_parser import parse_loads, parse_dumps

ATTRIBUTES = [
    "__code__",
    "__name__",
    "__defaults__",
    "__closure__",
]


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
    if isinstance(obj, bytes):
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


def serialize_function(f: object) -> dict:
    d = {}
    for mem, val in inspect.getmembers(f):
        if mem in ATTRIBUTES:
            d[mem] = serialize_obj(val)
        if mem == "__code__":
            d["__globals__"] = {}
            glob = f.__globals__
            for name in val.co_names:
                if name == f.__name__:
                    d["__globals__"][name] = f.__name__
                elif not inspect.isbuiltin(name):
                    if name in glob:
                        if not inspect.ismodule(glob[name]):
                            d["__globals__"][name] = serialize_obj(glob[name])

    return d


def deserialize_co_consts(cc: list):
    lst = []
    for elem in cc:
        if type(elem) == dict and "co_code" in elem:
            lst.append(deserialize_codeobject(elem))
        else:
            lst.append(elem)
    return tuple(lst)


def deserialize_codeobject(code: dict):
    return types.CodeType(
        code['co_argcount'],
        code['co_posonlyargcount'],
        code['co_kwonlyargcount'],
        code['co_nlocals'],
        code['co_stacksize'],
        code['co_flags'],
        bytes(code['co_code']),
        deserialize_co_consts(code['co_consts']),
        tuple(code['co_names']),
        tuple(code['co_varnames']),
        code['co_filename'],
        code['co_name'],
        code['co_firstlineno'],
        bytes(code['co_lnotab']),
        tuple(code['co_freevars']),
        tuple(code['co_cellvars'])
    )


def deserialize_function(f: dict):
    code = f["__code__"]
    details = [deserialize_codeobject(code)]

    globs = {"__builtins__": __builtins__}
    for elem in f["__globals__"]:
        val = f["__globals__"][elem]
        if type(val) == dict and "__code__" in val:
            globs[elem] = deserialize_function(val)
        else:
            globs[elem] = val
    details.append(globs)

    for attr in ATTRIBUTES:
        if attr != "__code__":
            details.append(f[attr])

    result_func = types.FunctionType(*details)

    result_func.__globals__[result_func.__name__] = result_func

    return result_func


def function_dumps(func) -> str:
    dct = serialize_obj(func)
    return parse_dumps(dct)


def function_dump(func, fp: str):
    s = function_dumps(func)
    f = open(fp, "w")
    f.write(s)
    f.close()


def function_loads(s: str) -> object:
    dct = parse_loads(s)
    func = deserialize_function(dct)
    return func


def function_load(fp: str):
    f = open(fp, "r")
    s = f.read()
    f.close()
    return function_loads(s)

from CustomSerializer.task import class_serializer

CUR_PATH = ""
CODE_NAME = "Serialized_class.txt"


def SaveClass(c):
    class_serializer.class_dump(c, CUR_PATH + CODE_NAME)


def LoadClass():
    cl = class_serializer.class_load(CUR_PATH + CODE_NAME)
    return {cl}


class class1():
    pass


class class2():
    b = 1

    class a(object):
        k = [[2], 2, 2]

        def f(self):
            print('1')


class class3(object):
    a = None
    b = [1, (1, 5)]
    c = False
    d = "gds"
    e = {"a": 11, "b": {1: 21, 2: 22}}


def test_class():

    SaveClass(class3())

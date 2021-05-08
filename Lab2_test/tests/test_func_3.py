from CustomSerializer.task import func_serializer

CUR_PATH = ""
CODE_NAME = "Serialized_func_co_const.txt"


def SaveFunction(f):
    func_serializer.function_dump(f, CUR_PATH + CODE_NAME)


def LoadFunction():
    fc = func_serializer.function_load(CUR_PATH + CODE_NAME)
    return {fc}


def f_consts_answer(x: int) -> int:
    return 22 + x


def f_consts_co_const(x: int) -> int:
    a = 10
    b = 2
    k = "ashgf"
    return a + b + x + 10


def test_f_consts():
    SaveFunction(f_consts_co_const)
    x = 13
    for f in LoadFunction():
        assert f(x) == f_consts_answer(x)

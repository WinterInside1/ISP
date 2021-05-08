from CustomSerializer.task import func_serializer

CUR_PATH = ""
CODE_NAME = "Serialized_function.txt"

lol = 42



def SaveFunction(f):
    func_serializer.function_dump(f, CUR_PATH + CODE_NAME)


def LoadFunction():
    fc = func_serializer.function_load(CUR_PATH + CODE_NAME)
    return {fc}


def f_consts_answer(x: int) -> int:
    return 5542 + x


def f_consts(x: int) -> int:
    return x + lol + 5500


def f_recursion_answer(x: int) -> int:
    if x < 0: x = 0
    return (x * (x + 1)) // 2


def f_recursion(x: int) -> int:
    if x < 1: return 0
    return x + f_recursion(x - 1)


def f_connections_answer(s: str) -> str:
    return "Hello, Test! " + s


def f_connections_also(s: str) -> str:
    def f_connections_sub(): return "Test! "

    return f_connections_sub() + str(s)


def f_connections(s: str) -> str:
    return "Hello, " + f_connections_also(s)


def f_closures_answer(a, x):
    return a + x


def f_closures(a):
    def f_closures_sub(x):
        return a + x

    return f_closures_sub


def test_f_consts():
    SaveFunction(f_consts)
    x = 13
    for f in LoadFunction():
        assert f(x) == f_consts_answer(x)


def test_f_recursion():
    SaveFunction(f_recursion)
    x = 42
    for f in LoadFunction():
        assert f(x) == f_recursion_answer(x)


def test_f_connections():
    SaveFunction(f_connections)
    x = "Success!"
    for f in LoadFunction():
        assert f(x) == f_connections_answer(x)


def test_f_closures():
    SaveFunction(f_closures)
    a, b = 13, 42
    for f in LoadFunction():
        assert f(a)(b) == f_closures_answer(a, b)

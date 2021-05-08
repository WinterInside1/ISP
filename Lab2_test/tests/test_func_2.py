from CustomSerializer.task import func_serializer

CUR_PATH = ""
CODE_NAME = "Serialized_function.txt"


def check(f):
    assert f(1)(2) == 3


def test_code():
    f = func_serializer.function_load(CUR_PATH + CODE_NAME)
    check(f)

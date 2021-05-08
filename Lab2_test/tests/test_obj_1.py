from CustomSerializer.task.basic_serializer_creator import JsonSerializerCreator, PickleSerializerCreator, \
    YamlSerializerCreator, TomlSerializerCreator, from_object

CUR_PATH = ""
FILE_EXTENSION = ".txt"


class SubObjectParent:
    def __init__(self):
        self.a = 1
        self.b = "2"
        self.c = True


class SubObject(SubObjectParent):
    def __init__(self):
        SubObjectParent.__init__(self)
        self.d = {"a": 13, "top": "kek", "SPAM": "eggs"}


class Classes:
    num = int
    flt = float
    txt = str
    bul = bool
    arr = list
    tup = tuple
    sed = set
    dct = dict
    obj = object

    def init(self):
        self.num = 42
        self.flt = 3.1416
        self.txt = "Test kek test"
        self.bul = True
        self.arr = [13, 69, 420, 0]
        self.dct = {"a": 13, "42": "13", "top": "kek", "meh": ["eggs", "SPAM"]}
        self.obj = SubObject()

    def __str__(self):
        s = ""
        s += type(self).__name__
        s += "\n"
        for (k, v) in from_object(self).items():
            s += f"{k} = {v} \n"
        return s


Object = Classes()
Object.init()


def check_creator(creator):
    s = creator.dumps(Object)
    obj = creator.loads(s, Classes)
    assert str(obj) == str(Object)

    fn = CUR_PATH + type(creator).__name__ + FILE_EXTENSION
    s = creator.dump(Object, fn)
    obj = creator.load(fn, Classes)
    assert str(obj) == str(Object)


def test_json():
    creator = JsonSerializerCreator()
    check_creator(creator)


def test_pickle():
    creator = PickleSerializerCreator()
    check_creator(creator)


def test_yaml():
    creator = YamlSerializerCreator()
    check_creator(creator)


def test_toml():
    creator = TomlSerializerCreator()
    check_creator(creator)

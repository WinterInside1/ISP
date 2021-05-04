from CustomSerializer.Fabrics import IFabrics
from CustomSerializer.Fabrics.Fabrics import Fabrics
from CustomSerializer.Serialiser.BasicSerializers import JsonSerializer, TomlSerializer, YamlSerializer, \
    PickleSerializer


def basic_creator(ext: str) -> Fabrics:
    if ext == 'json':
        return JsonSerializerCreator()
    elif ext == 'pickle':
        return PickleSerializerCreator()
    elif ext == 'toml':
        return TomlSerializerCreator()
    elif ext == 'yaml':
        return YamlSerializerCreator()
    else:
        raise ValueError('Unknown extension: ' + ext)


class TomlSerializerCreator(Fabrics):

    def create_fabric(self) -> IFabrics:
        ser = TomlSerializer()
        return ser


class JsonSerializerCreator(Fabrics):

    def create_fabric(self) -> IFabrics:
        ser = JsonSerializer()
        return ser


class YamlSerializerCreator(Fabrics):

    def create_fabric(self) -> IFabrics:
        ser = YamlSerializer()
        return ser


class PickleSerializerCreator(Fabrics):

    def create_fabric(self) -> IFabrics:
        ser = PickleSerializer()
        return ser

    def loads(self, s: str, cls=None) -> object:
        ser = self.create_fabric()
        return ser.loads(s)

    def dump(self, obj: object, fp: str) -> None:
        s = self.dumps(obj)
        f = open(fp, "wb")
        f.write(s)
        f.close()

    def load(self, fp: str, cls=None) -> object:
        f = open(fp, "rb")
        s = f.read()
        f.close()
        return self.loads(s, cls)

import json
import pickle

import toml
import yaml

from CustomSerializer.konverter.fabrics import Fabrics, IFabrics


def from_object(obj):
    if not hasattr(obj, '__dict__'):
        return obj
    d = {}
    for elem in vars(obj):
        d[elem] = from_object(getattr(obj, elem))
    return d


class PickleSerializer(IFabrics):

    def dumps(self, obj: object) -> str:
        return pickle.dumps(obj)

    def loads(self, s: str) -> object:
        return pickle.loads(s)


class TomlSerializer(IFabrics):

    def dumps(self, obj: object) -> str:
        return toml.dumps(from_object(obj))

    def loads(self, s: str) -> object:
        return toml.loads(s)


class JsonSerializer(IFabrics):

    def dumps(self, obj: object) -> str:
        return json.dumps(from_object(obj), indent=4)

    def loads(self, s: str) -> object:
        return json.loads(s)


class YamlSerializer(IFabrics):

    def dumps(self, obj: object) -> str:
        return yaml.dump(from_object(obj), sort_keys=False)

    def loads(self, s: str) -> object:
        return yaml.full_load(s)


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

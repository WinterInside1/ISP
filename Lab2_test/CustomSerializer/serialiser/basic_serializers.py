import json
import pickle
import toml
import yaml
from CustomSerializer.fabrics.IFabrics import IFabrics
from CustomSerializer.serialiser.object_serialiser.ObjectConverter import *


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


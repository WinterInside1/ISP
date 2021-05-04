import IFabrics
from CustomSerializer.Serialiser.ObjectSerialiser.ObjectConverter import *


class Fabrics:

    def create_fabric(self) -> IFabrics:
        raise NotImplementedError

    def dumps(self, obj: object) -> str:
        serializer = self.create_fabric()
        return serializer.dumps(obj)

    def loads(self, s: str, cls=None) -> object:
        ser = self.create_fabric()
        if cls is not None:
            return to_object(ser.loads(s), cls)
        return ser.loads(s)

    def dump(self, obj: object, fp: str) -> None:
        f = open(fp, "w")
        f.write(self.dumps(obj))
        f.close()

    def load(self, fp: str, cls=None) -> object:
        f = open(fp, "r")
        s = f.read()
        f.close()
        return self.loads(s, cls)

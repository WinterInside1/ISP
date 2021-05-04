class IFabrics:
    def dumps(self, obj: object) -> str:
        raise NotImplementedError

    def loads(self, string: str) -> object:
        raise NotImplementedError

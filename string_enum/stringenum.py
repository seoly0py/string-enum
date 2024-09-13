from enum import StrEnum, auto


class StringEnum(StrEnum):

    def __eq__(self, val):
        if type(val) == str:
            return self.name == val
        else:
            return super().__eq__(val)

    def __hash__(self) -> int:
        return super().__hash__()


__all__ = ['StringEnum', 'auto']

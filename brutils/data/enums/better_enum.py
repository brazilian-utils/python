from enum import Enum, EnumMeta


class __MetaEnum(EnumMeta):
    @property
    def names(cls):
        return sorted(cls._member_names_)

    @property
    def values(cls):
        return sorted(x.value for x in cls._member_map_.values())


class BetterEnum(Enum, metaclass=__MetaEnum):
    pass

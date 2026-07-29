from brutils.data.enums.better_enum import BetterEnum


class MonthsEnum(BetterEnum):
    JANEIRO = 1
    FEVEREIRO = 2
    MARCO = 3
    ABRIL = 4
    MAIO = 5
    JUNHO = 6
    JULHO = 7
    AGOSTO = 8
    SETEMBRO = 9
    OUTUBRO = 10
    NOVEMBRO = 11
    DEZEMBRO = 12

    @property
    def month_name(self) -> str:
        if self == MonthsEnum.JANEIRO:
            return "janeiro"
        elif self == MonthsEnum.FEVEREIRO:
            return "fevereiro"
        elif self == MonthsEnum.MARCO:
            return "marco"
        elif self == MonthsEnum.ABRIL:
            return "abril"
        elif self == MonthsEnum.MAIO:
            return "maio"
        elif self == MonthsEnum.JUNHO:
            return "junho"
        elif self == MonthsEnum.JULHO:
            return "julho"
        elif self == MonthsEnum.AGOSTO:
            return "agosto"
        elif self == MonthsEnum.SETEMBRO:
            return "setembro"
        elif self == MonthsEnum.OUTUBRO:
            return "outubro"
        elif self == MonthsEnum.NOVEMBRO:
            return "novembro"
        else:
            return "dezembro"

    @classmethod
    def is_valid_month(cls, month: int) -> bool:
        """
        Checks if the given month value is valid.
        Args:
            month (int): The month to check.

        Returns:
            True if the month is valid, False otherwise.
        """
        return month in {month.value for month in MonthsEnum}

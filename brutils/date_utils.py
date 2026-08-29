import re
from datetime import datetime

import holidays
from num2words import num2words

from brutils.data.enums.months import MonthsEnum

DATE_REGEX = re.compile(r"^\d{2}/\d{2}/\d{4}$")


def is_holiday(target_date: datetime, uf: str = None) -> bool | None:
    """
    Checks if the given date is a national or state holiday in Brazil.

    This function takes a date as a `datetime` object and an optional UF (Unidade Federativa),
    returning a boolean value indicating whether the date is a holiday or `None` if the date or
    UF are invalid.

    The method does not handle municipal holidays.

    Args:
        target_date (datetime): The date to be checked.
        uf (str, optional): The state abbreviation (UF) to check for state holidays.
                            If not provided, only national holidays will be considered.

    Returns:
        bool | None: Returns `True` if the date is a holiday, `False` if it is not,
                     or `None` if the date or UF are invalid.

    Note:
        The function logic should be implemented using the `holidays` library.
        For more information, refer to the documentation at: https://pypi.org/project/holidays/

    Usage Examples:
        >>> from datetime import datetime
        >>> is_holiday(datetime(2024, 1, 1))
        True

        >>> is_holiday(datetime(2024, 1, 2))
        False

        >>> is_holiday(datetime(2024, 3, 2), uf="SP")
        False

        >>> is_holiday(datetime(2024, 12, 25), uf="RJ")
        True
    """
    if not isinstance(target_date, datetime):
        return None

    national_holidays = holidays.Brazil(years=target_date.year)
    valid_ufs = national_holidays.subdivisions

    if uf is not None and uf not in valid_ufs:
        return None

    if uf is None:
        return target_date in national_holidays

    state_holidays = holidays.Brazil(subdiv=uf, years=target_date.year)
    return target_date in state_holidays


def convert_date_to_text(date: str) -> str | None:
    """
    Converts a given date in Brazilian format (dd/mm/yyyy) to its textual representation.

    This function takes a date as a string in the format dd/mm/yyyy and converts it
    to a string with the date written out in Brazilian Portuguese, including the full
    month name and the year.

    Args:
        date (str): The date to be converted into text. Expected format: dd/mm/yyyy.

    Returns:
        str | None: A string with the date written out in Brazilian Portuguese,
        or None if the date is invalid.

    """
    if not DATE_REGEX.match(date):
        return None

    try:
        dt = datetime.strptime(date, "%d/%m/%Y")
    except ValueError:
        return None

    day, month, year = dt.day, dt.month, dt.year

    day_str = "Primeiro" if day == 1 else num2words(day, lang="pt")
    month_enum = MonthsEnum(month)
    year_str = num2words(year, lang="pt")

    return f"{day_str.capitalize()} de {month_enum.month_name} de {year_str}"

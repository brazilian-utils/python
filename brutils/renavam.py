RENAVAM_DV_WEIGHTS = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3]


def _validate_renavam_format(renavam: str):
    if not isinstance(renavam, str):
        return False
    if len(renavam) != 11 or not renavam.isdigit():
        return False
    if len(set(renavam)) == 1:
        return False
    return True


def _sum_weighted_digits(renavam: str) -> int:
    base_digits = [int(d) for d in renavam[:-1][::-1]]
    return sum(x * y for x, y in zip(base_digits, RENAVAM_DV_WEIGHTS))


def _calculate_renavam_dv(renavam: str):
    weighted_sum = _sum_weighted_digits(renavam)
    dv = 11 - (weighted_sum % 11)
    return 0 if dv >= 10 else dv


def is_valid_renavam(renavam: str) -> bool:
    """
    Validates the Brazilian vehicle registration number (RENAVAM).

    This function takes a RENAVAM string and checks if it is valid.
    A valid RENAVAM consists of exactly 11 digits, with the last digit as
    a verification digit calculated from the previous 10 digits.

    Args:
        renavam (str): The RENAVAM string to be validated.

    Returns:
        bool: True if the RENAVAM is valid, False otherwise.

    Example:
        >>> is_valid_renavam('86769597308')
        True
        >>> is_valid_renavam('12345678901')
        False
        >>> is_valid_renavam('1234567890a')
        False
        >>> is_valid_renavam('12345678 901')
        False
        >>> is_valid_renavam('12345678')
        False
        >>> is_valid_renavam('')
        False
    """
    if not _validate_renavam_format(renavam):
        return False

    return _calculate_renavam_dv(renavam) == int(renavam[-1])

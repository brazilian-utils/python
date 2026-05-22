import string
from itertools import chain
from random import choice, randint

# Mapeamento alfanumérico: A=10, B=11, ..., Z=35
_CHAR_VALUES = {c: i + 10 for i, c in enumerate(string.ascii_uppercase)}

# FORMATTING
############


def sieve(dirty: str) -> str:
    """
    Removes specific symbols from a CNPJ string.

    Args:
        cnpj (str): The CNPJ string containing symbols to be removed.

    Returns:
        str: A new string with the specified symbols removed.

    Example:
        >>> sieve("12.345/6789-01")
        "12345678901"
    """
    return "".join(filter(lambda char: char not in "./-", dirty))


def remove_symbols(dirty: str) -> str:
    """Alias for sieve()."""
    return sieve(dirty)


def display(cnpj: str) -> str | None:
    """
    Formats a CNPJ string for visual display (legacy, numeric only).

    .. note::
       This method should not be used in new code and is only provided for
       backward compatibility. Use format_cnpj() instead.
    """
    if not cnpj.isdigit() or len(cnpj) != 14 or len(set(cnpj)) == 1:
        return None
    return "{}.{}.{}/{}-{}".format(
        cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:]
    )


def format_cnpj(cnpj: str) -> str | None:
    """
    Formats a CNPJ string for visual display.

    Supports both the classic numeric format and the new alphanumeric format
    introduced by RFB Nota Técnica 49/2024 (effective July 2026).

    Args:
        cnpj (str): The CNPJ string to be formatted (14 characters, no symbols).

    Returns:
        str: The formatted CNPJ if valid, None otherwise.

    Example:
        >>> format_cnpj("03560714000142")
        '03.560.714/0001-42'
        >>> format_cnpj("B3S30714000142")
        'B3.S30.714/0001-42'
    """
    if not is_valid(cnpj):
        return None
    return "{}.{}.{}/{}-{}".format(
        cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:14]
    )


# OPERATIONS
############


def _char_to_val(c: str) -> int:
    """
    Converts a CNPJ character to its numeric value for checksum calculation.

    Digits map to their integer value; uppercase letters map to 10-35
    (A=10, B=11, ..., Z=35), as defined by RFB Nota Técnica 49/2024.

    Args:
        c (str): A single character (digit or uppercase letter).

    Returns:
        int: The numeric value of the character.
    """
    if c.isdigit():
        return int(c)
    return _CHAR_VALUES[c.upper()]


def _is_valid_chars(cnpj: str) -> bool:
    """
    Checks if all characters in a CNPJ are valid (digits or uppercase letters).

    Args:
        cnpj (str): The CNPJ string to check.

    Returns:
        bool: True if all characters are valid, False otherwise.
    """
    return all(c.isdigit() or c.upper() in _CHAR_VALUES for c in cnpj)


def _hashdigit(cnpj: str, position: int) -> int:
    """
    Calculates the checksum digit at the given position for the provided CNPJ.

    Supports both numeric and alphanumeric CNPJs per RFB Nota Técnica 49/2024.

    Args:
        cnpj (str): The CNPJ string.
        position (int): The position of the checksum digit (13 or 14).

    Returns:
        int: The calculated checksum digit.
    """
    weightgen = chain(range(position - 8, 1, -1), range(9, 1, -1))
    val = sum(_char_to_val(c) * w for c, w in zip(cnpj, weightgen)) % 11
    return 0 if val < 2 else 11 - val


def _checksum(basenum: str) -> str:
    """
    Calculates the verifying checksum digits for a given CNPJ base number.

    Supports both numeric and alphanumeric base numbers.

    Args:
        basenum (str): The 12-character CNPJ base number.

    Returns:
        str: The two verifying checksum digits.
    """
    d1 = str(_hashdigit(basenum, 13))
    d2 = str(_hashdigit(basenum + d1, 14))
    return d1 + d2


def validate(cnpj: str) -> bool:
    """
    Validates a CNPJ by comparing its verifying checksum digits to its base.

    Supports both the classic numeric format and the new alphanumeric format
    introduced by RFB Nota Técnica 49/2024 (effective July 2026).

    Args:
        cnpj (str): The CNPJ to be validated (14 characters, no symbols).

    Returns:
        bool: True if valid, False otherwise.

    Example:
        >>> validate("03560714000142")
        True
        >>> validate("00111222000133")
        False
        >>> validate("B3S30714000142")
        True

    .. note::
       This method should not be used in new code and is only provided for
       backward compatibility.
    """
    if (
        not isinstance(cnpj, str)
        or len(cnpj) != 14
        or not _is_valid_chars(cnpj)
        or len(set(cnpj.upper())) == 1
    ):
        return False
    return all(_hashdigit(cnpj, i + 13) == int(cnpj[12 + i]) for i in range(2))


def is_valid(cnpj: str) -> bool:
    """
    Returns whether the verifying checksum digits of the given CNPJ match
    its base number.

    Supports both the classic numeric format and the new alphanumeric format
    introduced by RFB Nota Técnica 49/2024 (effective July 2026).

    This function does not verify the existence of the CNPJ; it only
    validates the format of the string.

    Args:
        cnpj (str): The CNPJ to be validated (14 characters, no symbols).

    Returns:
        bool: True if the checksum digits match the base number,
              False otherwise.

    Example:
        >>> is_valid("03560714000142")
        True
        >>> is_valid("00111222000133")
        False
        >>> is_valid("B3S30714000142")
        True
    """
    return isinstance(cnpj, str) and validate(cnpj)


def generate(branch: int = 1, alphanumeric: bool = False) -> str:
    """
    Generates a random valid CNPJ string.

    Args:
        branch (int): An optional branch number (default: 1).
        alphanumeric (bool): If True, generates a new alphanumeric CNPJ
                             per RFB Nota Técnica 49/2024. Default: False.

    Returns:
        str: A randomly generated valid CNPJ string.

    Example:
        >>> generate()
        "30180536000105"
        >>> generate(alphanumeric=True)
        "B3S30714000142"
    """
    branch %= 10000
    branch += int(branch == 0)
    branch = str(branch).zfill(4)

    if alphanumeric:
        charset = string.digits + string.ascii_uppercase
        base = "".join(choice(charset) for _ in range(8)) + branch
        # Ensure at least one letter in the base (distinguishes from numeric)
        if base[:8].isdigit():
            pos = randint(0, 7)
            base = base[:pos] + choice(string.ascii_uppercase) + base[pos + 1 :]
    else:
        base = str(randint(0, 99999999)).zfill(8) + branch

    return base + _checksum(base)

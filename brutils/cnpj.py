from itertools import chain
from random import choice, randint
from string import ascii_uppercase, digits

# ---------------------------------------------------------------------------
# Conjunto de caracteres válidos para o CNPJ (dígitos + letras maiúsculas).
# A Receita Federal passa a emitir CNPJs alfanuméricos a partir de julho/2026,
# conforme Nota Técnica Conjunta COCAD/SUARA/RFB nº 49/2024.
#
# Regra de conversão (ASCII - 48):
#   '0'...'9'  →  0...9
#   'A'...'Z'  →  17...42
#
# Os dois últimos caracteres (dígitos verificadores) permanecem sempre
# numéricos ('0'...'9').
# ---------------------------------------------------------------------------

_VALID_CHARS = set(digits + ascii_uppercase)
_ALPHANUM_CHARS = digits + ascii_uppercase


# FORMATTING
############


def sieve(dirty: str) -> str:
    """
    Removes specific symbols from a CNPJ string.

    Removes all occurrences of '.', '/' and '-' from the given string,
    returning a raw alphanumeric CNPJ string.

    Args:
        dirty (str): The CNPJ string containing symbols to be removed.

    Returns:
        str: A new string with the specified symbols removed.

    Example:
        >>> sieve("12.ABC.345/01DE-35")
        "12ABC34501DE35"
        >>> sieve("12.345.678/0001-42")
        "12345678000142"

    .. note::
       This method should not be used in new code and is only provided for
       backward compatibility.
    """
    return "".join(filter(lambda char: char not in "./-", dirty))


def remove_symbols(dirty: str) -> str:
    """
    Alias for :func:`sieve` with a more descriptive name.

    Args:
        dirty (str): The dirty string containing symbols to be removed.

    Returns:
        str: A new string with the specified symbols removed.

    Example:
        >>> remove_symbols("12.ABC.345/01DE-35")
        "12ABC34501DE35"
    """
    return sieve(dirty)


def display(cnpj: str) -> str | None:
    """
    Formats a raw CNPJ string (numeric or alphanumeric) for visual display.

    Args:
        cnpj (str): A 14-character raw CNPJ string (no symbols).

    Returns:
        str | None: The formatted CNPJ (``XX.XXX.XXX/XXXX-DD``) if valid,
        ``None`` otherwise.

    Example:
        >>> display("12ABC34501DE35")
        "12.ABC.345/01DE-35"
        >>> display("12345678000142")
        "12.345.678/0001-42"

    .. note::
       This method should not be used in new code and is only provided for
       backward compatibility.
    """
    if not _is_valid_format(cnpj):
        return None
    return "{}.{}.{}/{}-{}".format(
        cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:]
    )


def format_cnpj(cnpj: str) -> str | None:
    """
    Formats a CNPJ string (numeric or alphanumeric) for visual display.

    Args:
        cnpj (str): A 14-character raw CNPJ string (no symbols).

    Returns:
        str | None: The formatted CNPJ (``XX.XXX.XXX/XXXX-DD``) if valid,
        ``None`` otherwise.

    Example:
        >>> format_cnpj("12ABC34501DE35")
        '12.ABC.345/01DE-35'
        >>> format_cnpj("03560714000142")
        '03.560.714/0001-42'
        >>> format_cnpj("98765432100100")
        None
    """
    if not is_valid(cnpj):
        return None
    return "{}.{}.{}/{}-{}".format(
        cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:14]
    )


# OPERATIONS
############


def _char_value(char: str) -> int:
    """
    Converts a CNPJ character to its numeric value using the RFB rule
    (ASCII ordinal − 48).

    Args:
        char (str): A single character ('0'–'9' or 'A'–'Z').

    Returns:
        int: The numeric value of the character.

    Example:
        >>> _char_value('0')
        0
        >>> _char_value('9')
        9
        >>> _char_value('A')
        17
        >>> _char_value('Z')
        42
    """
    return ord(char) - 48


def _is_valid_format(cnpj: str) -> bool:
    """
    Returns True if *cnpj* has the correct raw format: 14 characters, each
    one in ``[0-9A-Z]``, the last two being digits, and not all identical.
    """
    if not isinstance(cnpj, str) or len(cnpj) != 14:
        return False
    if not all(c in _VALID_CHARS for c in cnpj):
        return False
    if not cnpj[12:].isdigit():
        return False
    if len(set(cnpj)) == 1:
        return False
    return True


def validate(cnpj: str) -> bool:
    """
    Validates a CNPJ by verifying its checksum digits.

    Supports both the classic all-numeric format and the new alphanumeric
    format introduced by Receita Federal (Nota Técnica 49/2024, effective
    July 2026).

    Args:
        cnpj (str): The raw 14-character CNPJ string (no symbols).

    Returns:
        bool: ``True`` if the checksum digits match the base number,
        ``False`` otherwise.

    Example:
        >>> validate("03560714000142")
        True
        >>> validate("12ABC34501DE35")
        True
        >>> validate("00111222000133")
        False

    .. note::
       This method should not be used in new code and is only provided for
       backward compatibility.
    """
    if not _is_valid_format(cnpj):
        return False
    return all(
        _hashdigit(cnpj, i + 13) == int(v) for i, v in enumerate(cnpj[12:])
    )


def is_valid(cnpj: str) -> bool:
    """
    Returns whether the verifying checksum digits of the given CNPJ match
    its base number.

    Supports both the classic all-numeric format and the new alphanumeric
    format introduced by Receita Federal (Nota Técnica 49/2024, effective
    July 2026).

    This function does not verify the *existence* of the CNPJ; it only
    validates the format and checksum.

    Args:
        cnpj (str): The raw 14-character CNPJ string (no symbols).

    Returns:
        bool: ``True`` if the checksum digits match the base number,
        ``False`` otherwise.

    Example:
        >>> is_valid("03560714000142")
        True
        >>> is_valid("12ABC34501DE35")
        True
        >>> is_valid("00111222000133")
        False
    """
    return isinstance(cnpj, str) and validate(cnpj)


def generate(branch: int = 1, alphanumeric: bool = False) -> str:
    """
    Generates a random valid CNPJ string.

    Args:
        branch (int): An optional branch (filial) number, defaults to 1.
            Must be between 0 and 9999.
        alphanumeric (bool): When ``True``, generates a CNPJ using the new
            alphanumeric format (RFB Nota Técnica 49/2024). Defaults to
            ``False`` for backward compatibility.

    Returns:
        str: A randomly generated valid CNPJ string (14 raw characters).

    Example:
        >>> len(generate())
        14
        >>> is_valid(generate())
        True
        >>> is_valid(generate(alphanumeric=True))
        True
    """
    branch %= 10000
    branch += int(branch == 0)
    branch = str(branch).zfill(4)

    if alphanumeric:
        base = "".join(choice(_ALPHANUM_CHARS) for _ in range(8)) + branch
    else:
        base = str(randint(0, 99999999)).zfill(8) + branch

    return base + _checksum(base)


def _hashdigit(cnpj: str, position: int) -> int:
    """
    Calculates the checksum digit at *position* for the provided CNPJ.

    Uses the RFB character-value rule (``ord(char) − 48``) so that the
    function works for both numeric and alphanumeric CNPJs.

    Args:
        cnpj (str): The CNPJ string. Must contain all characters before
            *position*.
        position (int): The 1-based position of the checksum digit (13 or 14).

    Returns:
        int: The calculated checksum digit (0–9).

    Example:
        >>> _hashdigit("03560714000142", 13)
        4
        >>> _hashdigit("12ABC34501DE35", 13)
        3
    """
    weightgen = chain(range(position - 8, 1, -1), range(9, 1, -1))
    val = (
        sum(_char_value(char) * weight for char, weight in zip(cnpj, weightgen))
        % 11
    )
    return 0 if val < 2 else 11 - val


def _checksum(basenum: str) -> str:
    """
    Calculates the two verifying checksum digits for a CNPJ base number.

    Works for both numeric and alphanumeric base numbers.

    Args:
        basenum (str): The 12-character base CNPJ (no checksum digits).

    Returns:
        str: The two checksum digits (always numeric, '00'–'99').

    Example:
        >>> _checksum("123456789012")
        "30"
        >>> _checksum("12ABC34501DE")
        "35"
    """
    d1 = str(_hashdigit(basenum, 13))
    d2 = str(_hashdigit(basenum + d1, 14))
    return d1 + d2

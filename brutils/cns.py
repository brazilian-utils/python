import re
from random import randint

# CNS numbers are 15 digits long. The check digit(s) are calculated as a
# weighted sum of the digits, using decreasing weights starting at 15.
WEIGHTS = list(range(15, 0, -1))

# Definitive CNS: starts with 1 or 2, followed by 10 digits (the 11-digit
# block is derived from a PIS/PASEP-like base), then a fixed "00" segment,
# a flag digit ("0" or "1") and the check digit.
_DEFINITIVE_REGEX = re.compile(r"^[12]\d{10}00[01]\d$")

# Provisional CNS: starts with 7, 8 or 9, followed by 13 digits and a check
# digit, all 15 digits taking part in the weighted sum.
_PROVISIONAL_REGEX = re.compile(r"^[789]\d{14}$")


# FORMATTING
############


def remove_symbols(cns: str) -> str:
    """
    Remove formatting symbols from a CNS.

    This function takes a CNS (Cartão Nacional de Saúde) string with
    formatting symbols and returns a cleaned version with no symbols.

    Args:
        cns (str): A CNS string that may contain formatting symbols.

    Returns:
        str: A cleaned CNS string with no formatting symbols.

    Example:
        >>> remove_symbols("898 0032 6314 4970")
        '898003263144970'
        >>> remove_symbols("898003263144970")
        '898003263144970'
    """
    return cns.replace(" ", "").replace(".", "").replace("-", "")


def format_cns(cns: str) -> str | None:
    """
    Return the correct four-character suffix string of a definitive CNS,
    derived from its first eleven digits.

    It is used by both `is_valid` and `_generate_definitive`, so validating
    and generating a definitive CNS follow the same rule, which keeps them consistent.

    Args:
        base (str): The first eleven digits of a definitive CNS (starting with 1 or 2).

    Returns:
        str: A four-character string with the segment ("000" or "001") and the check digit.

    Example:
        >>> _definitive_suffix("16124337445")
        '0004'
    """

    if not is_valid(cns):
        return None

    return "{} {} {} {}".format(cns[:3], cns[3:7], cns[7:11], cns[11:15])


# OPERATIONS
############


def _definitive_suffix(value: str) -> str:
    """
    Return the four-character suffix of a definitive CNS, derived from its
    first eleven digits: the three-digit segment ("000", or "001" in the
    special case) followed by the check digit.

    It is used by both `is_valid` and `_generate_definitive`, so validating
    and generating a definitive CNS follow the same rule.

    Args:
        base (str): The first eleven digits of a definitive CNS (starting
            with 1 or 2).

    Returns:
        str: A four-character string with the segment and the check digit.

    Example:
        >>> _definitive_suffix("16124337445")
        '0004'
    """

    soma = _weighted_sum(value)
    resto = soma % 11
    dv = 11 - resto

    if dv == 11:
        dv = 0
        seq = "000"
    elif dv == 10:
        # Special case: recalculate with an offset of 2 and mark the
        # sequence segment accordingly.
        soma += 2
        dv = 11 - (soma % 11)
        seq = "001"
    else:
        seq = "000"

    return f"{seq}{dv}"


def is_valid(cns: str) -> bool:
    """
    Returns whether or not the given `CNS` is valid.

    It does not verify if the CNS actually exists.

    References:
        - https://gist.github.com/dudanogueira/7af722477c33bd4bb85843cf0e035b77
        - https://integracao.esusaps.bridge.ufsc.tech/v211/docs/algoritmo_CNS.html

    Args:
        cns (str): CNS number as a string of proper length.

    Returns:
        bool: True if CNS is valid, False otherwise.

    Example:
        >>> is_valid("161243374450004")
        True
        >>> is_valid("905885616557480")
        True
        >>> is_valid("123456789012345")
        False
    """

    if not isinstance(cns, str) or not cns.isdigit() or len(cns) != 15:
        return False

    if not (_DEFINITIVE_REGEX.match(cns) or _PROVISIONAL_REGEX.match(cns)):
        return False

    if cns[0] == "1" or cns[0] == "2":
        prefix = cns[:11]
        suffix = cns[-4:]
        verification = _definitive_suffix(prefix)
        return verification == suffix
    else:
        return _weighted_sum(cns) % 11 == 0


def generate(is_final: bool = True) -> str:
    """
    Generate a random valid Brazilian CNS number.

    Args:
        is_final (bool): Whether to generate a "definitive" CNS (starting
            with 1 or 2) or a "provisional" one (starting with 7, 8 or 9).
            Defaults to True (definitive).

    Returns:
        str: A randomly generated valid CNS number as a string.

    Example:
        >>> generate()
        '161243374450004'
        >>> generate(is_final=False)
        '905885616557480'
    """

    return _generate_definitive() if is_final else _generate_provisional()


def _weighted_sum(digits: str) -> int:
    """
    Calculate the weighted sum of the given digits, using decreasing
    weights starting at 15 (i.e. the first digit is always weighted 15,
    regardless of the total length of `digits`).

    Args:
        digits (str): A string of digits.

    Returns:
        int: The weighted sum of the digits.
    """
    return sum(int(digit) * weight for digit, weight in zip(digits, WEIGHTS))


def _generate_definitive() -> str:
    """
    Generate a random valid "definitive" CNS (starting with 1 or 2).

    Returns:
        str: A randomly generated valid definitive CNS number as a string.
    """
    base = str(randint(1, 2)) + str(randint(0, 9999999999)).zfill(10)
    final = _definitive_suffix(base)
    return f"{base}{final}"


def _generate_provisional() -> str:
    """
    Generate a random valid "provisional" CNS (starting with 7, 8 or 9).

    Returns:
        str: A randomly generated valid provisional CNS number as a string.
    """
    while True:
        base = str(randint(7, 9)) + str(randint(0, 10**13 - 1)).zfill(13)
        dv = (11 - (_weighted_sum(base) % 11)) % 11

        # A check digit of 10 cannot be represented by a single digit, so
        # a new base must be generated in that (rare) case.
        if dv != 10:
            return f"{base}{dv}"

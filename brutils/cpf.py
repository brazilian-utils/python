from random import randint

# FORMATTING
############


def sieve(dirty: str) -> str:
    """
    Removes specific symbols from a CPF (Brazilian Individual Taxpayer Number)
    string.

    This function takes a CPF string as input and removes all occurrences of
    the '.', '-' characters from it.

    Args:
        cpf (str): The CPF string containing symbols to be removed.

    Returns:
        str: A new string with the specified symbols removed.

    Example:
        >>> sieve("123.456.789-01")
        '12345678901'
        >>> sieve("987-654-321.01")
        '98765432101'

    .. note::
       This method should not be used in new code and is only provided for
       backward compatibility.
    """

    return "".join(filter(lambda char: char not in ".-", dirty))


def remove_symbols(dirty: str) -> str:
    """
    Alias for the `sieve` function. Better naming.

    Args:
        cpf (str): The CPF string containing symbols to be removed.

    Returns:
        str: A new string with the specified symbols removed.
    """

    return sieve(dirty)


def display(cpf: str) -> str:
    """
    Format a CPF for display with visual aid symbols.

    This function takes a numbers-only CPF string as input and adds standard
    formatting visual aid symbols for display.

    Args:
        cpf (str): A numbers-only CPF string.

    Returns:
        str: A formatted CPF string with standard visual aid symbols
            or None if the input is invalid.

    Example:
        >>> display("12345678901")
        "123.456.789-01"
        >>> display("98765432101")
        "987.654.321-01"

    .. note::
       This method should not be used in new code and is only provided for
       backward compatibility.
    """

    if not cpf.isdigit() or len(cpf) != 11 or len(set(cpf)) == 1:
        return None

    return "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])


def format_cpf(cpf: str) -> str:
    """
    Format a CPF for display with visual aid symbols.

    This function takes a numbers-only CPF string as input and adds standard
    formatting visual aid symbols for display.

    Args:
        cpf (str): A numbers-only CPF string.

    Returns:
        str: A formatted CPF string with standard visual aid symbols or None
        if the input is invalid.

    Example:
        >>> format_cpf("82178537464")
        '821.785.374-64'
        >>> format_cpf("55550207753")
        '555.502.077-53'
    """

    if not is_valid(cpf):
        return None

    return "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:11])


# OPERATIONS
############


def validate(cpf: str) -> bool:
    """
    Validate the checksum digits of a CPF.

    This function checks whether the verifying checksum digits of the given CPF
    match its base number. The input should be a digit string of the proper
    length.

    Args:
        cpf (str): A numbers-only CPF string.

    Returns:
        bool: True if the checksum digits are valid, False otherwise.

    Example:
        >>> validate("82178537464")
        True
        >>> validate("55550207753")
        True

    .. note::
       This method should not be used in new code and is only provided for
       backward compatibility.
    """

    if not cpf.isdigit() or len(cpf) != 11 or len(set(cpf)) == 1:
        return False

    return all(_hashdigit(cpf, i + 10) == int(v) for i, v in enumerate(cpf[9:]))


def is_valid(cpf: str) -> bool:
    """
    Returns whether or not the verifying checksum digits of the given `˜CPF`
    match its base number.

    This function does not verify the existence of the CPF; it only
    validates the format of the string.

    Args:
        cpf (str): The CPF to be validated, a 11-digit string

    Returns:
        bool: True if the checksum digits match the base number,
              False otherwise.

    Example:
        >>> is_valid("82178537464")
        True
        >>> is_valid("55550207753")
        True
    """

    return isinstance(cpf, str) and validate(cpf)


def generate() -> str:
    """
    Generate a random valid CPF digit string.

    This function generates a random valid CPF string.

    Returns:
        str: A random valid CPF string.

    Example:
        >>> generate()
        "10895948109"
        >>> generate()
        "52837606502"
    """

    base = str(randint(1, 999999998)).zfill(9)

    return base + _checksum(base)


def _hashdigit(cpf: str, position: int) -> int:
    """
    Compute the given position checksum digit for a CPF.

    This function computes the specified position checksum digit for the CPF
    input.
    The input needs to contain all elements previous to the position, or the
    computation will yield the wrong result.

    Args:
        cpf (str): A CPF string.
        position (int): The position to calculate the checksum digit for.

    Returns:
        int: The calculated checksum digit.

    Example:
        >>> _hashdigit("52599927765", 11)
        5
        >>> _hashdigit("52599927765", 10)
        6
    """

    val = (
        sum(
            int(digit) * weight
            for digit, weight in zip(cpf, range(position, 1, -1))
        )
        % 11
    )

    return 0 if val < 2 else 11 - val


def _checksum(basenum: str) -> str:
    """
    Compute the checksum digits for a given CPF base number.

    This function calculates the checksum digits for a given CPF base number.
    The base number should be a digit string of adequate length.

    Args:
        basenum (str): A digit string of adequate length.

    Returns:
        str: The calculated checksum digits.

    Example:
        >>> _checksum("335451269")
        '51'
        >>> _checksum("382916331")
        '26'
    """

    verifying_digits = str(_hashdigit(basenum, 10))
    verifying_digits += str(_hashdigit(basenum + verifying_digits, 11))

    return verifying_digits

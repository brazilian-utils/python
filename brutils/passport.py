import random
import re
import string


def is_valid(passport: str) -> bool:
    """
    Checks if a Brazilian passport number is valid.

    To be considered valid, the input must be a string containing exactly two alphabetical characters followed by exactly six numerical digits.

    This function does not verify is the input is a real passport number, as there are no checksums for the Brazilian passport.

    Args:
        passport (str): The string containing the passport number to be checked.

    Returns:
        bool: True if the passport number is valid (2 letters followed by 6 digits). False otherwise.

    Example:
        >>> is_valid("Ab123456")
        True
        >>> is_valid("12345678")
        False
        >>> is_valid("DC-221345")
        False
    """

    if not isinstance(passport, str):
        return False

    pattern = re.compile("^[A-Z]{2}[0-9]{6}$")
    match = re.match(pattern, passport)
    return match is not None


def remove_symbols(passport: str) -> str:
    """
    Removes symbols ('-', '.', and whitespaces) from a passport number.

    This function takes a passport number string as input and removes all occurrences of
    the '.', '-', and whitespace characters from it.

    Args:
        passport (str): The string containing a passport number

    Returns:
        str: The passport numbers with dashes (-), dots (.), and whitespaces ( ) removed.

    Example:
        >>> remove_symbols("Ab123456")
        Ab123456
        >>> remove_symbols("Ab-123456")
        Ab123456
        >>> remove_symbols("Ab -. 123456")
        Ab123456
    """

    return "".join(filter(lambda c: c not in ".- ", passport))


def format_passport(passport: str) -> str | None:
    """
    Formats a Brazilian passport number for display.

    This function takes a string representing a valid passport number and returns it formatted (uppercase, without symbols).

    Args:
        passport (str | None): A Brazilian passport number (lower or uppercase, possibly including symbols)

    Returns:
        str: The formatted passport number (uppercase, without symbols) or None if the input is invalid

    Example:
        >>> format_passport("Ab123456")
        AB123456
        >>> format_passport("Ab-123456")
        AB123456
        >>> format_passport("111111")
        None
    """

    passport = remove_symbols(passport.upper())

    return passport if is_valid(passport) else None


def generate() -> str:
    """
    Generate a random valid Brazilian passport number string.

    This function generates a random Brazilian passport number string.

    Returns:
        str: A random valid passport number string.

    Example:
        >>> generate()
        "RY393097"
        >>> generate()
        "ZS840088"
    """

    letters = "".join(random.choices(string.ascii_uppercase, k=2))
    digits = "".join(random.choices(string.digits, k=6))

    return f"{letters}{digits}"

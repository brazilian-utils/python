import re


def is_valid(email: str) -> bool:
    """
    Check if a string corresponds to a valid email address.

    Args:
        email (str): The input string to be checked.

    Returns:
        bool: True if email is a valid email address, False otherwise.

    Example:
        >>> is_valid("brutils@brutils.com")
        True
        >>> is_valid("invalid-email@brutils")
        False

    .. note::
        The rules for validating an email address generally follow the
        specifications defined by RFC 5322 (updated by RFC 5322bis),
        which is the widely accepted standard for email address formats.
    """

    pattern = re.compile(
        r"^(?![.])[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    )
    return isinstance(email, str) and re.match(pattern, email) is not None

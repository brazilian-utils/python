import json
import os
import re
from datetime import datetime
from random import randint
from typing import Final

ROOT_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))
DATA_DIR: Final[str] = f"{ROOT_DIR}/data"
VALID_IDS_FILE: Final[str] = f"{DATA_DIR}/legal_process_ids.json"

# FORMATTING
############


def remove_symbols(legal_process: str) -> str:
    """
    Removes specific symbols from a given legal process.

    This function takes a legal process as input and removes all occurrences
    of the '.' and '-' characters from it.

    Args:
        legal_process (str): A legal process containing symbols to be removed.

    Returns:
        str: The legal process string with the specified symbols removed.

    Example:
        >>> remove_symbols("123.45-678.901.234-56.7890")
        '12345678901234567890'
        >>> remove_symbols("9876543-21.0987.6.54.3210")
        '98765432109876543210'
    """

    return legal_process.replace(".", "").replace("-", "")


def format_legal_process(legal_process_id: str) -> str | None:
    """
    Format a legal process ID into a standard format.

    Args:
        legal_process_id (str): A 20-digits string representing the legal
                                process ID.

    Returns:
        str: The formatted legal process ID or None if the input is invalid.

    Example:
        >>> format_legal_process("12345678901234567890")
        '1234567-89.0123.4.56.7890'
        >>> format_legal_process("98765432109876543210")
        '9876543-21.0987.6.54.3210'
        >>> format_legal_process("123")
        None
    """

    if legal_process_id.isdigit() and len(legal_process_id) == 20:
        capture_fields = r"(\d{7})(\d{2})(\d{4})(\d)(\d{2})(\d{4})"
        include_chars = r"\1-\2.\3.\4.\5.\6"

        return re.sub(capture_fields, include_chars, legal_process_id)

    return None


# OPERATIONS
############


def is_valid(legal_process_id: str) -> bool:
    """
    Check if a legal process ID is valid.

    This function does not verify if the legal process ID is a real legal
    process ID; it only validates the format of the string.

    Args:
        legal_process_id (str): A digit-only string representing the legal
                                process ID.

    Returns:
        bool: True if the legal process ID is valid, False otherwise.

    Example:
        >>> is_valid("68476506020233030000")
        True
        >>> is_valid("51808233620233030000")
        True
        >>> is_valid("123")
        False
    """

    clean_legal_process_id = remove_symbols(legal_process_id)
    DD = clean_legal_process_id[7:9]
    J = clean_legal_process_id[13:14]
    TR = clean_legal_process_id[14:16]
    OOOO = clean_legal_process_id[16:]

    with open(VALID_IDS_FILE) as file:
        legal_process_ids = json.load(file)
        process = legal_process_ids.get(f"orgao_{J}")
        if not process:
            return False
        valid_process = int(TR) in process.get("id_tribunal") and int(
            OOOO
        ) in process.get("id_foro")

    return (
        _checksum(int(clean_legal_process_id[0:7] + clean_legal_process_id[9:]))
        == DD
    ) and valid_process


def generate(
    year: int = datetime.now().year, orgao: int = randint(1, 9)
) -> str | None:
    """
    Generate a random legal process ID number.

    Args:
        year (int): The year for the legal process ID (default is the current
                    year).
                    The year should not be in the past
        orgao (int): The organization code (1-9) for the legal process ID
                     (default is random).

    Returns:
        str: A randomly generated legal process ID.
             None if one of the arguments is invalid.

    Example:
        >>> generate(2023, 5)
        '51659517020235080562'
        >>> generate()
        '88031888120233030000'
        >>> generate(2022, 10)
        None
    """

    if year < datetime.now().year or orgao not in range(1, 10):
        return None

    # Getting possible legal process ids from 'legal_process_ids.json' asset
    with open(VALID_IDS_FILE) as file:
        legal_process_ids = json.load(file)
        _ = legal_process_ids[f"orgao_{orgao}"]
        TR = str(
            _["id_tribunal"][randint(0, (len(_["id_tribunal"]) - 1))]
        ).zfill(2)
        OOOO = str(_["id_foro"][randint(0, (len(_["id_foro"])) - 1)]).zfill(4)
        NNNNNNN = str(randint(0, 9999999)).zfill(7)
        DD = _checksum(f"{NNNNNNN}{year}{orgao}{TR}{OOOO}")

        return f"{NNNNNNN}{DD}{year}{orgao}{TR}{OOOO}"


def _checksum(basenum: int) -> str:
    """
    Checksum to compute the verification digit for a Legal Process ID number.
    `basenum` needs to be a digit without the verification id.

    Args:
        basenum (int): The base number for checksum calculation.

    Returns:
        str: The checksum value as a string.

    Example:
        >>> _checksum(1234567)
        '50'
        >>> _checksum(9876543)
        '88'
    """

    return str(97 - ((int(basenum) * 100) % 97)).zfill(2)

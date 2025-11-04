import unicodedata

from brutils.data.enums.uf import UF, UF_CODE


def convert_code_to_uf(code: str) -> str | None:
    """
    Converts a given IBGE code (2-digit string) to its corresponding UF (state abbreviation).

    This function takes a 2-digit IBGE code and returns the corresponding UF code.
    It handles all Brazilian states and the Federal District.

    Args:
        code (str): The 2-digit IBGE code to be converted.

    Returns:
        str or None: The UF code corresponding to the IBGE code,
            or None if the IBGE code is invalid.

    Example:
        >>> convert_code_to_uf('12')
        'AC'
        >>> convert_code_to_uf('33')
        'RJ'
        >>> convert_code_to_uf('99')
        >>>
    """
    if code not in UF_CODE.values:
        return None

    return UF_CODE(code).name


def convert_uf_to_name(uf: str) -> str | None:
    """
    Convert a Brazilian UF code (e.g., 'SP') to its full state name ('São Paulo').

    - The lookup is case-insensitive and ignores surrounding whitespace.
    - Returns ``None`` if the input is invalid or the UF code is not recognized.

    Args:
        uf (str): A two-letter UF code (e.g., 'RJ', 'sp').

    Returns:
        str | None: The full state name if found, or ``None`` if the code is invalid.

    Examples:
        >>> convert_uf_to_name('SP')
        'São Paulo'
        >>> convert_uf_to_name('rj')
        'Rio de Janeiro'
    """
    if not uf or not isinstance(uf, str) or len(uf.strip()) != 2:
        return None

    federal_unit = uf.strip().upper()

    if federal_unit not in UF.names:
        return None

    result = UF[federal_unit].value

    return result


def _normalize_text(text: str) -> str:
    """
    Normalize text by removing accents and normalizing whitespace.

    Args:
        text (str): The text to normalize.

    Returns:
        str: The normalized text in uppercase.
    """
    nfd = unicodedata.normalize("NFD", text)
    without_accents = "".join(
        char for char in nfd if unicodedata.category(char) != "Mn"
    )

    normalized_spaces = " ".join(without_accents.split())
    return normalized_spaces.upper()


def convert_name_to_uf(state_name: str) -> str | None:
    """
    Convert a Brazilian state name to its UF code.

    This function takes the full name of a Brazilian state and returns its
    corresponding two-letter UF code. The comparison is case-insensitive and
    ignores accents.

    Args:
        state_name (str): The full name of the state (e.g., 'São Paulo', 'sao paulo').

    Returns:
        str | None: The UF code if found, or None if the state name is invalid.

    Examples:
        >>> convert_name_to_uf('São Paulo')
        'SP'
        >>> convert_name_to_uf('sao paulo')
        'SP'
        >>> convert_name_to_uf('Rio de Janeiro')
        'RJ'
        >>> convert_name_to_uf('rio de janeiro')
        'RJ'
        >>> convert_name_to_uf('Estado Inválido')
        >>>
    """
    if not state_name or not isinstance(state_name, str):
        return None

    normalized_input = _normalize_text(state_name.strip())

    for uf in UF:
        if _normalize_text(uf.value) == normalized_input:
            return uf.name

    return None

from random import randint


def is_valid(voter_id: str) -> bool:
    """
    Check if a Brazilian voter id number is valid.
    It does not verify if the voter id actually exists.

    References:
    - https://pt.wikipedia.org/wiki/T%C3%ADtulo_de_eleitor,
    - http://clubes.obmep.org.br/blog/a-matematica-nos-documentos-titulo-de-eleitor/

    Args:
        voter_id(str): string representing the voter id to be verified.

    Returns:
        bool: True if the voter id is valid. False otherwise.
    """

    # ensure voter_id only contains numerical characters and has a valid length
    if (
        not isinstance(voter_id, str)
        or not voter_id.isdigit()
        or not _is_length_valid(voter_id)
    ):
        return False

    # the voter id is composed of 3 parts, in this order:
    #   - sequential_number (8 or 9 digits)
    #   - federative_union (2 digits)
    #   - verifying digits (2 digits)
    sequential_number = _get_sequential_number(voter_id)
    federative_union = _get_federative_union(voter_id)
    verifying_digits = _get_verifying_digits(voter_id)

    # ensure federative union is valid
    if not _is_federative_union_valid(federative_union):
        return False

    # ensure the first verifying digit is valid
    vd1 = _calculate_vd1(sequential_number, federative_union)
    if vd1 != int(verifying_digits[0]):
        return False

    # ensure the second verifying digit is valid
    vd2 = _calculate_vd2(federative_union, vd1)
    if vd2 != int(verifying_digits[1]):
        return False

    return True


def _is_length_valid(voter_id: str) -> bool:
    """
    Check if the length of the provided voter id is valid.
    Typically, the length should be 12, but there are cases for SP and MG where
    the length might be 13. This occurs as an edge case when the sequential
    number has 9 digits instead of 8.

    Args:
        voter_id (str): string representing the voter id to be verified

    Returns:
        bool: True if the length is valid. False otherwise.
    """

    federative_union = _get_federative_union(voter_id)

    if len(voter_id) == 12:
        return True

    # edge case: for SP and MG with 9 digit long 'sequential number'
    return len(voter_id) == 13 and federative_union in ["01", "02"]


def _get_sequential_number(voter_id: str) -> str:
    """
    Some voter ids in São Paulo and Minas Gerais may have nine digits in their
    sequential number instead of eight. This fact does not compromise the
    calculation of the check digits, as it is done based on the first eight
    sequential numbers.

    Args:
        voter_id (str): string representing the voter id to be verified.

    Returns:
        str: eight-digit string representing the sequential number for the
             given voter id
    """

    return voter_id[:8]


def _get_federative_union(voter_id: str) -> str:
    """
    Returns the two digits that represent the federative union for the given
    voter id. Indexing it backwards, as the sequential_number can have eight
    or nine digits.

    Args:
        voter_id (str): string representing the voter id to be verified

    Returns:
        str: two-digits string representing the federative union for the given voter id
    """

    return voter_id[-4:-2]


def _get_verifying_digits(voter_id: str) -> str:
    """
    Returns the two verifying digits for the given voter id. Indexing it
    backwards, as the sequential_number can have eight or nine digits.

    Args:
        voter_id (str): string representing the voter id to be verified

    Returns:
        str: the two verifying digits for the given voter id
    """

    return voter_id[-2:]


def _is_federative_union_valid(federative_union: str) -> bool:
    """
    Check if the federative union is valid.

    Args:
        federative_union(str): federative union for the given voter id

    Returns:
        bool: True if the federative union is valid. False otherwise.
    """

    # valid federative unions: from '01' to '28'
    return federative_union in ["{:02d}".format(i) for i in range(1, 29)]


def _calculate_vd1(sequential_number: str, federative_union: str) -> int:
    """
    Calculate the first verifying digit.

    Args:
        sequential_number(str): sequential number sliced from the voter_id
        federative_union(str): federative union for the given voter id

    Returns:
        int: the expected value for the first verifying digit for the given
             voter id
    """

    # 2, 3, 4, 5, 6, 7, 8, 9
    x1, x2, x3, x4, x5, x6, x7, x8 = range(2, 10)

    sum = (
        (int(sequential_number[0]) * x1)
        + (int(sequential_number[1]) * x2)
        + (int(sequential_number[2]) * x3)
        + (int(sequential_number[3]) * x4)
        + (int(sequential_number[4]) * x5)
        + (int(sequential_number[5]) * x6)
        + (int(sequential_number[6]) * x7)
        + (int(sequential_number[7]) * x8)
    )

    rest = sum % 11
    vd1 = rest

    # edge case: rest == 0 and federative_union is SP or MG
    if rest == 0 and federative_union in ["01", "02"]:
        vd1 = 1

    # edge case: rest == 10, declare vd1 as zero
    if rest == 10:
        vd1 = 0

    return vd1


def _calculate_vd2(federative_union: str, vd1: int) -> int:
    """
    Calculate the second verifying digit.

    Args:
        federative_union(str): federative union for the given voter id
        vd1(int): first verifying digit calculated for the given voter id

    Returns:
        int: the expected value for the second verifying digit for the given
             voter id
    """

    x9, x10, x11 = 7, 8, 9

    sum = (
        (int(federative_union[0]) * x9)
        + (int(federative_union[1]) * x10)
        + (vd1 * x11)
    )

    rest = sum % 11
    vd2 = rest

    # edge case: if federative_union is "01" or "02" (for SP and MG) AND
    # rest == 0, declare vd2 as 1
    if federative_union in ["01", "02"] and rest == 0:
        vd2 = 1

    # edge case: rest == 10, declare vd2 as zero
    if rest == 10:
        vd2 = 0

    return vd2


def generate(federative_union: str = "ZZ") -> str | None:
    """
    Generates a random valid Brazilian voter registration.

    Args:
        federative_union(str): federative union for the voter id that will be generated. The default value "ZZ" is used for voter IDs issued to foreigners.

    Returns:
        str: A randomly generated valid voter ID for the given federative union
    """
    UFs = {
        "SP": "01",
        "MG": "02",
        "RJ": "03",
        "RS": "04",
        "BA": "05",
        "PR": "06",
        "CE": "07",
        "PE": "08",
        "SC": "09",
        "GO": "10",
        "MA": "11",
        "PB": "12",
        "PA": "13",
        "ES": "14",
        "PI": "15",
        "RN": "16",
        "AL": "17",
        "MT": "18",
        "MS": "19",
        "DF": "20",
        "SE": "21",
        "AM": "22",
        "RO": "23",
        "AC": "24",
        "AP": "25",
        "RR": "26",
        "TO": "27",
        "ZZ": "28",
    }

    federative_union = federative_union.upper()
    if federative_union in (UFs):
        sequential_number = str(randint(0, 99999999)).zfill(8)
        uf_number = UFs[federative_union]
        if _is_federative_union_valid(uf_number):
            vd1 = _calculate_vd1(sequential_number, uf_number)
            vd2 = _calculate_vd2(uf_number, vd1)
            return f"{sequential_number}{uf_number}{vd1}{vd2}"
    return None


def format_voter_id(voter_id: str) -> str | None:
    """
    Format a voter ID for display with visual spaces.

    This function takes a numeric voter ID string as input and adds standard
    formatting for display purposes.

    Args:
        voter_id (str): A numeric voter ID string.

    Returns:
        str: A formatted voter ID string with standard visual spacing, or None
        if the input is invalid.

    Example:
        >>> format_voter_id("690847092828")
        '6908 4709 28 28'
        >>> format_voter_id("163204010922")
        '1632 0401 09 22'
    """

    if not is_valid(voter_id):
        return None

    return "{} {} {} {}".format(
        voter_id[:4], voter_id[4:8], voter_id[8:10], voter_id[10:12]
    )

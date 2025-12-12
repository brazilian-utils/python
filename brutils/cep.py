from json import loads
from random import randint
from unicodedata import normalize
from urllib.request import urlopen

from brutils.data.enums import UF
from brutils.exceptions import CEPNotFound, InvalidCEP
from brutils.schemas import Address

# FORMATTING
############


def format_cep(cep: str, only_nums=False) -> str | None:
    """
    Formats a Brazilian CEP (Postal Code) into a standard format.

    This function takes a CEP (Postal Code) as input and,
        - Removes special characteres;
        - Check if the string follows the CEP length pattern;
        - Returns None if the string is out of the pattern;
        - Return a string with the formatted CEP.

    Args:
        cep (str): The input CEP (Postal Code) to be formatted.

    Returns:
        str: The formatted CEP in the "12345-678" format if it's valid,
             None if it's not valid.

    Example:
        >>> format_cep("12345678")
        "12345-678"
        >>> format_cep("  12.345/678 ", only_nums=True)
        "12345678"
        >>> format_cep("12345")
        None
    """
    ### Checking data type
    if not isinstance(cep, str):
        return None

    ### Removing special characteres
    cep = "".join(filter(str.isalnum, cep))

    ### Checking CEP patterns
    if len(cep) != 8:
        return None

    ### Returning CEP value
    if only_nums:
        return cep
    else:
        return f"{cep[:5]}-{cep[5:]}"


# OPERATIONS
############


def is_valid(cep: str) -> bool:
    """
    Checks if a CEP (Postal Code) is valid.

    To be considered valid, the input must be a string containing exactly 8
    digits.
    This function does not verify if the CEP is a real postal code; it only
    validates the format of the string.

    Args:
        cep (str): The string containing the CEP to be checked.

    Returns:
        bool: True if the CEP is valid (8 digits), False otherwise.

    Example:
        >>> is_valid("12345678")
        True
        >>> is_valid("12345")
        False
        >>> is_valid("abcdefgh")
        False

    Source:
        https://en.wikipedia.org/wiki/Código_de_Endereçamento_Postal
    """

    return isinstance(cep, str) and len(cep) == 8 and cep.isdigit()


def generate() -> str:
    """
    Generates a random 8-digit CEP (Postal Code) number as a string.

    Returns:
        str: A randomly generated 8-digit number.

    Example:
        >>> generate()
        "12345678"
    """

    generated_number = ""

    for _ in range(8):
        generated_number = generated_number + str(randint(0, 9))

    return generated_number


# Reference: https://viacep.com.br/
def get_address_from_cep(
    cep: str, raise_exceptions: bool = False
) -> Address | None:
    """
    Fetches address information from a given CEP (Postal Code) using the ViaCEP API.

    Args:
        cep (str): The CEP (Postal Code) to be used in the search.
        raise_exceptions (bool, optional): Whether to raise exceptions when the CEP is invalid or not found. Defaults to False.

    Raises:
        InvalidCEP: When the input CEP is invalid.
        CEPNotFound: When the input CEP is not found.

    Returns:
        Address | None: An Address object (TypedDict) containing the address information if the CEP is found, None otherwise.

    Example:
        >>> get_address_from_cep("12345678")
        {
            "cep": "12345-678",
            "logradouro": "Rua Example",
            "complemento": "",
            "bairro": "Example",
            "localidade": "Example",
            "uf": "EX",
            "ibge": "1234567",
            "gia": "1234",
            "ddd": "12",
            "siafi": "1234"
        }

        >>> get_address_from_cep("abcdefg")
        None

        >>> get_address_from_cep("abcdefg", True)
        InvalidCEP: CEP 'abcdefg' is invalid.

        >>> get_address_from_cep("00000000", True)
        CEPNotFound: 00000000
    """
    base_api_url = "https://viacep.com.br/ws/{}/json/"

    clean_cep = format_cep(cep, only_nums=True)
    cep_is_valid = is_valid(clean_cep)

    if not cep_is_valid:
        if raise_exceptions:
            raise InvalidCEP(cep)

        return None

    try:
        with urlopen(base_api_url.format(clean_cep)) as f:
            response = f.read()
            data = loads(response)

            if data.get("erro", False):
                raise CEPNotFound(cep)

            return Address(**loads(response))

    except Exception as e:
        if raise_exceptions:
            raise CEPNotFound(cep) from e

        return None


def get_cep_information_from_address(
    federal_unit: str, city: str, street: str, raise_exceptions: bool = False
) -> list[Address] | None:
    """
    Fetches CEP (Postal Code) options from a given address using the ViaCEP API.

    Args:
        federal_unit (str): The two-letter abbreviation of the Brazilian state.
        city (str): The name of the city.
        street (str): The name (or substring) of the street.
        raise_exceptions (bool, optional): Whether to raise exceptions when the address is invalid or not found. Defaults to False.

    Raises:
        ValueError: When the input UF is invalid.
        CEPNotFound: When the input address is not found.

    Returns:
        list[Address] | None: A list of Address objects (TypedDict) containing the address information if the address is found, None otherwise.

    Example:
        >>> get_cep_information_from_address("EX", "Example", "Rua Example")
        [
            {
                "cep": "12345-678",
                "logradouro": "Rua Example",
                "complemento": "",
                "bairro": "Example",
                "localidade": "Example",
                "uf": "EX",
                "ibge": "1234567",
                "gia": "1234",
                "ddd": "12",
                "siafi": "1234"
            }
        ]

        >>> get_cep_information_from_address("A", "Example", "Rua Example")
        None

        >>> get_cep_information_from_address("XX", "Example", "Example", True)
        ValueError: Invalid UF: XX

        >>> get_cep_information_from_address("SP", "Example", "Example", True)
        CEPNotFound: SP - Example - Example
    """
    if federal_unit in UF.values:
        federal_unit = UF(federal_unit).name

    if federal_unit not in UF.names:
        if raise_exceptions:
            raise ValueError(f"Invalid UF: {federal_unit}")

        return None

    base_api_url = "https://viacep.com.br/ws/{}/{}/{}/json/"

    parsed_city = (
        normalize("NFD", city)
        .encode("ascii", "ignore")
        .decode("utf-8")
        .replace(" ", "%20")
    )
    parsed_street = (
        normalize("NFD", street)
        .encode("ascii", "ignore")
        .decode("utf-8")
        .replace(" ", "%20")
    )

    try:
        with urlopen(
            base_api_url.format(federal_unit, parsed_city, parsed_street)
        ) as f:
            response = f.read()
            response = loads(response)

            if len(response) == 0:
                raise CEPNotFound(f"{federal_unit} - {city} - {street}")

            return [Address(**address) for address in response]

    except Exception as e:
        if raise_exceptions:
            raise CEPNotFound(f"{federal_unit} - {city} - {street}") from e

        return None

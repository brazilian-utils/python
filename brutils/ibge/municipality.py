import gzip
import io
import json
import unicodedata
from urllib.error import HTTPError
from urllib.request import urlopen

IBGE_MUNICIPALITY_BY_CODE_URL = (
    "https://servicodados.ibge.gov.br/api/v1/localidades/municipios/{code}"
)
IBGE_MUNICIPALITIES_BY_UF_URL = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios"


def get_municipality_by_code(code: str) -> tuple[str, str] | None:
    """
    Returns the municipality name and UF for a given IBGE code.

    This function takes a string representing an IBGE municipality code
    and returns a tuple with the municipality's name and its corresponding UF.

    Args:
        code (str): The IBGE code of the municipality.

    Returns:
        tuple: A tuple formatted as ("Município", "UF") or
               None if the code is not valid.

    Example:
        >>> get_municipality_by_code("3550308")
        ('São Paulo', 'SP')
        >>> get_municipality_by_code("3304557")
        ('Rio de Janeiro', 'RJ')
        >>> get_municipality_by_code("1234567")
    """
    base_url = IBGE_MUNICIPALITY_BY_CODE_URL.format(code=code)

    decompressed_data = _fetch_ibge_data(base_url)

    if decompressed_data is None:
        return None

    try:
        json_data = json.loads(decompressed_data)
        return _get_values(json_data)
    except (json.JSONDecodeError, KeyError):
        return None


def get_code_by_municipality_name(
    municipality_name: str, uf: str
) -> str | None:
    """
    Returns the IBGE code for a given municipality name and uf code.

    This function takes a string representing a municipality's name
    and uf's code and returns the corresponding IBGE code (string). The function
    will handle names by ignoring differences in case, accents, and
    treating the character ç as c and ignoring case differences for the uf code.

    Args:
        municipality_name (str): The name of the municipality.
        uf (str): The uf code of the state.

    Returns:
        str: The IBGE code of the municipality or
             None if the name is not valid or does not exist.

    Example:
        >>> get_code_by_municipality_name("São Paulo", "SP")
        '3550308'
        >>> get_code_by_municipality_name("Conceição do Coité", "Ba")
        '2908408'
        >>> get_code_by_municipality_name("Municipio Inexistente", "RS")
    """
    uf = uf.upper()

    base_url = IBGE_MUNICIPALITIES_BY_UF_URL.format(uf=uf)

    decompressed_data = _fetch_ibge_data(base_url)
    if decompressed_data is None:
        return None

    try:
        json_data = json.loads(decompressed_data)
        normalized_municipality_name = _transform_text(municipality_name)

        for municipality in json_data:
            municipality_name_from_api = municipality.get("nome", "")
            normalized_name_from_api = _transform_text(
                municipality_name_from_api
            )

            if normalized_name_from_api == normalized_municipality_name:
                return str(municipality.get("id"))

        return None

    except (json.JSONDecodeError, KeyError):
        return None


def _fetch_ibge_data(url: str) -> bytes | None:
    """
    Fetch data from IBGE API with gzip decompression support.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        bytes | None: The decompressed data or None if failed.
    """
    try:
        with urlopen(url) as f:
            compressed_data = f.read()
            if f.info().get("Content-Encoding") == "gzip":
                try:
                    with gzip.GzipFile(
                        fileobj=io.BytesIO(compressed_data)
                    ) as gzip_file:
                        decompressed_data = gzip_file.read()
                except (OSError, Exception):
                    return None
            else:
                decompressed_data = compressed_data

            if _is_empty(decompressed_data):
                return None

            return decompressed_data

    except HTTPError:
        return None
    except Exception:
        return None


def _get_values(data: dict) -> tuple[str, str]:
    """Extract municipality name and UF from IBGE API response."""
    municipio = data["nome"]
    estado = data["microrregiao"]["mesorregiao"]["UF"]["sigla"]
    return (municipio, estado)


def _is_empty(data: bytes) -> bool:
    """Check if the response data is empty."""
    return data == b"[]" or len(data) == 0


def _transform_text(municipality_name: str) -> str:
    """
    Normalize municipality name and returns the normalized string.

    Args:
        municipality_name (str): The name of the municipality.

    Returns:
        str: The normalized string

    Example:
        >>> _transform_text("São Paulo")
        'sao paulo'
        >>> _transform_text("Goiânia")
        'goiania'
        >>> _transform_text("Conceição do Coité")
        'conceicao do coite'
    """
    normalized_string = (
        unicodedata.normalize("NFKD", municipality_name)
        .encode("ascii", "ignore")
        .decode("ascii")
    )
    case_fold_string = normalized_string.casefold()

    return case_fold_string

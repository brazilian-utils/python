import gzip
from json import JSONDecodeError, dumps
from unittest import TestCase, main
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError

from brutils.ibge.municipality import (
    _get_values,
    _is_empty,
    _transform_text,
    get_code_by_municipality_name,
    get_municipality_by_code,
)

IBGE_BASE_URL = "https://servicodados.ibge.gov.br/api/v1/localidades"

VALID_MUNICIPALITY_DATA = {
    "SAO_PAULO": {
        "nome": "São Paulo",
        "microrregiao": {"mesorregiao": {"UF": {"sigla": "SP"}}},
        "code": "3550308",
    },
    "RIO_DE_JANEIRO": {
        "nome": "Rio de Janeiro",
        "microrregiao": {"mesorregiao": {"UF": {"sigla": "RJ"}}},
        "code": "3304557",
    },
    "GOIANIA": {
        "nome": "Goiânia",
        "microrregiao": {"mesorregiao": {"UF": {"sigla": "GO"}}},
        "code": "5208707",
    },
}


class TestIBGE(TestCase):
    """Test suite for IBGE municipality functions."""

    def _create_mock_response(self, data, encoding=None):
        """Helper method to create mock HTTP responses."""
        mock_file = MagicMock()
        mock_file.__enter__.return_value = mock_file
        mock_file.read.return_value = data
        mock_file.info.return_value = {"Content-Encoding": encoding}
        return mock_file

    @patch("brutils.ibge.municipality.urlopen")
    def test_get_municipality_by_code_success(self, mock):
        """Test successful municipality retrieval by code."""

        def mock_response(url):
            responses = {
                f"{IBGE_BASE_URL}/municipios/{VALID_MUNICIPALITY_DATA['SAO_PAULO']['code']}": dumps(
                    VALID_MUNICIPALITY_DATA["SAO_PAULO"]
                ).encode("utf-8"),
                f"{IBGE_BASE_URL}/municipios/{VALID_MUNICIPALITY_DATA['RIO_DE_JANEIRO']['code']}": dumps(
                    VALID_MUNICIPALITY_DATA["RIO_DE_JANEIRO"]
                ).encode("utf-8"),
                f"{IBGE_BASE_URL}/municipios/{VALID_MUNICIPALITY_DATA['GOIANIA']['code']}": dumps(
                    VALID_MUNICIPALITY_DATA["GOIANIA"]
                ).encode("utf-8"),
                f"{IBGE_BASE_URL}/municipios/1234567": b"[]",
            }
            return self._create_mock_response(responses.get(url, b"[]"))

        mock.side_effect = mock_response

        self.assertEqual(
            get_municipality_by_code(
                VALID_MUNICIPALITY_DATA["SAO_PAULO"]["code"]
            ),
            ("São Paulo", "SP"),
        )
        self.assertEqual(
            get_municipality_by_code(
                VALID_MUNICIPALITY_DATA["RIO_DE_JANEIRO"]["code"]
            ),
            ("Rio de Janeiro", "RJ"),
        )
        self.assertEqual(
            get_municipality_by_code(
                VALID_MUNICIPALITY_DATA["GOIANIA"]["code"]
            ),
            ("Goiânia", "GO"),
        )
        self.assertIsNone(get_municipality_by_code("1234567"))

    @patch("brutils.ibge.municipality.urlopen")
    def test_get_municipality_by_code_http_error_404(self, mock):
        """Test HTTP 404 error handling."""
        mock.side_effect = HTTPError(
            "http://fakeurl.com", 404, "Not Found", None, None
        )
        result = get_municipality_by_code("342432")
        self.assertIsNone(result)

    @patch("brutils.ibge.municipality.urlopen")
    def test_get_municipality_by_code_http_error_401(self, mock):
        """Test HTTP 401 error handling."""
        mock.side_effect = HTTPError(
            "http://fakeurl.com", 401, "Denied", None, None
        )
        result = get_municipality_by_code("342432")
        self.assertIsNone(result)

    @patch("brutils.ibge.municipality.urlopen")
    def test_get_municipality_by_code_generic_exception(self, mock):
        """Test generic exception handling."""
        mock.side_effect = Exception("Erro desconhecido")
        result = get_municipality_by_code("342432")
        self.assertIsNone(result)

    @patch("brutils.ibge.municipality.urlopen")
    def test_get_municipality_by_code_gzip_success(self, mock_urlopen):
        """Test successful gzip decompression."""
        valid_json = dumps(VALID_MUNICIPALITY_DATA["SAO_PAULO"])
        compressed_data = gzip.compress(valid_json.encode("utf-8"))
        mock_response = self._create_mock_response(compressed_data, "gzip")
        mock_urlopen.return_value = mock_response

        result = get_municipality_by_code("3550308")
        self.assertEqual(result, ("São Paulo", "SP"))

    @patch("brutils.ibge.municipality.urlopen")
    def test_get_municipality_by_code_no_compression(self, mock_urlopen):
        """Test successful JSON parsing without compression."""
        valid_json = dumps(VALID_MUNICIPALITY_DATA["SAO_PAULO"])
        mock_response = self._create_mock_response(valid_json.encode("utf-8"))
        mock_urlopen.return_value = mock_response

        result = get_municipality_by_code("3550308")
        self.assertEqual(result, ("São Paulo", "SP"))

    @patch("brutils.ibge.municipality.urlopen")
    @patch("gzip.GzipFile.read", side_effect=OSError("Erro na descompressão"))
    def test_get_municipality_by_code_gzip_error(
        self, mock_gzip_read, mock_urlopen
    ):
        """Test gzip decompression error handling."""
        valid_json = dumps(VALID_MUNICIPALITY_DATA["SAO_PAULO"])
        compressed_data = gzip.compress(valid_json.encode("utf-8"))
        mock_urlopen.return_value = self._create_mock_response(
            compressed_data, "gzip"
        )

        result = get_municipality_by_code("3550308")
        self.assertIsNone(result)

    @patch("brutils.ibge.municipality.urlopen")
    @patch(
        "gzip.GzipFile.read",
        side_effect=Exception("Erro desconhecido na descompressão"),
    )
    def test_get_municipality_by_code_gzip_generic_error(
        self, mock_gzip_read, mock_urlopen
    ):
        """Test generic gzip error handling."""
        valid_json = dumps(VALID_MUNICIPALITY_DATA["SAO_PAULO"])
        compressed_data = gzip.compress(valid_json.encode("utf-8"))
        mock_urlopen.return_value = self._create_mock_response(
            compressed_data, "gzip"
        )

        result = get_municipality_by_code("3550308")
        self.assertIsNone(result)

    @patch("json.loads", side_effect=JSONDecodeError("error", "city.json", 1))
    def test_get_municipality_by_code_json_decode_error(self, mock_json_loads):
        """Test JSON decode error handling."""
        result = get_municipality_by_code("3550308")
        self.assertIsNone(result)

    @patch("json.loads", side_effect=KeyError)
    def test_get_municipality_by_code_json_key_error(self, mock_json_loads):
        """Test JSON key error handling."""
        result = get_municipality_by_code("3550308")
        self.assertIsNone(result)

    @patch("brutils.ibge.municipality.urlopen")
    def test_get_code_by_municipality_name_success(self, mock_urlopen):
        """Test successful municipality code retrieval by name and UF."""

        def mock_response(url):
            mock_responses = {
                f"{IBGE_BASE_URL}/estados/SC/municipios": [
                    {"nome": "Florianópolis", "id": 4205407},
                    {"nome": "Aurora", "id": 4201901},
                    {"nome": "Lauro Müller", "id": 4209607},
                ],
                f"{IBGE_BASE_URL}/estados/SP/municipios": [
                    {"nome": "São Paulo", "id": 3550308},
                ],
                f"{IBGE_BASE_URL}/estados/RJ/municipios": [
                    {"nome": "Rio de Janeiro", "id": 3304557},
                ],
                f"{IBGE_BASE_URL}/estados/GO/municipios": [
                    {"nome": "Goiânia", "id": 5208707},
                ],
                f"{IBGE_BASE_URL}/estados/BA/municipios": [
                    {"nome": "Conceição do Coité", "id": 2908408},
                ],
                f"{IBGE_BASE_URL}/estados/RS/municipios": [
                    {"nome": "Tôrres", "id": 4321501},
                ],
                f"{IBGE_BASE_URL}/estados/CE/municipios": [
                    {"nome": "Aurora", "id": 2301703},
                ],
            }

            response_data = mock_responses.get(url, [])
            json_data = dumps(response_data).encode("utf-8")
            return self._create_mock_response(json_data)

        mock_urlopen.side_effect = mock_response

        self.assertEqual(
            get_code_by_municipality_name("Florianópolis", "sc"), "4205407"
        )
        self.assertEqual(
            get_code_by_municipality_name("São Paulo", "sp"), "3550308"
        )
        self.assertEqual(
            get_code_by_municipality_name("rio de janeiro", "rj"), "3304557"
        )
        self.assertEqual(
            get_code_by_municipality_name("GOIANIA", "GO"), "5208707"
        )
        self.assertEqual(
            get_code_by_municipality_name("Conceição do Coité", "BA"), "2908408"
        )
        self.assertEqual(
            get_code_by_municipality_name("conceicao do Coite", "Ba"), "2908408"
        )
        self.assertEqual(
            get_code_by_municipality_name("Lauro Müller", "sc"), "4209607"
        )
        self.assertEqual(
            get_code_by_municipality_name("Tôrres", "rs"), "4321501"
        )
        self.assertEqual(
            get_code_by_municipality_name("aurora", "ce"), "2301703"
        )
        self.assertEqual(
            get_code_by_municipality_name("aurora", "sc"), "4201901"
        )

    def test_get_code_by_municipality_name_not_found(self):
        """Test cases where municipality is not found."""
        self.assertIsNone(
            get_code_by_municipality_name("Municipio Inexistente", "RS")
        )
        self.assertIsNone(get_code_by_municipality_name("São Paulo", "XX"))

    @patch("brutils.ibge.municipality.urlopen")
    def test_get_code_by_municipality_name_http_error_404(self, mock):
        """Test HTTP 404 error handling for municipality name search."""
        mock.side_effect = HTTPError(
            "http://fakeurl.com", 404, "Not Found", None, None
        )
        result = get_code_by_municipality_name("São Paulo", "XX")
        self.assertIsNone(result)

    @patch("brutils.ibge.municipality.urlopen")
    def test_get_code_by_municipality_name_http_error_500(self, mock):
        """Test HTTP 500 error handling for municipality name search."""
        mock.side_effect = HTTPError(
            "http://fakeurl.com", 500, "Internal Server Error", None, None
        )
        result = get_code_by_municipality_name("São Paulo", "SP")
        self.assertIsNone(result)

    @patch("brutils.ibge.municipality.urlopen")
    def test_get_code_by_municipality_name_generic_exception(self, mock):
        """Test generic exception handling for municipality name search."""
        mock.side_effect = Exception("Network error")
        result = get_code_by_municipality_name("São Paulo", "SP")
        self.assertIsNone(result)

    @patch("brutils.ibge.municipality.urlopen")
    def test_get_code_by_municipality_name_empty_response(self, mock):
        """Test empty API response handling."""
        mock_response = self._create_mock_response(b"[]")
        mock.return_value = mock_response

        result = get_code_by_municipality_name("São Paulo", "SP")
        self.assertIsNone(result)

    @patch("brutils.ibge.municipality.urlopen")
    def test_get_code_by_municipality_name_json_decode_error(self, mock):
        """Test JSON decode error handling."""
        mock_response = self._create_mock_response(b"invalid json")
        mock.return_value = mock_response

        result = get_code_by_municipality_name("São Paulo", "SP")
        self.assertIsNone(result)

    @patch("brutils.ibge.municipality.urlopen")
    def test_get_code_by_municipality_name_missing_fields(self, mock):
        """Test response with missing required fields."""
        invalid_data = dumps([{"invalid": "data"}]).encode("utf-8")
        mock_response = self._create_mock_response(invalid_data)
        mock.return_value = mock_response

        result = get_code_by_municipality_name("São Paulo", "SP")
        self.assertIsNone(result)

    @patch("brutils.ibge.municipality.urlopen")
    def test_get_code_by_municipality_name_gzip_success(self, mock):
        """Test successful gzip decompression for municipality name search."""
        municipalities_data = [
            {"nome": "São Paulo", "id": 3550308},
            {"nome": "Campinas", "id": 3509502},
        ]
        json_data = dumps(municipalities_data)
        compressed_data = gzip.compress(json_data.encode("utf-8"))

        mock_response = self._create_mock_response(compressed_data, "gzip")
        mock.return_value = mock_response

        result = get_code_by_municipality_name("São Paulo", "SP")
        self.assertEqual(result, "3550308")

    @patch("brutils.ibge.municipality.urlopen")
    def test_get_code_by_municipality_name_gzip_error(self, mock):
        """Test gzip decompression error for municipality name search."""
        mock_response = self._create_mock_response(b"invalid gzip data", "gzip")
        mock.return_value = mock_response

        result = get_code_by_municipality_name("São Paulo", "SP")
        self.assertIsNone(result)

    def test_transform_text_normalization(self):
        """Test text normalization with accent removal and case conversion."""
        self.assertEqual(_transform_text("São Paulo"), "sao paulo")
        self.assertEqual(_transform_text("Goiânia"), "goiania")
        self.assertEqual(
            _transform_text("Conceição do Coité"), "conceicao do coite"
        )
        self.assertEqual(_transform_text("BRASÍLIA"), "brasilia")
        self.assertEqual(_transform_text("rio de janeiro"), "rio de janeiro")
        self.assertEqual(_transform_text("Müller"), "muller")
        self.assertEqual(_transform_text("Tôrres"), "torres")
        self.assertEqual(_transform_text("José de Freitas"), "jose de freitas")

    def test_transform_text_edge_cases(self):
        """Test edge cases for text transformation."""
        self.assertEqual(_transform_text(""), "")
        self.assertEqual(_transform_text("A"), "a")
        self.assertEqual(_transform_text("   "), "   ")

    def test_is_empty_response_detection(self):
        """Test detection of empty API responses."""
        self.assertTrue(_is_empty(b"[]"))
        self.assertTrue(_is_empty(b""))
        self.assertFalse(_is_empty(b"[{}]"))
        self.assertFalse(_is_empty(b'{"name": "test"}'))
        self.assertFalse(_is_empty(b"some data"))

    def test_get_values_success(self):
        """Test successful data extraction from municipality JSON."""
        result = _get_values(VALID_MUNICIPALITY_DATA["SAO_PAULO"])
        self.assertEqual(result, ("São Paulo", "SP"))
        result = _get_values(VALID_MUNICIPALITY_DATA["RIO_DE_JANEIRO"])
        self.assertEqual(result, ("Rio de Janeiro", "RJ"))

    def test_get_values_key_errors(self):
        """Test KeyError handling for malformed data structures."""
        with self.assertRaises(KeyError):
            _get_values({"invalid": "structure"})

        with self.assertRaises(KeyError):
            _get_values({"nome": "Test"})

        with self.assertRaises(KeyError):
            _get_values(
                {"nome": "Test", "microrregiao": {"invalid": "structure"}}
            )

    def test_empty_string_parameters(self):
        """Test handling of empty string parameters."""
        result = get_code_by_municipality_name("", "SP")
        self.assertIsNone(result)

        result = get_code_by_municipality_name("São Paulo", "")
        self.assertIsNone(result)

    def test_case_insensitive_uf_handling(self):
        """Test that UF parameter is case insensitive."""
        result1 = get_code_by_municipality_name("São Paulo", "sp")
        result2 = get_code_by_municipality_name("São Paulo", "SP")
        result3 = get_code_by_municipality_name("São Paulo", "Sp")

        self.assertEqual(result1, result2)
        self.assertEqual(result2, result3)


if __name__ == "__main__":
    main()

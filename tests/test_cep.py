from unittest import TestCase, main
from unittest.mock import MagicMock, patch

from brutils.cep import (
    CEPNotFound,
    InvalidCEP,
    format_cep,
    generate,
    get_address_from_cep,
    get_cep_information_from_address,
    is_valid,
    remove_symbols,
)


class TestCEP(TestCase):
    def test_remove_symbols(self):
        self.assertEqual(remove_symbols("00000000"), "00000000")
        self.assertEqual(remove_symbols("01310-200"), "01310200")
        self.assertEqual(remove_symbols("01..310.-200.-"), "01310200")
        self.assertEqual(remove_symbols("abc01310200*!*&#"), "abc01310200*!*&#")
        self.assertEqual(
            remove_symbols("ab.c1.--.3-102.-0-.0-.*.-!*&#"), "abc1310200*!*&#"
        )
        self.assertEqual(remove_symbols("...---..."), "")

    def test_is_valid(self):
        # When CEP is not string, returns False
        self.assertIs(is_valid(1), False)

        # When CEP's len is different of 8, returns False
        self.assertIs(is_valid("1"), False)

        # When CEP does not contain only digits, returns False
        self.assertIs(is_valid("1234567-"), False)

        # When CEP is valid
        self.assertIs(is_valid("99999999"), True)
        self.assertIs(is_valid("88390000"), True)

    def test_generate(self):
        for _ in range(10_000):
            self.assertIs(is_valid(generate()), True)


@patch("brutils.cep.is_valid")
class TestIsValidToFormat(TestCase):
    def test_when_cep_is_valid_returns_True_to_format(self, mock_is_valid):
        mock_is_valid.return_value = True

        self.assertEqual(format_cep("01310200"), "01310-200")

        # Checks if function is_valid_cnpj is called
        mock_is_valid.assert_called_once_with("01310200")

    def test_when_cep_is_not_valid_raises_value_error(self, mock_is_valid):
        mock_is_valid.return_value = False

        # When cep isn't valid, raises ValueError
        with self.assertRaises(ValueError):
            format_cep("013102009")


@patch("brutils.cep.urlopen")
class TestCEPAPICalls(TestCase):
    @patch("brutils.cep.loads")
    def test_get_address_from_cep_success(self, mock_loads, mock_urlopen):
        mock_loads.return_value = {"cep": "01310-200"}

        self.assertEqual(
            get_address_from_cep("01310200", True), {"cep": "01310-200"}
        )

    def test_get_address_from_cep_raise_exception_invalid_cep(
        self, mock_urlopen
    ):
        mock_data = MagicMock()
        mock_data.read.return_value = {"erro": True}
        mock_urlopen.return_value = mock_data

        self.assertIsNone(get_address_from_cep("013102009"))

    def test_get_address_from_cep_invalid_cep_raise_exception_invalid_cep(
        self, mock_urlopen
    ):
        with self.assertRaises(InvalidCEP):
            get_address_from_cep("abcdef", True)

    def test_get_address_from_cep_invalid_cep_raise_exception_cep_not_found(
        self, mock_urlopen
    ):
        mock_data = MagicMock()
        mock_data.read.return_value = {"erro": True}
        mock_urlopen.return_value = mock_data

        with self.assertRaises(CEPNotFound):
            get_address_from_cep("01310209", True)

    @patch("brutils.cep.loads")
    def test_get_cep_information_from_address_success(
        self, mock_loads, mock_urlopen
    ):
        mock_loads.return_value = [{"cep": "01310-200"}]

        self.assertDictEqual(
            get_cep_information_from_address(
                "SP", "Example", "Rua Example", True
            )[0],
            {"cep": "01310-200"},
        )

    @patch("brutils.cep.loads")
    def test_get_cep_information_from_address_success_with_uf_conversion(
        self, mock_loads, mock_urlopen
    ):
        mock_loads.return_value = [{"cep": "01310-200"}]

        self.assertDictEqual(
            get_cep_information_from_address(
                "São Paulo", "Example", "Rua Example", True
            )[0],
            {"cep": "01310-200"},
        )

    @patch("brutils.cep.loads")
    def test_get_cep_information_from_address_empty_response(
        self, mock_loads, mock_urlopen
    ):
        mock_loads.return_value = []

        self.assertIsNone(
            get_cep_information_from_address("SP", "Example", "Rua Example")
        )

    @patch("brutils.cep.loads")
    def test_get_cep_information_from_address_raise_exception_invalid_cep(
        self, mock_loads, mock_urlopen
    ):
        mock_loads.return_value = {"erro": True}

        self.assertIsNone(
            get_cep_information_from_address("SP", "Example", "Rua Example")
        )

    def test_get_cep_information_from_address_invalid_cep_dont_raise_exception_invalid_uf(
        self, mock_urlopen
    ):
        self.assertIsNone(
            get_cep_information_from_address("ABC", "Example", "Rua Example")
        )

    def test_get_cep_information_from_address_invalid_cep_raise_exception_invalid_uf(
        self, mock_urlopen
    ):
        with self.assertRaises(ValueError):
            get_cep_information_from_address(
                "ABC", "Example", "Rua Example", True
            )

    def test_get_cep_information_from_address_invalid_cep_raise_exception_cep_not_found(
        self, mock_urlopen
    ):
        mock_response = MagicMock()
        mock_response.read.return_value = {"erro": True}
        mock_urlopen.return_value = mock_response

        with self.assertRaises(CEPNotFound):
            get_cep_information_from_address(
                "SP", "Example", "Rua Example", True
            )


@patch("brutils.cep.urlopen")
class TestGetAddressFromCEP_MC_DC(TestCase):
    def test_ct1_cep_invalido_com_excecao(self, mock_urlopen):
        """CT1: cep inválido e raise_exceptions=True → lança InvalidCEP"""
        with self.assertRaises(InvalidCEP):
            get_address_from_cep("abcdefg", raise_exceptions=True)

    def test_ct2_cep_invalido_sem_excecao(self, mock_urlopen):
        """CT2: cep inválido e raise_exceptions=False → retorna None"""
        result = get_address_from_cep("abcdefg", raise_exceptions=False)
        self.assertIsNone(result)

    @patch("brutils.cep.loads")
    def test_ct3_cep_valido(self, mock_loads, mock_urlopen):
        """CT3: cep válido → retorna dicionário com endereço"""

        # A função get_address_from_cep faz dois loads() no mesmo JSON
        mock_loads.side_effect = [
            {"cep": "01001-000"},  # Primeiro loads para verificar "erro"
            {"cep": "01001-000"},  # Segundo loads para retornar Address
        ]

        # Simula a resposta da API ViaCEP
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"cep": "01001-000"}'

        # Corrige o mock para suportar o contexto "with urlopen(...) as f"
        mock_urlopen.return_value.__enter__.return_value = mock_response

        # Executa a chamada
        result = get_address_from_cep("01001000", raise_exceptions=False)

        # Valida o resultado
        self.assertIsInstance(result, dict)
        self.assertEqual(result.get("cep"), "01001-000")

    def test_ct4_erro_na_api_com_excecao(self, mock_urlopen):
        """CT4: cep válido mas inexistente + raise_exceptions=True → lança CEPNotFound"""
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"erro": true}'
        mock_urlopen.return_value = mock_response

        with self.assertRaises(CEPNotFound):
            get_address_from_cep("99999999", raise_exceptions=True)

    def test_ct5_erro_na_api_sem_excecao(self, mock_urlopen):
        """CT5: cep válido mas inexistente + raise_exceptions=False → retorna None"""
        mock_response = mock_urlopen.return_value
        mock_response.read.return_value = b'{"erro": true}'

        result = get_address_from_cep("99999999", raise_exceptions=False)
        self.assertIsNone(result)

    def test_ct6_viacep_responde_com_erro_e_raise_exceptions_true(
        self, mock_urlopen
    ):
        """
        CT6: cobre a linha 172 e a decisão CD2 (data.get("erro", True))
        """
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"erro": true}'
        mock_urlopen.return_value = mock_response

        with self.assertRaises(CEPNotFound):
            get_address_from_cep("01001000", raise_exceptions=True)


if __name__ == "__main__":
    main()

from datetime import datetime
from unittest import TestCase
from unittest.mock import patch

from num2words import num2words

from brutils import convert_date_to_text
from brutils.data.enums.months import MonthsEnum
from brutils.date_utils import is_holiday


class TestIsHoliday(TestCase):
    @patch("brutils.date_utils.is_holiday")
    def test_feriados_validos(self, mock_is_holiday):
        # Testes com feriados válidos
        mock_is_holiday.return_value = True
        self.assertTrue(is_holiday(datetime(2024, 1, 1)))  # Ano Novo
        self.assertTrue(
            is_holiday(datetime(2024, 7, 9), uf="SP")
        )  # Revolução Constitucionalista (SP)
        self.assertTrue(
            is_holiday(datetime(2024, 9, 7))
        )  # Independência do Brasil
        self.assertTrue(is_holiday(datetime(2025, 1, 1)))  # Ano Novo

    @patch("brutils.date_utils.is_holiday")
    def test_dias_normais(self, mock_is_holiday):
        # Testes com dias normais
        mock_is_holiday.return_value = False
        self.assertFalse(is_holiday(datetime(2024, 1, 2)))  # Dia normal
        self.assertFalse(
            is_holiday(datetime(2024, 7, 9), uf="RJ")
        )  # Dia normal no RJ

    @patch("brutils.date_utils.is_holiday")
    def test_data_invalida(self, mock_is_holiday):
        # Testes com data inválida
        mock_is_holiday.return_value = None
        self.assertIsNone(is_holiday("2024-01-01"))  # Formato incorreto
        self.assertIsNone(is_holiday(None))  # Data None

    @patch("brutils.date_utils.is_holiday")
    def test_uf_invalida(self, mock_is_holiday):
        # Testes com UF inválida
        mock_is_holiday.return_value = None
        self.assertIsNone(
            is_holiday(datetime(2024, 1, 1), uf="XX")
        )  # UF inválida
        self.assertIsNone(
            is_holiday(datetime(2024, 1, 1), uf="SS")
        )  # UF inválida

    @patch("brutils.date_utils.is_holiday")
    def test_limite_de_datas(self, mock_is_holiday):
        # Testes com limite de datas
        mock_is_holiday.return_value = True
        self.assertTrue(is_holiday(datetime(2024, 12, 25)))  # Natal
        self.assertTrue(
            is_holiday(datetime(2024, 11, 15))
        )  # Proclamação da República

    @patch("brutils.date_utils.is_holiday")
    def test_datas_depois_de_feriados(self, mock_is_holiday):
        # Test data after holidays
        mock_is_holiday.return_value = False
        self.assertFalse(is_holiday(datetime(2024, 12, 26)))  # Não é feriado
        self.assertFalse(is_holiday(datetime(2025, 1, 2)))  # Não é feriado

    @patch("brutils.date_utils.is_holiday")
    def test_ano_bissexto(self, mock_is_holiday):
        # Teste ano bissexto
        mock_is_holiday.return_value = False
        self.assertFalse(
            is_holiday(datetime(2024, 2, 29))
        )  # Não é feriado, mas data válida
        # Uncomment to test non-leap year invalid date
        # self.assertIsNone(is_holiday(datetime(1900, 2, 29)))  # Ano não bissexto, data inválida

    @patch("brutils.date_utils.is_holiday")
    def test_data_passada_futura(self, mock_is_holiday):
        # Teste de data passada e futura
        mock_is_holiday.return_value = True
        self.assertTrue(is_holiday(datetime(2023, 1, 1)))  # Ano anterior
        self.assertTrue(is_holiday(datetime(2100, 12, 25)))  # Ano futuro
        self.assertFalse(
            is_holiday(datetime(2100, 1, 2))
        )  # Dia normal em ano futuro

    @patch("brutils.date_utils.is_holiday")
    def test_data_sem_uf(self, mock_is_holiday):
        # Teste feriado nacional sem UF
        mock_is_holiday.return_value = True
        self.assertTrue(
            is_holiday(datetime(2024, 12, 25))
        )  # Natal, feriado nacional
        self.assertFalse(
            is_holiday(datetime(2024, 7, 9))
        )  # Data estadual de SP, sem UF


class TestNum2Words(TestCase):
    def test_num_conversion(self) -> None:
        """
        Smoke test of the num2words library.
        This test is used to guarantee that our dependency still works.
        """
        self.assertEqual(num2words(30, lang="pt-br"), "trinta")
        self.assertEqual(num2words(42, lang="pt-br"), "quarenta e dois")
        self.assertEqual(
            num2words(2024, lang="pt-br"), "dois mil e vinte e quatro"
        )
        self.assertEqual(num2words(0, lang="pt-br"), "zero")
        self.assertEqual(num2words(-1, lang="pt-br"), "menos um")


class TestConvertDateToText(TestCase):
    def test_convert_date_to_text(self):
        self.assertEqual(
            convert_date_to_text("15/08/2024"),
            "Quinze de agosto de dois mil e vinte e quatro",
        )
        self.assertEqual(
            convert_date_to_text("01/01/2000"),
            "Primeiro de janeiro de dois mil",
        )
        self.assertEqual(
            convert_date_to_text("31/12/1999"),
            "Trinta e um de dezembro de mil novecentos e noventa e nove",
        )

        self.assertIsNone(convert_date_to_text("30/02/2020"), None)
        self.assertIsNone(convert_date_to_text("30/00/2020"), None)
        self.assertIsNone(convert_date_to_text("30/02/2000"), None)
        self.assertIsNone(convert_date_to_text("50/09/2000"), None)
        self.assertIsNone(convert_date_to_text("25/15/2000"), None)
        self.assertIsNone(convert_date_to_text("29/02/2019"), None)

        # Invalid date pattern.
        self.assertIsNone(convert_date_to_text("Invalid"))
        self.assertIsNone(convert_date_to_text("25/1/2020"))
        self.assertIsNone(convert_date_to_text("1924/08/20"))
        self.assertIsNone(convert_date_to_text("5/09/2020"))
        self.assertIsNone(convert_date_to_text("00/09/2020"))
        self.assertIsNone(convert_date_to_text("32/09/2020"))

        self.assertEqual(
            convert_date_to_text("29/02/2020"),
            "Vinte e nove de fevereiro de dois mil e vinte",
        )
        self.assertEqual(
            convert_date_to_text("01/01/1900"),
            "Primeiro de janeiro de mil e novecentos",
        )

    months_year = [
        (1, "janeiro"),
        (2, "fevereiro"),
        (3, "marco"),
        (4, "abril"),
        (5, "maio"),
        (6, "junho"),
        (7, "julho"),
        (8, "agosto"),
        (9, "setembro"),
        (10, "outubro"),
        (11, "novembro"),
        (12, "dezembro"),
    ]

    def testMonthEnum(self):
        for number_month, name_month in self.months_year:
            month = MonthsEnum(number_month)
            self.assertEqual(month.month_name, name_month)

    def test_is_valid_month(self):
        for number_month, _ in self.months_year:
            self.assertTrue(MonthsEnum.is_valid_month(number_month))
        self.assertFalse(MonthsEnum.is_valid_month(0))
        self.assertFalse(MonthsEnum.is_valid_month(13))

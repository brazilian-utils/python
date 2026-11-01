from decimal import Decimal
from unittest import TestCase

from brutils.currency import convert_real_to_text, format_currency


class TestFormatCurrency(TestCase):
    def test_when_value_is_a_decimal_value(self):
        assert format_currency(Decimal("123236.70")) == "R$ 123.236,70"

    def test_when_value_is_a_float_value(self):
        assert format_currency(123236.70) == "R$ 123.236,70"

    def test_when_value_is_negative(self):
        assert format_currency(-123236.70) == "R$ -123.236,70"

    def test_when_value_is_zero(self):
        assert format_currency(0) == "R$ 0,00"

    def test_value_decimal_replace_rounding(self):
        assert format_currency(-123236.7676) == "R$ -123.236,77"

    def test_when_value_is_nan(self):
        assert format_currency(float("nan")) is None
        assert format_currency("nan") is None
        assert format_currency(Decimal("nan")) is None

    def test_when_value_is_infinite(self):
        assert format_currency(float("inf")) is None
        assert format_currency(float("-inf")) is None
        assert format_currency("-inf") is None

    def test_when_value_is_not_a_valid_currency(self):
        assert format_currency("not a number") is None
        assert format_currency("09809,87") is None
        assert format_currency("897L") is None


class TestConvertRealToText(TestCase):
    def test_convert_real_to_text(self):
        self.assertEqual(convert_real_to_text(0.00), "Zero reais")
        self.assertEqual(convert_real_to_text(0.01), "Um centavo")
        self.assertEqual(convert_real_to_text(0.50), "Cinquenta centavos")
        self.assertEqual(convert_real_to_text(1.00), "Um real")
        self.assertEqual(
            convert_real_to_text(-50.25),
            "Menos cinquenta reais e vinte e cinco centavos",
        )
        self.assertEqual(
            convert_real_to_text(1523.45),
            "Mil, quinhentos e vinte e três reais e quarenta e cinco centavos",
        )
        self.assertEqual(convert_real_to_text(1000000.00), "Um milhão de reais")
        self.assertEqual(
            convert_real_to_text(2000000.00), "Dois milhões de reais"
        )
        self.assertEqual(
            convert_real_to_text(1000000000.00), "Um bilhão de reais"
        )
        self.assertEqual(
            convert_real_to_text(2000000000.00), "Dois bilhões de reais"
        )
        self.assertEqual(
            convert_real_to_text(1000000000000.00), "Um trilhão de reais"
        )
        self.assertEqual(
            convert_real_to_text(2000000000000.00), "Dois trilhões de reais"
        )
        self.assertEqual(
            convert_real_to_text(1000000.45),
            "Um milhão de reais e quarenta e cinco centavos",
        )
        self.assertEqual(
            convert_real_to_text(2000000000.99),
            "Dois bilhões de reais e noventa e nove centavos",
        )
        self.assertEqual(
            convert_real_to_text(1234567890.50),
            "Um bilhão, duzentos e trinta e quatro milhões, quinhentos e sessenta e sete mil, oitocentos e noventa reais e cinquenta centavos",
        )

        # Almost zero values
        self.assertEqual(convert_real_to_text(0.001), "Zero reais")
        self.assertEqual(convert_real_to_text(0.009), "Zero reais")

        # Negative milions
        self.assertEqual(
            convert_real_to_text(-1000000.00), "Menos um milhão de reais"
        )
        self.assertEqual(
            convert_real_to_text(-2000000.50),
            "Menos dois milhões de reais e cinquenta centavos",
        )

        # billions with cents
        self.assertEqual(
            convert_real_to_text(1000000000.01),
            "Um bilhão de reais e um centavo",
        )
        self.assertEqual(
            convert_real_to_text(1000000000.99),
            "Um bilhão de reais e noventa e nove centavos",
        )

        self.assertEqual(
            convert_real_to_text(999999999999.99),
            "Novecentos e noventa e nove bilhões, novecentos e noventa e nove milhões, novecentos e noventa e nove mil, novecentos e noventa e nove reais e noventa e nove centavos",
        )

        # trillions with cents
        self.assertEqual(
            convert_real_to_text(1000000000000.01),
            "Um trilhão de reais e um centavo",
        )
        self.assertEqual(
            convert_real_to_text(1000000000000.99),
            "Um trilhão de reais e noventa e nove centavos",
        )
        self.assertEqual(
            convert_real_to_text(9999999999999.99),
            "Nove trilhões, novecentos e noventa e nove bilhões, novecentos e noventa e nove milhões, novecentos e noventa e nove mil, novecentos e noventa e nove reais e noventa e nove centavos",
        )

        # 1 quadrillion
        self.assertEqual(
            convert_real_to_text(1000000000000000.00),
            "Um quatrilhão de reais",
        )

        # Edge cases should return None
        self.assertIsNone(
            convert_real_to_text("invalid_value")
        )  # invalid value
        self.assertIsNone(convert_real_to_text(None))  # None value
        self.assertIsNone(
            convert_real_to_text(-1000000000000001.00)
        )  # less than -1 quadrillion
        self.assertIsNone(
            convert_real_to_text(-1000000000000001.00)
        )  # more than 1 quadrillion
        self.assertIsNone(convert_real_to_text(float("inf")))  # Infinity
        self.assertIsNone(
            convert_real_to_text(float("nan"))
        )  # Not a number (NaN)

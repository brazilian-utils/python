from unittest import TestCase, main
from unittest.mock import patch

from brutils.license_plate import (
    _is_valid_mercosul,
    _is_valid_old_format,
    convert_to_mercosul,
    format_license_plate,
    generate,
    get_format,
    remove_symbols,
)


class TestLicensePlate(TestCase):
    def test_remove_symbols(self):
        self.assertEqual(remove_symbols("ABC-123"), "ABC123")
        self.assertEqual(remove_symbols("abc123"), "abc123")
        self.assertEqual(remove_symbols("ABCD123"), "ABCD123")
        self.assertEqual(remove_symbols("A-B-C-1-2-3"), "ABC123")
        self.assertEqual(remove_symbols("@abc#-#123@"), "@abc##123@")
        self.assertEqual(remove_symbols("@---#"), "@#")
        self.assertEqual(remove_symbols("---"), "")

    def test_convert_license_plate_to_mercosul(self):
        # when license plate is not an instance of string, returns None
        self.assertIsNone(convert_to_mercosul(1234567))

        # when license plate has a length different from 7, returns None
        self.assertIsNone(convert_to_mercosul("ABC123"))
        self.assertIsNone(convert_to_mercosul("ABC12356"))

        # when then license plate's 5th character is not a number, return None
        self.assertIsNone(convert_to_mercosul("ABC1A34"))
        self.assertIsNone(convert_to_mercosul("ABC1-34"))
        self.assertIsNone(convert_to_mercosul("ABC1*34"))
        self.assertIsNone(convert_to_mercosul("ABC1_34"))
        self.assertIsNone(convert_to_mercosul("ABC1%34"))
        self.assertIsNone(convert_to_mercosul("ABC1 34"))

        # when then license plate's 5th character is 0, return with a letter A
        self.assertEqual(convert_to_mercosul("AAA1011"), "AAA1A11")
        # when then license plate's 5th character is 1, return with a letter B
        self.assertEqual(convert_to_mercosul("AAA1111"), "AAA1B11")
        # when then license plate's 5th character is 2, return with a letter C
        self.assertEqual(convert_to_mercosul("AAA1211"), "AAA1C11")
        # when then license plate's 5th character is 3, return with a letter D
        self.assertEqual(convert_to_mercosul("AAA1311"), "AAA1D11")
        # when then license plate's 5th character is 4, return with a letter E
        self.assertEqual(convert_to_mercosul("AAA1411"), "AAA1E11")
        # when then license plate's 5th character is 5, return with a letter F
        self.assertEqual(convert_to_mercosul("AAA1511"), "AAA1F11")
        # when then license plate's 5th character is 6, return with a letter G
        self.assertEqual(convert_to_mercosul("AAA1611"), "AAA1G11")
        # when then license plate's 5th character is 7, return with a letter H
        self.assertEqual(convert_to_mercosul("AAA1711"), "AAA1H11")
        # when then license plate's 5th character is 8, return with a letter I
        self.assertEqual(convert_to_mercosul("AAA1811"), "AAA1I11")
        # when then license plate's 5th character is 9, return with a letter J
        self.assertEqual(convert_to_mercosul("AAA1911"), "AAA1J11")

        # when then license is provided in lowercase, it's correctly converted
        # and then returned value is in uppercase
        self.assertEqual(convert_to_mercosul("abc1234"), "ABC1C34")

    def test_format_license_plate(self):
        self.assertEqual(format_license_plate("ABC1234"), "ABC-1234")
        self.assertEqual(format_license_plate("abc1234"), "ABC-1234")
        self.assertEqual(format_license_plate("ABC1D23"), "ABC1D23")
        self.assertEqual(format_license_plate("abc1d23"), "ABC1D23")
        # When license place isn't valid, raises ValueError
        with self.assertRaises(ValueError):
            format_license_plate("ABCD123")

    def test_get_format(self):
        # Old format
        self.assertEqual(get_format("ABC1234"), "LLLNNNN")
        self.assertEqual(get_format("abc1234"), "LLLNNNN")

        # Mercosul
        self.assertEqual(get_format("ABC4E67"), "LLLNLNN")
        self.assertEqual(get_format("XXX9X99"), "LLLNLNN")

        # Invalid
        self.assertIsNone(get_format(None))
        self.assertIsNone(get_format(""))
        self.assertIsNone(get_format("ABC-1D23"))
        self.assertIsNone(get_format("invalid plate"))

    def test_generate_license_plate(self):
        with patch("brutils.license_plate.choice", return_value="X"):
            with patch("brutils.license_plate.randint", return_value=9):
                self.assertEqual(generate(format="LLLNNNN"), "XXX9999")
                self.assertEqual(generate(format="LLLNLNN"), "XXX9X99")

        for _ in range(10_000):
            self.assertTrue(_is_valid_mercosul(generate(format="LLLNLNN")))

        for _ in range(10_000):
            self.assertTrue(_is_valid_old_format(generate(format="LLLNNNN")))

        # When no format is provided, returns a valid Mercosul license plate
        self.assertTrue(_is_valid_mercosul(generate()))

        # When invalid format is provided, returns None
        self.assertIsNone(generate("LNLNLNL"))


if __name__ == "__main__":
    main()

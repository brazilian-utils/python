from unittest import TestCase, main
from unittest.mock import patch

from brutils.license_plate import (
    _is_valid_mercosul,
    _is_valid_old_format,
    is_valid,
)


@patch("brutils.license_plate._is_valid_mercosul")
@patch("brutils.license_plate._is_valid_old_format")
class TestIsValidWithTypeOldFormat(TestCase):
    def test_when_old_format_is_valid_returns_true(
        self, mock__is_valid_old_format, mock__is_valid_mercosul
    ):
        mock__is_valid_old_format.return_value = True

        self.assertIs(is_valid("ABC1234", "old_format"), True)
        mock__is_valid_old_format.assert_called_once_with("ABC1234")
        mock__is_valid_mercosul.assert_not_called()

    def test_when_old_format_is_not_valid_returns_false(
        self, mock__is_valid_old_format, mock__is_valid_mercosul
    ):
        mock__is_valid_old_format.return_value = False

        self.assertIs(is_valid("123456", "old_format"), False)
        mock__is_valid_old_format.assert_called_once_with("123456")
        mock__is_valid_mercosul.assert_not_called()


@patch("brutils.license_plate._is_valid_mercosul")
@patch("brutils.license_plate._is_valid_old_format")
class TestIsValidWithTypeMercosul(TestCase):
    def test_when_mercosul_is_valid_returns_true(
        self, mock__is_valid_old_format, mock__is_valid_mercosul
    ):
        mock__is_valid_mercosul.return_value = True

        self.assertIs(is_valid("ABC4E67", "mercosul"), True)
        mock__is_valid_mercosul.assert_called_once_with("ABC4E67")
        mock__is_valid_old_format.assert_not_called()

    def test_when_mercosul_is_not_valid_returns_false(
        self, mock__is_valid_old_format, mock__is_valid_mercosul
    ):
        mock__is_valid_mercosul.return_value = False

        self.assertIs(is_valid("11994029275", "mercosul"), False)
        mock__is_valid_mercosul.assert_called_once_with("11994029275")
        mock__is_valid_old_format.assert_not_called()


@patch("brutils.license_plate._is_valid_mercosul")
@patch("brutils.license_plate._is_valid_old_format")
class TestIsValidWithTypeNone(TestCase):
    def test_when_mercosul_valid_old_format_invalid(
        self, mock__is_valid_old_format, mock__is_valid_mercosul
    ):
        mock__is_valid_mercosul.return_value = True
        mock__is_valid_old_format.return_value = False

        self.assertIs(is_valid("ABC4E67"), True)
        mock__is_valid_old_format.assert_called_once_with("ABC4E67")
        mock__is_valid_mercosul.assert_called_once_with("ABC4E67")

    def test_when_mercosul_and_old_format_are_valids(
        self, mock__is_valid_old_format, mock__is_valid_mercosul
    ):
        mock__is_valid_mercosul.return_value = True
        mock__is_valid_old_format.return_value = True

        self.assertIs(is_valid("ABC1234"), True)
        mock__is_valid_mercosul.assert_not_called()
        mock__is_valid_old_format.assert_called_once_with("ABC1234")

    def test_when_mercosul_invalid_old_format_valid(
        self, mock__is_valid_old_format, mock__is_valid_mercosul
    ):
        mock__is_valid_mercosul.return_value = False
        mock__is_valid_old_format.return_value = True

        self.assertIs(is_valid("ABC1234"), True)
        mock__is_valid_old_format.assert_called_once_with("ABC1234")
        mock__is_valid_mercosul.assert_not_called()

    def test_when_mercosul_and_old_format_are_invalid(
        self, mock__is_valid_old_format, mock__is_valid_mercosul
    ):
        mock__is_valid_old_format.return_value = False
        mock__is_valid_mercosul.return_value = False

        self.assertIs(is_valid("ABC1234"), False)
        mock__is_valid_old_format.assert_called_once_with("ABC1234")
        mock__is_valid_mercosul.assert_called_once_with("ABC1234")


class TestIsValidOldFormat(TestCase):
    def test__is_valid_old_format(self):
        # When license plate is valid, returns True
        self.assertIs(_is_valid_old_format("ABC1234"), True)
        self.assertIs(_is_valid_old_format("abc1234"), True)

        # When license plate is valid with whitespaces, returns True
        self.assertIs(_is_valid_old_format(" ABC1234    "), True)

        # When license plate is not string, returns False
        self.assertIs(_is_valid_old_format(123456), False)

        # When license plate is invalid with special characters,
        # returns False
        self.assertIs(_is_valid_old_format("ABC-1234"), False)

        # When license plate is invalid with numbers and letters out of
        # order, returns False
        self.assertIs(_is_valid_old_format("A1CA23W"), False)

        # When license plate is invalid with new format, returns False
        self.assertIs(_is_valid_old_format("ABC1D23"), False)
        self.assertIs(_is_valid_old_format("abcd123"), False)


class TestIsValidMercosul(TestCase):
    def test__is_valid_mercosul(self):
        # When license plate is not string, returns False
        self.assertIs(_is_valid_mercosul(1234567), False)

        # When license plate doesn't match the pattern LLLNLNN,
        # returns False
        self.assertIs(_is_valid_mercosul("ABCDEFG"), False)
        self.assertIs(_is_valid_mercosul("1234567"), False)
        self.assertIs(_is_valid_mercosul("ABC4567"), False)
        self.assertIs(_is_valid_mercosul("ABCD567"), False)
        self.assertIs(_is_valid_mercosul("ABC45F7"), False)
        self.assertIs(_is_valid_mercosul("ABC456G"), False)
        self.assertIs(_is_valid_mercosul("ABC123"), False)

        # When license plate is an empty string, returns False
        self.assertIs(_is_valid_mercosul(""), False)

        # When license plate's length is different of 7, returns False
        self.assertIs(_is_valid_mercosul("ABC4E678"), False)

        # When license plate has separator, returns false
        self.assertIs(_is_valid_mercosul("ABC-1D23"), False)

        # When license plate contains digits from other alphabets,
        # returns False
        self.assertIs(_is_valid_mercosul("ABC٤E٦٧"), False)
        self.assertIs(_is_valid_mercosul("ABC４E６７"), False)

        # When license plate is valid
        self.assertIs(_is_valid_mercosul("ABC4E67"), True)
        self.assertIs(_is_valid_mercosul("AAA1A11"), True)
        self.assertIs(_is_valid_mercosul("XXX9X99"), True)

        # Check if function is case insensitive
        self.assertIs(_is_valid_mercosul("abc4e67"), True)


if __name__ == "__main__":
    main()

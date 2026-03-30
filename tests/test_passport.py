from unittest import TestCase, main
from unittest.mock import patch

from brutils.passport import format_passport, generate, is_valid, remove_symbols


class TestCPF(TestCase):
    def test_is_valid(self):
        # When passport is not string, returns False
        self.assertIs(is_valid(1), False)  # type: ignore

        # When passport's len is different of 8, returns False
        self.assertIs(is_valid("1"), False)

        # When passport does not contain only digits, returns False
        self.assertIs(is_valid("1112223334-"), False)

        # When cpf is valid
        self.assertIs(is_valid("AA111111"), True)
        self.assertIs(is_valid("CL125167"), True)

    def test_generate(self):
        for _ in range(10_000):
            self.assertIs(is_valid(generate()), True)

    def test_remove_symbols(self):
        # When there are no symbols, returns the same string
        self.assertEqual(remove_symbols("Ab123456"), "Ab123456")

        # When there are spaces, returns the string without them
        self.assertEqual(remove_symbols(" AB 123 456 "), "AB123456")

        # When there are dashes, returns the string without them
        self.assertEqual(remove_symbols("-AB1-23-4-56-"), "AB123456")

        # When there are dots, returns the string without them
        self.assertEqual(remove_symbols(".AB.1.23.456."), "AB123456")

        # When there are multiple symbols, returns the string without any of them
        self.assertEqual(remove_symbols(".A B.1.2-3.45 -. 6."), "AB123456")


@patch("brutils.passport.is_valid")
class TestIsValidToFormat(TestCase):
    def test_when_passport_is_valid_returns_true_to_format(self, mock_is_valid):
        mock_is_valid.return_value = True

        # When passport is_valid, returns formatted passport
        self.assertEqual(format_passport("yz 987654"), "YZ987654")

        # Checks if function is_valid_passport is called
        mock_is_valid.assert_called_once_with("YZ987654")

    def test_when_cpf_is_not_valid_returns_none(self, mock_is_valid):
        mock_is_valid.return_value = False

        # When passport isn't valid, returns None
        self.assertIsNone(format_passport("acd12736"))


if __name__ == "__main__":
    main()

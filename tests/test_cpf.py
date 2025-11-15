from unittest import TestCase, main
from unittest.mock import patch

from brutils.cpf import (
    _checksum,
    _hashdigit,
    display,
    format_cpf,
    generate,
    is_valid,
    remove_symbols,
    sieve,
    validate,
)


class TestCPF(TestCase):
    def test_sieve(self):
        self.assertEqual(sieve("00000000000"), "00000000000")
        self.assertEqual(sieve("123.456.789-10"), "12345678910")
        self.assertEqual(sieve("134..2435.-1892.-"), "13424351892")
        self.assertEqual(sieve("abc1230916*!*&#"), "abc1230916*!*&#")
        self.assertEqual(
            sieve("ab.c1.--.2-309.-1-.6-.*.-!*&#"), "abc1230916*!*&#"
        )
        self.assertEqual(sieve("...---..."), "")

    def test_display(self):
        self.assertEqual(display("00000000011"), "000.000.000-11")
        self.assertIsNone(display("00000000000"))
        self.assertIsNone(display("0000000000a"))
        self.assertIsNone(display("000000000000"))

    def test_validate(self):
        self.assertIs(validate("52513127765"), True)
        self.assertIs(validate("52599927765"), True)
        self.assertIs(validate("00000000000"), False)

    def test_is_valid(self):
        # When cpf is not string, returns False
        self.assertIs(is_valid(1), False)

        # When cpf's len is different of 11, returns False
        self.assertIs(is_valid("1"), False)

        # When cpf does not contain only digits, returns False
        self.assertIs(is_valid("1112223334-"), False)

        # When CPF has only the same digit, returns false
        self.assertIs(is_valid("11111111111"), False)

        # When rest_1 is lt 2 and the 10th digit is not 0, returns False
        self.assertIs(is_valid("11111111215"), False)

        # When rest_1 is gte 2 and the 10th digit is not (11 - rest), returns
        # False
        self.assertIs(is_valid("11144477705"), False)

        # When rest_2 is lt 2 and the 11th digit is not 0, returns False
        self.assertIs(is_valid("11111111204"), False)

        # When rest_2 is gte 2 and the 11th digit is not (11 - rest), returns
        # False
        self.assertIs(is_valid("11144477732"), False)

        # When cpf is valid
        self.assertIs(is_valid("11144477735"), True)
        self.assertIs(is_valid("11111111200"), True)

    def test_generate(self):
        for _ in range(10_000):
            self.assertIs(validate(generate()), True)
            self.assertIsNotNone(display(generate()))

    def test__hashdigit(self):
        self.assertEqual(_hashdigit("000000000", 10), 0)
        self.assertEqual(_hashdigit("0000000000", 11), 0)
        self.assertEqual(_hashdigit("52513127765", 10), 6)
        self.assertEqual(_hashdigit("52513127765", 11), 5)

    def test_checksum(self):
        self.assertEqual(_checksum("000000000"), "00")
        self.assertEqual(_checksum("525131277"), "65")


@patch("brutils.cpf.sieve")
class TestRemoveSymbols(TestCase):
    def test_remove_symbols(self, mock_sieve):
        # When call remove_symbols, it calls sieve
        remove_symbols("123.456.789-10")
        mock_sieve.assert_called()


@patch("brutils.cpf.is_valid")
class TestIsValidToFormat(TestCase):
    def test_when_cpf_is_valid_returns_true_to_format(self, mock_is_valid):
        mock_is_valid.return_value = True

        # When cpf is_valid, returns formatted cpf
        self.assertEqual(format_cpf("11144477735"), "111.444.777-35")

        # Checks if function is_valid_cpf is called
        mock_is_valid.assert_called_once_with("11144477735")

    def test_when_cpf_is_not_valid_raises_value_error(self, mock_is_valid):
        mock_is_valid.return_value = False

        # When cpf isn't valid, raises ValueError
        with self.assertRaises(ValueError):
            format_cpf("11144477735")


if __name__ == "__main__":
    main()

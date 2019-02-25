from unittest import TestCase
from brazilian_utils import cpf
from constant import BLACKLIST


class TestCPF(TestCase):
    def test_cpf_in_blacklist(self):
        for c in BLACKLIST:
            with self.subTest():
                self.assertFalse(cpf.is_valid(c))

    def test_is_digit(self):
        self.assertFalse(cpf.is_valid("ABC9123DF12312"))

    def test_is_empty_or_None(self):
        self.assertFalse(cpf.is_valid(""))
        self.assertFalse(cpf.is_valid(None))

    def test_has_11_digits(self):
        self.assertFalse(cpf.is_valid("123"))
        self.assertFalse(cpf.is_valid("12345678901236"))

    def test_validate_first_digit(self):
        self.assertEqual(cpf.validate_first_digit("12345678901"), 0)
        self.assertEqual(cpf.validate_first_digit("52998224725"), 2)

    def test_validate_second_digit(self):
        self.assertEqual(cpf.validate_second_digit("12345678901"), 9)
        self.assertEqual(cpf.validate_second_digit("52998224725"), 5)

    def test_is_valid(self):
        self.assertTrue(cpf.is_valid("58756403240"))
        self.assertTrue(cpf.is_valid("71746540532"))
        self.assertFalse(cpf.is_valid("71746540531"))
        self.assertFalse(cpf.is_valid("58756403257"))

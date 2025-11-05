from unittest import TestCase

from brutils.renavam import is_valid_renavam


class TestRENAVAM(TestCase):
    def test_is_valid_renavam(self):
        self.assertTrue(is_valid_renavam("86769597308"))
        self.assertFalse(is_valid_renavam("12345678901"))
        self.assertFalse(is_valid_renavam("1234567890a"))
        self.assertFalse(is_valid_renavam("12345678 901"))
        self.assertFalse(is_valid_renavam("12345678"))
        self.assertFalse(is_valid_renavam(""))
        self.assertFalse(is_valid_renavam("123456789012"))
        self.assertFalse(is_valid_renavam("abcdefghijk"))
        self.assertFalse(is_valid_renavam("12345678901!"))
        self.assertFalse(is_valid_renavam("00000000000"))
        self.assertFalse(is_valid_renavam("11111111111"))

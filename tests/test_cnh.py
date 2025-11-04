from unittest import TestCase

from brutils.cnh import is_valid_cnh


class TestCNH(TestCase):
    def test_is_valid_cnh(self):
        self.assertFalse(is_valid_cnh("22222222222"))
        self.assertFalse(is_valid_cnh("ABC70304734"))
        self.assertFalse(is_valid_cnh("6619558737912"))
        self.assertTrue(is_valid_cnh("097703047-34"))
        self.assertTrue(is_valid_cnh("09770304734"))

from unittest import TestCase

from brutils.cnh import is_valid_cnh


class TestCNH(TestCase):
    def test_is_valid_cnh(self):
        self.assertFalse(is_valid_cnh("22222222222"))
        self.assertFalse(is_valid_cnh("ABC70304734"))
        self.assertFalse(is_valid_cnh("6619558737912"))
        self.assertTrue(is_valid_cnh("097703047-34"))
        self.assertTrue(is_valid_cnh("09770304734"))

    def test_is_valid_cnh_when_first_verificator_remainder_is_greater_than_9(
        self,
    ):
        # When the remainder of the first verification digit is 10, that digit
        # is printed as 0 and the second one must be calculated with a discount
        # of 2. These CNHs are valid and were rejected before the fix.
        self.assertTrue(is_valid_cnh("51106130609"))
        self.assertTrue(is_valid_cnh("71776598807"))
        self.assertTrue(is_valid_cnh("22342625204"))

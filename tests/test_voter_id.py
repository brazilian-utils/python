from unittest import TestCase, main

from brutils.voter_id import (
    _calculate_vd1,
    _calculate_vd2,
    _get_federative_union,
    _get_sequential_number,
    _get_verifying_digits,
    _is_length_valid,
    format_voter_id,
    generate,
    is_valid,
)


class TestIsValid(TestCase):
    def test_valid_voter_id(self):
        # test a valid voter id number
        voter_id = "217633460930"
        self.assertIs(is_valid(voter_id), True)
        self.assertIsInstance(is_valid(voter_id), bool)

    def test_invalid_voter_id(self):
        # test an invalid voter id number (dv1 & UF fail)
        voter_id = "123456789011"
        self.assertIs(is_valid(voter_id), False)

    def test_invalid_length(self):
        # Test an invalid length for voter id
        invalid_length_short = "12345678901"
        invalid_length_long = "1234567890123"
        self.assertIs(is_valid(invalid_length_short), False)
        self.assertIs(is_valid(invalid_length_long), False)

    def test_invalid_characters(self):
        # Test voter id with non-numeric characters
        invalid_characters = "ABCD56789012"
        invalid_characters_space = "217633 460 930"
        self.assertIs(is_valid(invalid_characters), False)
        self.assertIs(is_valid(invalid_characters_space), False)

    def test_valid_special_case(self):
        # Test a valid edge case (SP & MG with 13 digits)
        valid_special = "3244567800167"
        self.assertIs(is_valid(valid_special), True)

    def test_invalid_vd1(self):
        voter_id = "427503840223"
        self.assertIs(is_valid(voter_id), False)

    def test_invalid_vd2(self):
        voter_id = "427503840214"
        self.assertIs(is_valid(voter_id), False)

    def test_get_voter_id_parts(self):
        voter_id = "12345678AB12"

        sequential_number = _get_sequential_number(voter_id)
        federative_union = _get_federative_union(voter_id)
        verifying_digits = _get_verifying_digits(voter_id)

        self.assertEqual(sequential_number, "12345678")
        self.assertIsInstance(sequential_number, str)

        self.assertEqual(federative_union, "AB")
        self.assertIsInstance(federative_union, str)

        self.assertEqual(verifying_digits, "12")
        self.assertIsInstance(verifying_digits, str)

    def test_valid_length_verify(self):
        voter_id = "123456789012"
        self.assertIs(_is_length_valid(voter_id), True)
        self.assertIsInstance(_is_length_valid(voter_id), bool)

    def test_invalid_length_verify(self):
        voter_id = "12345678AB123"  # Invalid length
        self.assertIs(_is_length_valid(voter_id), False)

    def test_calculate_vd1(self):
        self.assertIs(_calculate_vd1("07881476", "03"), 6)

        # test edge case: when federative union is SP and rest is 0, declare vd1 as 1
        self.assertIs(_calculate_vd1("73146499", "01"), 1)
        # test edge case: when federative union is MG and rest is 0, declare vd1 as 1
        self.assertIs(_calculate_vd1("42750359", "02"), 1)
        # test edge case: rest is 10, declare vd1 as 0
        self.assertIs(_calculate_vd1("73146415", "03"), 0)
        self.assertIsInstance(_calculate_vd1("73146415", "03"), int)

    def test_calculate_vd2(self):
        self.assertIs(_calculate_vd2("02", 7), 2)
        # edge case: if rest == 10, declare vd2 as zero
        self.assertIs(_calculate_vd2("03", 7), 0)
        # edge case: if UF is "01" (for SP) and rest == 0
        # declare dv2 as 1 instead
        self.assertIs(_calculate_vd2("01", 4), 1)
        # edge case: if UF is "02" (for MG) and rest == 0
        # declare dv2 as 1 instead
        self.assertIs(_calculate_vd2("02", 8), 1)
        self.assertIsInstance(_calculate_vd2("02", 8), int)

    def test_generate_voter_id(self):
        # test if is_valid a voter id from MG
        voter_id = generate(federative_union="MG")
        self.assertIs(is_valid(voter_id), True)

        # test if is_valid a voter id from AC
        voter_id = generate(federative_union="AC")
        self.assertIs(is_valid(voter_id), True)

        # test if is_valid a voter id from foreigner
        voter_id = generate()
        self.assertIs(is_valid(voter_id), True)
        self.assertIsInstance(voter_id, str)

        # test if UF is not valid
        voter_id = generate(federative_union="XX")
        self.assertIs(is_valid(voter_id), False)
        self.assertIsNone(voter_id)

    def test_format_voter_id(self):
        self.assertEqual(format_voter_id("277627122852"), "2776 2712 28 52")
        self.assertIsInstance(format_voter_id("277627122852"), str)
        self.assertIsNone(format_voter_id("00000000000"))
        self.assertIsNone(format_voter_id("0000000000a"))
        self.assertIsNone(format_voter_id("000000000000"))
        self.assertIsNone(format_voter_id("800911840197"))


if __name__ == "__main__":
    main()

from unittest import TestCase, main
from unittest.mock import patch

from brutils.cns import (
    _generate_definitive,
    _generate_provisional,
    _weighted_sum,
    format_cns,
    generate,
    is_valid,
    remove_symbols,
)


class TestCNS(TestCase):
    def test_is_valid(self):
        # When CNS is not a string, returns False
        self.assertIs(is_valid(1), False)
        self.assertIs(is_valid([]), False)
        self.assertIs(is_valid({}), False)
        self.assertIs(is_valid(None), False)

        # When CNS's len is different of 15, returns False
        self.assertIs(is_valid("12345678901234"), False)
        self.assertIs(is_valid("1234567890123456"), False)

        # When CNS does not contain only digits, returns False
        self.assertIs(is_valid("12345678901234x"), False)

        # When the first digit does not match a known CNS format, returns False
        self.assertIs(is_valid("323456789012345"), False)
        self.assertIs(is_valid("000000000000000"), False)

        # When the "definitive" fixed segment ("00" + flag digit) is wrong,
        # returns False even if some digit sequence looks plausible
        self.assertIs(is_valid("123456789012345"), False)

        # When checksum digit doesn't match, returns False
        self.assertIs(is_valid("161243374450005"), False)
        self.assertIs(is_valid("905885616557481"), False)

        # When CNS is valid (definitive, starts with 1 or 2)
        self.assertIs(is_valid("161243374450004"), True)

        # When CNS is valid (provisional, starts with 7, 8 or 9)
        self.assertIs(is_valid("905885616557480"), True)

    def test_weighted_sum(self):
        self.assertEqual(_weighted_sum("161243374450004"), 374)
        self.assertEqual(_weighted_sum("12345678901"), 440)

    def test_generate_definitive(self):
        for _ in range(10_000):
            cns = _generate_definitive()
            self.assertIs(is_valid(cns), True)
            self.assertIn(cns[0], ("1", "2"))

    def test_generate_provisional(self):
        for _ in range(10_000):
            cns = _generate_provisional()
            self.assertIs(is_valid(cns), True)
            self.assertIn(cns[0], ("7", "8", "9"))

    def test_generate(self):
        self.assertIn(generate()[0], ("1", "2"))
        self.assertIn(generate(is_final=False)[0], ("7", "8", "9"))
        self.assertIs(is_valid(generate()), True)
        self.assertIs(is_valid(generate(is_final=False)), True)

    def test_remove_symbols(self):
        self.assertEqual(
            remove_symbols("898 0032 6314 4970"), "898003263144970"
        )
        self.assertEqual(remove_symbols("898003263144970"), "898003263144970")
        self.assertEqual(remove_symbols("134..2435/.-1892.-"), "1342435/1892")
        self.assertEqual(remove_symbols("...---..."), "")

    @patch("brutils.cns.is_valid")
    def test_format_valid_cns(self, mock_is_valid):
        mock_is_valid.return_value = True

        # When CNS is_valid, returns formatted CNS
        self.assertEqual(format_cns("161243374450004"), "161 2433 7445 0004")

        # Checks if function is_valid is called
        mock_is_valid.assert_called_once_with("161243374450004")

    @patch("brutils.cns.is_valid")
    def test_format_invalid_cns(self, mock_is_valid):
        mock_is_valid.return_value = False

        # When CNS isn't valid, returns None
        self.assertIsNone(format_cns("161243374450004"))


if __name__ == "__main__":
    main()

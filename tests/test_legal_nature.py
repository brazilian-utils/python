from unittest import TestCase, main

from brutils.legal_nature import (
    LEGAL_NATURE,
    get_description,
    is_valid,
    list_all,
)


class TestNaturezaJuridica(TestCase):
    def test_is_valid_non_string(self):
        # When input is not string, returns False
        self.assertIs(is_valid(1234), False)
        self.assertIs(is_valid(None), False)
        self.assertIs(is_valid([]), False)
        self.assertIs(is_valid({}), False)

    def test_is_valid_invalid_patterns(self):
        # Wrong length after normalization or contains no digits
        self.assertIs(is_valid(""), False)
        self.assertIs(is_valid("20"), False)
        self.assertIs(is_valid("20623"), False)
        self.assertIs(is_valid("abcd"), False)
        self.assertIs(is_valid("---"), False)

    def test_is_valid_formats_hyphen_and_plain(self):
        # Accept both "NNNN" and "NNN-N" formats
        self.assertTrue(is_valid("2062"))
        self.assertTrue(is_valid("206-2"))
        self.assertTrue(is_valid("101-5"))
        self.assertTrue(is_valid("1015"))

    def test_is_valid_known_codes_true(self):
        # A few known valid codes from different sections
        for code in (
            "1015",
            "2062",
            "2143",
            "2305",
            "3034",
            "3131",
            "3212",
            "4014",
            "5002",
        ):
            self.assertTrue(is_valid(code))

    def test_get_description_known(self):
        self.assertEqual(
            get_description("2062"), "Sociedade Empresária Limitada"
        )
        self.assertEqual(
            get_description("101-5"), "Órgão Público do Poder Executivo Federal"
        )
        self.assertEqual(get_description("2143"), "Cooperativa")
        self.assertEqual(
            get_description("5002"),
            "Organização Internacional e Outras Instituições Extraterritoriais",
        )

    def test_get_description_invalid(self):
        self.assertIsNone(get_description("9999"))
        self.assertIsNone(get_description("0000"))
        self.assertIsNone(get_description("20A2"))
        self.assertIsNone(get_description(None))  # type: ignore[arg-type]

    def test_table_integrity(self):
        # Dictionary should contain only 4-digit string keys and string descriptions
        for k, v in LEGAL_NATURE.items():
            self.assertIsInstance(k, str)
            self.assertTrue(
                k.isdigit() and len(k) == 4, msg=f"Invalid key: {k}"
            )
            self.assertIsInstance(v, str)
            self.assertTrue(len(v) > 0)

    def test_list_all_returns_copy(self):
        data = list_all()
        self.assertEqual(data["2062"], "Sociedade Empresária Limitada")
        data["2062"] = "X"
        self.assertEqual(LEGAL_NATURE["2062"], "Sociedade Empresária Limitada")


if __name__ == "__main__":
    main()

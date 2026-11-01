from unittest import TestCase, main

from brutils.phone import (
    _is_valid_landline,
    _is_valid_mobile,
    format_phone,
    generate,
    is_valid,
    remove_international_dialing_code,
    remove_symbols_phone,
)


class TestPhone(TestCase):
    def test_remove_symbols_phone(self):
        # When the string empty, it returns an empty string
        self.assertEqual(remove_symbols_phone(""), "")

        # When there are no symbols to remove, it returns the same string
        self.assertEqual(remove_symbols_phone("21994029275"), "21994029275")

        # When there are symbols to remove, it returns the string without
        # symbols
        self.assertEqual(remove_symbols_phone("(21)99402-9275"), "21994029275")
        self.assertEqual(remove_symbols_phone("(21)2569-6969"), "2125696969")

        # When there are extra symbols, it only removes the specified symbols
        self.assertEqual(
            remove_symbols_phone("(21) 99402-9275!"), "21994029275!"
        )

        # When the string contains non-numeric characters, it returns the
        # string without the specified symbols
        self.assertEqual(remove_symbols_phone("(21)ABC-DEF"), "21ABCDEF")

        # When the phone number contains a plus symbol and spaces, they are
        # removed
        self.assertEqual(
            remove_symbols_phone("+55 21 99402-9275"), "5521994029275"
        )

        # When the phone number contains multiple spaces, all are removed
        self.assertEqual(
            remove_symbols_phone("55 21  99402 9275"), "5521994029275"
        )

        # When the phone number contains a mixture of all specified symbols,
        # all are removed
        self.assertEqual(
            remove_symbols_phone("+55 (21) 99402-9275"), "5521994029275"
        )

    def test_format_phone_number(self):
        # When is a invalid number
        self.assertEqual(format_phone("333333"), None)

        # When is a mobile number
        self.assertEqual(format_phone("21994029275"), "(21)99402-9275")
        self.assertEqual(format_phone("21994029275"), "(21)99402-9275")
        self.assertEqual(format_phone("21994029275"), "(21)99402-9275")
        self.assertEqual(format_phone("11994029275"), "(11)99402-9275")

        # When is a landline number
        self.assertEqual(format_phone("1928814933"), "(19)2881-4933")
        self.assertEqual(format_phone("1938814933"), "(19)3881-4933")
        self.assertEqual(format_phone("1948814933"), "(19)4881-4933")
        self.assertEqual(format_phone("1958814933"), "(19)5881-4933")
        self.assertEqual(format_phone("3333333333"), "(33)3333-3333")

    def test_generate(self):
        for _ in range(25):
            with self.subTest():
                no_type_phone_generated = generate()
                self.assertIs(is_valid(no_type_phone_generated), True)
                mobile_phone_generated = generate("mobile")
                self.assertIs(_is_valid_mobile(mobile_phone_generated), True)
                landline_phone_generated = generate("landline")
                self.assertIs(
                    _is_valid_landline(landline_phone_generated), True
                )

    def test_remove_international_dialing_code(self):
        # When the phone number does not have the international code,
        # return the same phone number
        self.assertEqual(
            remove_international_dialing_code("21994029275"), "21994029275"
        )
        self.assertEqual(
            remove_international_dialing_code("55994024478"), "55994024478"
        )
        self.assertEqual(
            remove_international_dialing_code("994024478"), "994024478"
        )

        # When the phone number has the international code,
        # return phone number without international code
        self.assertEqual(
            remove_international_dialing_code("5521994029275"), "21994029275"
        )
        self.assertEqual(
            remove_international_dialing_code("+5521994029275"), "+21994029275"
        )
        self.assertEqual(
            remove_international_dialing_code("+5555994029275"), "+55994029275"
        )
        self.assertEqual(
            remove_international_dialing_code("5511994029275"), "11994029275"
        )

        # When "55" is part of the number, but is not the international
        # code at the beginning, the phone number is returned unchanged
        self.assertEqual(
            remove_international_dialing_code("(55) 95512-3456"),
            "(55) 95512-3456",
        )
        self.assertEqual(
            remove_international_dialing_code("0415599402927"),
            "0415599402927",
        )


if __name__ == "__main__":
    main()

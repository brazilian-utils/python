from datetime import datetime
from unittest import TestCase, main

from brutils.legal_process import (
    _checksum,
    format_legal_process,
    generate,
    is_valid,
    remove_symbols,
)


class TestLegalProcess(TestCase):
    def test_format_legal_process(self):
        self.assertEqual(
            format_legal_process("23141945820055070079"),
            ("2314194-58.2005.5.07.0079"),
        )
        self.assertEqual(
            format_legal_process("00000000000000000000"),
            ("0000000-00.0000.0.00.0000"),
        )
        self.assertIsInstance(
            format_legal_process("00000000000000000000"),
            str,
        )
        self.assertIsNone(format_legal_process("2314194582005507"))
        self.assertIsNone(format_legal_process("0000000000000000000000000"))
        self.assertIsNone(format_legal_process("0000000000000000000asdasd"))

    def test_remove_symbols(self):
        self.assertEqual(
            remove_symbols("6439067-89.2023.4.04.5902"), "64390678920234045902"
        )
        self.assertEqual(
            remove_symbols("4976023-82.2012.7.00.2263"), "49760238220127002263"
        )
        self.assertEqual(
            remove_symbols("4976...-02382-.-2012.-7002--263"),
            "49760238220127002263",
        )
        self.assertEqual(
            remove_symbols("4976023-82.2012.7.00.2263*!*&#"),
            "49760238220127002263*!*&#",
        )
        self.assertEqual(
            remove_symbols("4976..#.-0@2382-.#-2012.#-7002--263@"),
            "4976#0@2382#2012#7002263@",
        )
        self.assertEqual(remove_symbols("@...---...#"), "@#")
        self.assertEqual(remove_symbols("...---..."), "")
        self.assertIsInstance(remove_symbols("...---..."), str)

    def test_generate(self):
        self.assertEqual(generate()[9:13], str(datetime.now().year))
        self.assertEqual(generate(year=3000)[9:13], "3000")
        self.assertEqual(generate(orgao=4)[13:14], "4")
        self.assertEqual(generate(year=3000, orgao=4)[9:13], "3000")
        self.assertIsInstance(generate(year=3000, orgao=4)[9:13], str)
        self.assertIsNone(generate(year=1000, orgao=4))
        self.assertIsNone(generate(orgao=0))

    def test_generate_returns_valid_check_digits(self):
        # CNJ Resolution 65/2008: moving DD to the end, a valid number is
        # congruent to 1 modulo 97 (ISO 7064 MOD 97-10)
        for orgao in range(1, 10):
            legal_process_id = generate(orgao=orgao)
            reordered = legal_process_id[:7] + legal_process_id[9:]
            reordered += legal_process_id[7:9]
            self.assertEqual(int(reordered) % 97, 1)
            self.assertIs(is_valid(legal_process_id), True)

    def test_check_sum(self):
        self.assertEqual(_checksum(546611720238150014), "78")
        self.assertEqual(_checksum(403818720238230498), "51")
        # Real legal process IDs
        self.assertEqual(_checksum(504651220164047000), "94")
        self.assertEqual(_checksum(6975820154013400), "61")
        self.assertIsInstance(_checksum(403818720238230498), str)

    def test_is_valid(self):
        self.assertIs(is_valid("10188748320234018200"), True)
        self.assertIs(is_valid("45532347020234025107"), True)
        # Real legal process IDs
        self.assertIs(is_valid("5046512-94.2016.4.04.7000"), True)
        self.assertIs(is_valid("0069758-61.2015.4.01.3400"), True)
        # Check digits off by one
        self.assertIs(is_valid("5046512-93.2016.4.04.7000"), False)
        self.assertIs(is_valid("10188748220234018200"), False)
        self.assertIs(is_valid("10188748220239918200"), False)
        self.assertIs(is_valid("00000000000000000000"), False)
        self.assertIs(is_valid("455323469202340251"), False)
        self.assertIs(is_valid("455323469202340257123123123"), False)
        self.assertIs(is_valid("455323423QQWEQWSsasd&*(()"), False)
        self.assertIsInstance(is_valid("455323423QQWEQWSsasd&*(()"), bool)


if __name__ == "__main__":
    main()

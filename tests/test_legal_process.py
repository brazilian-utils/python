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

    def test_check_sum(self):
        self.assertEqual(_checksum(546611720238150014), "77")
        self.assertEqual(_checksum(403818720238230498), "50")
        self.assertIsInstance(_checksum(403818720238230498), str)

    def test_is_valid(self):
        self.assertIs(is_valid("10188748220234018200"), True)
        self.assertIs(is_valid("45532346920234025107"), True)
        self.assertIs(is_valid("10188748220239918200"), False)
        self.assertIs(is_valid("00000000000000000000"), False)
        self.assertIs(is_valid("455323469202340251"), False)
        self.assertIs(is_valid("455323469202340257123123123"), False)
        self.assertIs(is_valid("455323423QQWEQWSsasd&*(()"), False)
        self.assertIsInstance(is_valid("455323423QQWEQWSsasd&*(()"), bool)


if __name__ == "__main__":
    main()

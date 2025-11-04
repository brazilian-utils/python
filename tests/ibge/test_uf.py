from unittest import TestCase

from brutils.ibge.uf import (
    convert_code_to_uf,
    convert_name_to_uf,
    convert_uf_to_name,
)


class TestUF(TestCase):
    def test_convert_code_to_uf_valid(self):
        test_cases = [
            ("12", "AC"),
            ("27", "AL"),
            ("16", "AP"),
            ("13", "AM"),
            ("29", "BA"),
            ("23", "CE"),
            ("53", "DF"),
            ("32", "ES"),
            ("52", "GO"),
            ("21", "MA"),
            ("51", "MT"),
            ("50", "MS"),
            ("31", "MG"),
            ("15", "PA"),
            ("25", "PB"),
            ("41", "PR"),
            ("26", "PE"),
            ("22", "PI"),
            ("33", "RJ"),
            ("24", "RN"),
            ("43", "RS"),
            ("11", "RO"),
            ("14", "RR"),
            ("42", "SC"),
            ("35", "SP"),
            ("28", "SE"),
            ("17", "TO"),
        ]
        for code, expected_uf in test_cases:
            with self.subTest(code=code):
                self.assertEqual(convert_code_to_uf(code), expected_uf)

    def test_convert_code_to_uf_invalid(self):
        invalid_codes = ["99", "00", "", "AB", "1", "123"]
        for invalid_code in invalid_codes:
            with self.subTest(code=invalid_code):
                self.assertIsNone(convert_code_to_uf(invalid_code))

    def test_convert_uf_to_name_valid(self):
        test_cases = [
            ("SP", "São Paulo"),
            ("RJ", "Rio de Janeiro"),
            ("MG", "Minas Gerais"),
            ("DF", "Distrito Federal"),
            ("BA", "Bahia"),
            ("RS", "Rio Grande do Sul"),
        ]
        for uf, expected_name in test_cases:
            with self.subTest(uf=uf):
                self.assertEqual(convert_uf_to_name(uf), expected_name)

    def test_convert_uf_to_name_case_insensitive(self):
        test_cases = [
            ("sp", "São Paulo"),
            ("df", "Distrito Federal"),
            ("Rj", "Rio de Janeiro"),
        ]
        for uf, expected_name in test_cases:
            with self.subTest(uf=uf):
                self.assertEqual(convert_uf_to_name(uf), expected_name)

    def test_convert_uf_to_name_invalid(self):
        invalid_ufs = ["XX", "XXX", "", "A", "123", "  "]
        for invalid_uf in invalid_ufs:
            with self.subTest(uf=invalid_uf):
                self.assertIsNone(convert_uf_to_name(invalid_uf))

    def test_convert_name_to_uf_all_states(self):
        test_cases = [
            ("Acre", "AC"),
            ("Alagoas", "AL"),
            ("Amapá", "AP"),
            ("Amazonas", "AM"),
            ("Bahia", "BA"),
            ("Ceará", "CE"),
            ("Distrito Federal", "DF"),
            ("Espírito Santo", "ES"),
            ("Goiás", "GO"),
            ("Maranhão", "MA"),
            ("Mato Grosso", "MT"),
            ("Mato Grosso do Sul", "MS"),
            ("Minas Gerais", "MG"),
            ("Pará", "PA"),
            ("Paraíba", "PB"),
            ("Paraná", "PR"),
            ("Pernambuco", "PE"),
            ("Piauí", "PI"),
            ("Rio de Janeiro", "RJ"),
            ("Rio Grande do Norte", "RN"),
            ("Rio Grande do Sul", "RS"),
            ("Rondônia", "RO"),
            ("Roraima", "RR"),
            ("Santa Catarina", "SC"),
            ("São Paulo", "SP"),
            ("Sergipe", "SE"),
            ("Tocantins", "TO"),
        ]
        for state_name, expected_uf in test_cases:
            with self.subTest(state_name=state_name):
                self.assertEqual(convert_name_to_uf(state_name), expected_uf)

    def test_convert_name_to_uf_normalization(self):
        test_cases = [
            ("sao paulo", "SP"),
            ("SAO PAULO", "SP"),
            ("SãO pAuLo", "SP"),
            ("  Rio de Janeiro  ", "RJ"),
            ("ceara", "CE"),
            ("PARANÁ", "PR"),
            ("parana", "PR"),
        ]
        for state_name, expected_uf in test_cases:
            with self.subTest(state_name=state_name):
                self.assertEqual(convert_name_to_uf(state_name), expected_uf)

    def test_convert_name_to_uf_wrong_spacing(self):
        test_cases = [
            ("Sao  Paulo", "SP"),
            ("Rio  de  Janeiro", "RJ"),
            ("Mato   Grosso", "MT"),
            ("Rio   Grande   do   Sul", "RS"),
            ("Mato  Grosso  do  Sul", "MS"),
            ("Espírito  Santo", "ES"),
            ("Rio Grande  do Norte", "RN"),
        ]
        for state_name, expected_uf in test_cases:
            with self.subTest(state_name=state_name):
                self.assertEqual(convert_name_to_uf(state_name), expected_uf)

    def test_convert_name_to_uf_invalid_input(self):
        invalid_inputs = [
            None,
            "",
            "   ",
            "Estado Inválido",
            "São Pauloo",
            "Rio",
            "Brasil",
            "XYZ",
            123,
            [],
            {},
        ]
        for invalid_input in invalid_inputs:
            with self.subTest(input=repr(invalid_input)):
                self.assertIsNone(convert_name_to_uf(invalid_input))

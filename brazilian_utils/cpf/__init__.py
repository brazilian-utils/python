# This module provides a single method, is_valid_cpf(),
# which returns True or False to indicate whether a given cpf
# is valid according with Ministério da Fazenda specification.

from constant import BLACKLIST


def is_valid(cpf):
    if not isinstance(cpf, str):
        return False

    if cpf in BLACKLIST or not cpf.isdigit():
        return False

    if len(cpf) != 11:
        return False

    first_digit = validate_first_digit(cpf)
    second_digit = validate_second_digit(cpf)

    verificators = cpf[-2:]

    return first_digit == int(verificators[0]) and second_digit == int(verificators[1])


def validate_first_digit(cpf):
    """Calculate first verificator digit"""
    weigth = list(range(10, 1, -1))
    result = 11 - (sum(int(cpf[:9][g]) * weigth[g] for g in range(9)) % 11)
    return result if result <= 9 else 0


def validate_second_digit(cpf):
    """Calculate second verificator digit"""
    weigth = list(range(11, 1, -1))
    result = 11 - (sum(int(cpf[:10][g]) * weigth[g] for g in range(10)) % 11)
    return result if result <= 9 else 0

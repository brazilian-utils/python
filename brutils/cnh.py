def is_valid_cnh(cnh: str) -> bool:
    """
    Validates the registration number for the Brazilian CNH (Carteira Nacional de Habilitação) that was created in 2022.
    Previous versions of the CNH are not supported in this version.
    This function checks if the given CNH is valid based on the format and allowed characters,
    verifying the verification digits.

    Args:
        cnh (str): CNH string (symbols will be ignored).

    Returns:
        bool: True if CNH has a valid format.

    Examples:
        >>> is_valid_cnh("12345678901")
        False
        >>> is_valid_cnh("A2C45678901")
        False
        >>> is_valid_cnh("98765432100")
        True
        >>> is_valid_cnh("987654321-00")
        True
    """
    cnh = "".join(
        filter(str.isdigit, cnh)
    )  # clean the input and check for numbers only

    if not cnh:
        return False

    if len(cnh) != 11:
        return False

    # Reject sequences as "00000000000", "11111111111", etc.
    if cnh == cnh[0] * 11:
        return False

    # cast digits to list of integers
    digits: list[int] = [int(ch) for ch in cnh]
    first_verificator = digits[9]
    second_verificator = digits[10]

    if not _check_first_verificator(
        digits, first_verificator
    ):  # checking the 10th digit
        return False

    return _check_second_verificator(
        digits, second_verificator, first_verificator
    )  # checking the 11th digit


def _check_first_verificator(digits: list[int], first_verificator: int) -> bool:
    """
    Generates the first verification digit and uses it  to verify the 10th digit of the CNH
    """

    sum = 0
    for i in range(9):
        sum += digits[i] * (9 - i)

    sum = sum % 11
    result = 0 if sum > 9 else sum

    return result == first_verificator


def _check_second_verificator(
    digits: list[int], second_verificator: int, first_verificator: int
) -> bool:
    """
    Generates the second verification  and uses it to verify the 11th digit of the CNH
    """
    sum = 0
    for i in range(9):
        sum += digits[i] * (i + 1)

    result = sum % 11

    if first_verificator > 9:
        result = result + 9 if (result - 2) < 0 else result - 2

    if result > 9:
        result = 0

    return result == second_verificator

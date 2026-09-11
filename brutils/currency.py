from decimal import ROUND_DOWN, Decimal, InvalidOperation

from num2words import num2words


def format_currency(value: float | int | str | Decimal) -> str | None:
    """
    Format a numeric value as Brazilian currency (R$).

    Args:
        value: The numeric value to format. Accepts float, int, str, or Decimal.

    Returns:
        Formatted currency string (e.g., "R$ 1.234,56") or None if invalid.

    Example:
        >>> format_currency(1234.56)
        'R$ 1.234,56'
        >>> format_currency(0)
        'R$ 0,00'
        >>> format_currency(-9876.54)
        'R$ -9.876,54'
        >>> format_currency("invalid")
    """
    try:
        decimal_value = Decimal(value)
        formatted_value = (
            f"R$ {decimal_value:,.2f}".replace(",", "_")
            .replace(".", ",")
            .replace("_", ".")
        )
        return formatted_value
    except (InvalidOperation, TypeError, ValueError):
        return None


def convert_real_to_text(amount: Decimal | float | int | str) -> str | None:
    """
    Convert a monetary value in Brazilian Reais to textual representation.

    Args:
        amount: Monetary value to convert. Accepts Decimal, float, int, or str.

    Returns:
        Textual representation in Brazilian Portuguese, or None if invalid.

    Note:
        - Values are rounded down to 2 decimal places
        - Maximum supported value is 1 quadrillion reais
        - Negative values are prefixed with "Menos"

    Example:
        >>> convert_real_to_text(1523.45)
        'Mil, quinhentos e vinte e três reais e quarenta e cinco centavos'
        >>> convert_real_to_text(1.00)
        'Um real'
        >>> convert_real_to_text(0.50)
        'Cinquenta centavos'
        >>> convert_real_to_text(0.00)
        'Zero reais'
    """
    try:
        amount = Decimal(str(amount)).quantize(
            Decimal("0.01"), rounding=ROUND_DOWN
        )
    except (InvalidOperation, TypeError, ValueError):
        return None

    if amount.is_nan() or amount.is_infinite():
        return None

    if abs(amount) > Decimal("1000000000000000.00"):  # 1 quadrillion
        return None

    negative = amount < 0
    amount = abs(amount)

    reais = int(amount)
    centavos = int((amount - reais) * 100)

    parts = []

    if reais > 0:
        """
        Note:
        Although the `num2words` library provides a "to='currency'" feature, it has known
        issues with the representation of "zero reais" and "zero centavos". Therefore, this
        implementation uses only the traditional number-to-text conversion for better accuracy.
        """
        reais_text = num2words(reais, lang="pt_BR")
        currency_text = "real" if reais == 1 else "reais"
        conector = "de " if reais_text.endswith(("lhão", "lhões")) else ""
        parts.append(f"{reais_text} {conector}{currency_text}")

    if centavos > 0:
        centavos_text = f"{num2words(centavos, lang='pt_BR')} {'centavo' if centavos == 1 else 'centavos'}"
        if reais > 0:
            parts.append(f"e {centavos_text}")
        else:
            parts.append(centavos_text)

    if reais == 0 and centavos == 0:
        parts.append("Zero reais")

    result = " ".join(parts)
    if negative:
        result = f"Menos {result}"

    return result.capitalize()

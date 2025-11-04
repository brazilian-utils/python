![Brazilian Utils Logo](https://github.com/brazilian-utils/brand/raw/main/github-hero/github-hero-python.png)

<div align="center">
<p>Utils library for Brazilian-specific businesses.</p>

[![codecov](https://codecov.io/gh/brazilian-utils/brutils-python/branch/main/graph/badge.svg?token=5KNECS8JYF)](https://codecov.io/gh/brazilian-utils/brutils-python)
[![Downloads per Month](https://shields.io/pypi/dm/brutils)](https://pypistats.org/packages/brutils)
[![Package version](https://shields.io/pypi/v/brutils)](https://pypi.org/project/brutils/)

### [Procurando pela versão em português?](README.md)

</div>

# Getting Started

Brazilian Utils is a library focused on solving problems that we face daily in
the development of applications for the Brazilian business.

- [Installation](#installation)
- [Usage](#usage)
- [Utilities](#utilities)
- [Feature Request and Bug Report](#feature-request-and-bug-report)
- [Questions? Ideas?](#questions-ideas)
- [Code Contribution](#code-contribution)

# Installation

```bash
pip install brutils
```

# Usage

To use one of our utilities you just need to import the required function as in the example below:

```python
>>> from brutils import is_valid_cpf
>>> is_valid_cpf('00011122233')
False
```

# Utilities

- [CPF](#cpf)
  - [is\_valid\_cpf](#is_valid_cpf)
  - [format\_cpf](#format_cpf)
  - [remove\_symbols\_cpf](#remove_symbols_cpf)
  - [generate\_cpf](#generate_cpf)
- [CNPJ](#cnpj)
  - [is\_valid\_cnpj](#is_valid_cnpj)
  - [format\_cnpj](#format_cnpj)
  - [remove\_symbols\_cnpj](#remove_symbols_cnpj)
  - [generate\_cnpj](#generate_cnpj)
- [CEP](#cep)
  - [is\_valid\_cep](#is_valid_cep)
  - [format\_cep](#format_cep)
  - [remove\_symbols\_cep](#remove_symbols_cep)
  - [generate\_cep](#generate_cep)
  - [get\_address\_from\_cep](#get_address_from_cep)
  - [get\_cep\_information\_from\_address](#get_cep_information_from_address)
- [Date](#date)
  - [convert\_date\_to_text](#convert_date_to_text)
- [Phone](#phone)
  - [is\_valid\_phone](#is_valid_phone)
  - [format\_phone](#format_phone)
  - [remove\_symbols\_phone](#remove_symbols_phone)
  - [remove\_international\_dialing\_code](#remove_international_dialing_code)
  - [generate\_phone](#generate_phone)
- [Email](#email)
  - [is\_valid\_email](#is_valid_email)
- [CNH](#cnh)
  - [is\_valid\_cnh](#is_valid_cnh)
- [License Plate](#license-plate)
  - [is\_valid\_license\_plate](#is_valid_license_plate)
  - [format\_license\_plate](#format_license_plate)
  - [remove\_symbols\_license\_plate](#remove_symbols_license_plate)
  - [generate\_license\_plate](#generate_license_plate)
  - [convert\_license\_plate\_to\_mercosul](#convert_license_plate_to_mercosul)
  - [get\_format\_license\_plate](#get_format_license_plate)
- [PIS](#pis)
  - [is\_valid\_pis](#is_valid_pis)
  - [format\_pis](#format_pis)
  - [remove\_symbols\_pis](#remove_symbols_pis)
  - [generate\_pis](#generate_pis)
- [Legal Process](#legal-process)
  - [is\_valid\_legal\_process](#is_valid_legal_process)
  - [format\_legal\_process](#format_legal_process)
  - [remove\_symbols\_legal\_process](#remove_symbols_legal_process)
  - [generate\_legal\_process](#generate_legal_process)
- [Voter ID](#voter-id)
  - [is_valid_voter_id](#is_valid_voter_id)
  - [format_voter_id](#format_voter_id)
  - [generate_voter_id](#generate_voter_id)
- [IBGE](#ibge)
  - [convert_code_to_uf](#convert_code_to_uf)
  - [convert_uf_to_name](#convert_uf_to_name)
  - [convert_name_to_uf](#convert_name_to_uf)
  - [get_code_by_municipality_name](#get_code_by_municipality_name)
  - [get\_municipality\_by\_code](#get_municipality_by_code)
- [Holidays](#holidays)
  - [is_holiday](#is_holiday)
- [Monetary](#monetary)
  - [format_currency](#format_currency)
  - [convert\_real\_to\_text](#convert_real_to_text)

## CPF

### is_valid_cpf

Returns whether or not the verifying checksum digits of the given CPF
(Brazilian Individual Taxpayer Number) match its base number.
This function does not verify the existence of the CPF; it only
validates the format of the string.

Args:

- cpf (str): The CPF to be validated, a 11-digit string

Returns:

- bool: True if the checksum digits match the base number,
          False otherwise.

Example:

```python
>>> from brutils import is_valid_cpf
>>> is_valid_cpf("82178537464")
True
>>> is_valid_cpf('00011122233')
False
```

### format_cpf

Format a CPF (Brazilian Individual Taxpayer Number) for display with visual
aid symbols. This function takes a numbers-only CPF string as input and adds
standard formatting visual aid symbols for display.

Args:

- cpf (str): A numbers-only CPF string.

Returns:

- str: A formatted CPF string with standard visual aid symbols or
         None if the input is invalid.

Example:

```python
>>> from brutils import format_cpf
>>> format_cpf('82178537464')
'821.785.374-64'
>>> format_cpf("55550207753")
'555.502.077-53'
```

### remove_symbols_cpf

Removes specific symbols from a CPF (Brazilian Individual Taxpayer Number)
string. This function takes a CPF string as input and removes all occurrences of
the '.', '-' characters from it.

Args:

- cpf (str): The CPF string containing symbols to be removed.

Returns:

- str: A new string with the specified symbols removed.

Example:

```python
>>> from brutils import remove_symbols_cpf
>>> remove_symbols_cpf('000.111.222-33')
'00011122233'
```

### generate_cpf

Generate a random valid CPF (Brazilian Individual Taxpayer Number) digit string.

Returns:

- str: A random valid CPF string.

Example:

```python
>>> from brutils import generate_cpf
>>> generate_cpf()
'17433964657'
>>> generate_cpf()
"10895948109"
```

## CNPJ

### is_valid_cnpj

Returns whether or not the verifying checksum digits of the given CNPJ
(Brazilian Company Registration Number) match its base number.
Input should be a digit string of proper length.
This function does not verify the existence of the CNPJ; it only
validates the format of the string.

Args:

- cnpj (str): The CNPJ to be validated.

Returns:

- bool: True if the checksum digits match the base number,
          False otherwise.

Example:

```python
>>> from brutils import is_valid_cnpj
>>> is_valid_cnpj('03560714000142')
True
>>> is_valid_cnpj('00111222000133')
False
```

### format_cnpj

Formats a CNPJ (Brazilian Company Registration Number) string for visual
display.
This function takes a CNPJ string as input, validates its format, and
formats it with standard visual aid symbols for display purposes.

Args:

- cnpj (str): The CNPJ string to be formatted for display.

Returns:

- str: The formatted CNPJ with visual aid symbols if it's valid,
         None if it's not valid.

Example:

```python
>>> from brutils import format_cnpj
>>> format_cnpj("03560714000142")
'03.560.714/0001-42'
>>> format_cnpj("98765432100100")
None
```

### remove_symbols_cnpj

Removes specific symbols from a CNPJ (Brazilian Company Registration Number)
string.
This function takes a CNPJ string as input and removes all occurrences of
the '.', '/' and '-' characters from it.

Args:

- cnpj (str): The CNPJ string containing symbols to be removed.

Returns:

- str: A new string with the specified symbols removed.

Example:

```python
>>> from brutils import remove_symbols_cnpj
>>> remove_symbols_cnpj('00.111.222/0001-00')
'00111222000100'
```

### generate_cnpj

Generates a random valid CNPJ (Brazilian Company Registration Number) digit
string. An optional branch number parameter can be given; it defaults to 1.

Args:

- branch (int): An optional branch number to be included in the CNPJ.

Returns:

- str: A randomly generated valid CNPJ string.

Example:

```python
>>> from brutils import generate_cnpj
>>> generate_cnpj()
'34665388000161'
>>> generate_cnpj(1234)
"01745284123455"
```

## CEP

### is_valid_cep

Checks if a Brazilian CEP (Postal Code) is valid.
To be considered valid, the input must be a string containing exactly 8 digits.
This function does not verify if the CEP is a real postal code; it only
validates the format of the string.

Args:

- cep (str): The string containing the CEP to be checked.

Returns:

- bool: True if the CEP is valid (8 digits), False otherwise.

Example:

```python
>>> from brutils import is_valid_cep
>>> is_valid_cep('01310200')
True
>>> is_valid_cep("12345")
False
>>> is_valid_cep("abcdefgh")
False
```

### format_cep

This function takes a CEP (Postal Code) as input and, if it is a valid
8-digit CEP, formats it into the standard "12345-678" format.

Args:

- cep (str): The input CEP (Postal Code) to be formatted.

Returns:

- str: The formatted CEP in the "12345-678" format if it's valid,
         None if it's not valid.

Example:

```python
>>> from brutils import format_cep
>>> format_cep('01310200')
'01310-200'
>>> format_cep("12345678")
"12345-678"
>>> format_cep("12345")
None
```

### remove_symbols_cep

This function takes a CEP (Postal Code) as input and removes all occurrences of
the '.' and '-' characters from it.

Args:

- cep (str): The input CEP (Postal Code) containing symbols to be removed.

Returns:

- str: A new string with the specified symbols removed.

Example:

```python
>>> from brutils import remove_symbols_cep
>>> remove_symbols_cep('01310-200')
'01310200'
>>> remove_symbols_cep("123-45.678.9")
"123456789"
>>> remove_symbols_cep("abc.xyz")
"abcxyz"
```

### generate_cep

Generates a random 8-digit CEP (Postal Code) number as a string.

Returns:

- str: A randomly generated 8-digit number.

Example:

```python
>>> from brutils import generate_cep
>>> generate_cep()
'77520503'
```

### get_address_from_cep

Fetches address information from a given CEP (Postal Code) using the ViaCEP API.

Args:

- cep (str): The CEP (Postal Code) to be used in the search.
- raise_exceptions (bool, optional): Whether to raise exceptions when the CEP is invalid or not found. Defaults to False.

Returns:

- Address | None: An Address object (TypedDict) containing the address information if the CEP is found, None otherwise.

Example:

```python
>>> from brutils import get_address_from_cep
>>> get_address_from_cep("12345678")
{
    "cep": "12345-678",
    "logradouro": "Rua Example",
    "complemento": "",
    "bairro": "Example",
    "localidade": "Example",
    "uf": "EX",
    "ibge": "1234567",
    "gia": "1234",
    "ddd": "12",
    "siafi": "1234"
}
```

### get_cep_information_from_address

Fetches CEP (Postal Code) options from a given address using the ViaCEP API.

Args:

- federal_unit (str): The two-letter abbreviation of the Brazilian state.
- city (str): The name of the city.
- street (str): The name (or substring) of the street.
- raise_exceptions (bool, optional): Whether to raise exceptions when the address is invalid or not found. Defaults to False.

Returns:

- list[Address] | None: A list of Address objects (TypedDict) containing the address information if the address is found, None otherwise.

Example:

```python
>>> from brutils import get_cep_information_from_address
>>> get_cep_information_from_address("EX", "Example", "Rua Example")
[
    {
        "cep": "12345-678",
        "logradouro": "Rua Example",
        "complemento": "",
        "bairro": "Example",
        "localidade": "Example",
        "uf": "EX",
        "ibge": "1234567",
        "gia": "1234",
        "ddd": "12",
        "siafi": "1234"
    }
]
```

## Date

### convert_date_to_text
Convert a brazilian date (dd/mm/yyyy) format in their portuguese textual representation.

Args:
 - date (str): A date in a string format dd/mm/yyyy.

Return:
 - (str) | None: A portuguese textual representation of the date or None case a date is invalid.


Example:

````python
>>> from brutils import convert_date_to_text
>>> convert_date_to_text("25/12/2000")
"Vinte e cinco de dezembro de dois mil"
>>> convert_date_to_text("31/02/2000")
None
>>> convert_date_to_text("29/02/2024")
"Vinte e nove de fevereiro de dois mil e vinte e quatro"
>>> convert_date_to_text("1/08/2024")
"Primeiro de agosto de dois mil e vinte e quatro"
````

## Phone

### is_valid_phone

Return whether a Brazilian phone number is valid.
It does not verify if the number actually exists.

```
is_valid_phone(phone_number, type)
```

Args:

- phone_number:
  - the phone number to be validated
  - digits only, no symbols
  - without the country code
  - should include the area code (DDD) with two digits
  - example: '+55 48 9999 9999' should be used as '4899999999'
  - mandatory

- type:
  - 'mobile' to validate only mobile numbers
  - 'landline' to validate only landline phone numbers
  - if not specified, it validates for either.
  - optional

Returns:

- bool: True if the phone number is valid. False otherwise.

Example:

```python
>>> from brutils import is_valid_phone
>>> is_valid_phone('11994029275')
True
>>> is_valid_mobile_phone('11994029275', 'mobile')
True
>>> is_valid_landline_phone('1938814933', 'landline')
True
```

### format_phone

Format a phone number for visual display. This function takes a string representing a phone number containing only numbers as input and adds standard formatting symbols for display.

Args:

- phone (str): A string representing a phone number.

Returns:

- str: The formatted phone number for display or None if it is not valid.

Example:

```python
>>> from brutils import format_phone
>>> format_phone("11994029275")
'(11)99402-9275'
>>> format_phone("1635014415")
'(16)3501-4415'
>>> format_phone("333333")
None
```

### remove_symbols_phone

Remove symbols from the phone number. This function takes a phone number as input and removes all symbols, such as parentheses '()', dashes '-', and spaces ' '.

Args:

- phone (str): The input phone number containing the symbols to be removed.

Returns:

- str: A new string with the specified symbols removed.

Example:

```python
>>> from brutils import remove_symbols_phone
>>> remove_symbols_phone('(21)2569-6969')
'2125696969'
>>> remove_symbols_phone('11 9999-8888')
'1199998888'
>>> remove_symbols_phone('333333')
'333333'
```

### remove_international_dialing_code

Remove the international code (+55) from a string containing a Brazilian phone number, preserving other special characters.

Args:

- phone (str): The input phone number that may contain the international code.

Returns:

- str: A new string without the international code, preserving other special characters.

Example:

```python
>>> from brutils import remove_international_dialing_code
>>> remove_international_dialing_code("5521994029275")
"21994029275"
>>> remove_international_dialing_code("+5521994029275")
"+21994029275"
>>> remove_international_dialing_code("5555994029275")
"55994029275"
>>> remove_international_dialing_code("21994029275")
"21994029275"
>>> remove_international_dialing_code("(+55)21994029275")
"(+)21994029275"
```

### generate_phone

Generates a valid random phone number.

Args:

- type (str): It can be "landline" or "mobile".
                If not specified, the function generates
                a random number of any type.

Returns:

- str: A randomly generated valid phone number.

Example:

```python
>>> from brutils import generate_phone
>>> generate_phone()
"5929797740"
>>> generate_phone("mobile")
"1899115895"
>>> generate_phone("landline")
"5535317900"
```

## Email

### is_valid_email

Check if a string corresponds to a valid email address.

Args:

- email (str): The input string to be checked.

Returns:

- bool: True if email is a valid email address, False otherwise.

Example:

```python
from brutils import is_valid_email

>>> is_valid_email("joao.ninguem@gmail.com")
True
>>> is_valid_email(".joao.ninguem@gmail.com")
False
>>> is_valid_email("joao.ninguem@gmail.")
False
>>> is_valid_email("joao ninguem@gmail.com")
False
```


## CNH

### is_valid_cnh

Checks if the registration number of a brazilian CNH (Carteira de Habilitação Nacional or Driver's License in En.) is valid.
To be considered valid, the input must be a string containing exactly 11 digits. This function does not verify if the registration number of the CNH is a real one, it only validates it's verification numbers.

Argumentos:

- cnh (str): A string containing the registration nunber of the CNH to be checked.

Retorno:

- bool: True if the CNH number is valid (11 digits), False otherwise.

Exemplo:

```python
>>> from brutils import is_valid_cnh
>>> is_valid_cnh("123456789")
False
>>> is_valid_cnh("A2C45678901")
False
>>> is_valid_cnh("98765432100")
True
>>> is_valid_cnh("987654321-00")
True
```


## License Plate

### is_valid_license_plate

Check if a license plate is valid.
This function does not verify if the license plate is a real license plate;
it only validates the format of the string.

Args:

- license_plate (str): A license plate string.
- type (str): "old_format" or "mercosul".
                If not specified, checks for one or another.

Returns:

- bool: True if the license plate is valid, False otherwise.

Example:

```python
>>> from brutils import is_valid_license_plate
>>> is_valid_license_plate('ABC1234')
True
>>> is_valid_license_plate('def5678', type="old_format")
True
>>> is_valid_license_plate('ABC4E67')
True
>>> is_valid_license_plate('ABC4E67', type="mercosul")
True
>>> is_valid_license_plate('GHI-4567')
False
```

### format_license_plate

Formats a license plate into the correct pattern.
This function receives a license plate in any pattern (LLLNNNN or LLLNLNN)
and returns a formatted version.

Args:

- license_plate (str): A license plate string.

Returns:

- str: The formatted license plate string or
         'None' if the input is invalid.

Example:

```python
>>> from brutils import format_license_plate
>>> format_license_plate("ABC1234")
"ABC-1234"
# old format (contains a dash)
>>> format_license_plate("abc1234")
"ABC-1234"
# old format (contains a dash)
>>> format_license_plate("ABC1D23")
"ABC1D23"
# mercosul format
>>> format_license_plate("abc1d23")
"ABC1D23"
# mercosul format
>>> format_license_plate("ABCD123")
None
```

### remove_symbols_license_plate

Removes the dash (-) symbol from a license plate string.

Args:

- license_plate_number (str): A license plate number containing symbols to
                                be removed.

Returns:

- str: The license plate number with the specified symbols removed.

Example:

```python
from brutils import remove_symbols_license_plate
>>> remove_symbols_license_plate("ABC-123")
"ABC123"
>>> remove_symbols_license_plate("abc123")
"abc123"
>>> remove_symbols_license_plate("ABCD123")
"ABCD123"
>>> remove_symbols_license_plate("@abc#-#123@")
"@abc##123@"
```

### generate_license_plate

Generate a valid license plate in the given format. In case no format is
provided, it will return a license plate in the Mercosul format.

Args:

- format (str): The desired format for the license plate.
                  'LLLNNNN' for the old pattern or 'LLLNLNN' for the
                   Mercosul one. Default is 'LLLNLNN'

Returns:

- str: A randomly generated license plate number or
         'None' if the format is invalid.

Example:

```python
from brutils import generate_license_plate
>>> generate_license_plate()
"ABC1D23"
>>> generate_license_plate(format="LLLNLNN")
"ABC4D56"
>>> generate_license_plate(format="LLLNNNN")
"ABC123"
>>> generate_license_plate(format="invalid")
None
```

### convert_license_plate_to_mercosul

Converts an old pattern license plate (LLLNNNN) to a Mercosul format
(LLLNLNN).

Args:

- license_plate (str): A string of proper length representing the
                         old pattern license plate.

Returns:

- str: The converted Mercosul license plate (LLLNLNN) or
         'None' if the input is invalid.

Example:

```python
>>> from brutils import convert_license_plate_to_mercosul
>>> convert_license_plate_to_mercosul("ABC123")
"ABC1C34"
>>> convert_license_plate_to_mercosul("abc123")
"ABC1C34"
>>> convert_license_plate_to_mercosul("ABC1D23")
None
```

### get_format_license_plate

Return the format of a license plate. 'LLLNNNN' for the old pattern and
'LLLNLNN' for the Mercosul one.

Args:

- license_plate (str): A license plate string without symbols.

Returns:

- str: The format of the license plate (LLLNNNN, LLLNLNN) or
          'None' if the format is invalid.

Example:

```python
from brutils import get_format_license_plate
>>> get_format_license_plate("ABC123")
"LLLNNNN"
>>> get_format_license_plate("abc123")
"LLLNNNN"
>>> get_format_license_plate("ABC1D23")
"LLLNLNN"
>>> get_format_license_plate("abc1d23")
"LLLNLNN"
>>> get_format_license_plate("ABCD123")
None
```

## PIS

### is_valid_pis

Verifies if the PIS/PASEP number is valid. Only numbers, formatted as a string. It does not check if the PIS/PASEP actually exists.

References:

- <https://www.macoratti.net/alg_pis.htm>.

Args:

- pis (str): PIS number as a string with the proper length.

Returns:

- bool: True if the PIS is valid, False otherwise.

Example:

```python
from brutils import is_valid_pis
>>> is_valid_pis("82178537464")
False
>>> is_valid_pis("12082043519")
True
```

### format_pis

Formats a valid PIS (Programa de Integração Social) string with symbols and adds standard formatting symbols for display.

Args:

- pis (str): A valid string of PIS containing only numbers.

Returns:

- str: A formatted PIS string with standard visual aid symbols or None if the input is invalid.

Example:

```python
from brutils import format_pis
>>> format_pis("17033259504")
'170.33259.50-4'
>>> format_pis("12013128292")
'120.13128.29-2'
```

### remove_symbols_pis

This function takes a string of PIS (Programa de Integração Social) with formatting symbols and returns a clean version without certain symbols. It intentionally removes only the symbols "-" and ".", leaving other symbols untouched.

Args:

- pis (str): A string of PIS that may contain formatting symbols.

Returns:

- str: A clean string of PIS without formatting symbols.

Example:

```python
from brutils import remove_symbols_pis
>>> remove_symbols_pis('170.33259.50-4')
'17033259504'
>>> remove_symbols_pis("123.456.789-09")
'12345678909'
>>> remove_symbols_pis('/._')
'/_'
```

### generate_pis

Generates a string of digits containing a random valid Brazilian PIS number.

Returns:

- str: A randomly generated valid PIS number as a string.

Example:

```python
from brutils import generate_pis
>>> generate_pis()
'61352489741'
>>> generate_pis()
'73453349671'
```

## Legal Process

## is_valid_legal_process

Check if a legal process ID is valid.

This function does not verify if the legal process ID is a real legal
process ID; it only validates the format of the string.

Args:

- legal_process_id (str): A digit-only string representing the legal
                            process ID.

Returns:

- bool: True if the legal process ID is valid, False otherwise.

Example:

```python
>>> from brutils import is_valid_legal_process
>>> is_valid_legal_process('10188748220234018200')
True
>>> is_valid_legal_process('45532346920234025107')
True
>>> is_valid_legal_process('00000000000000000000')
False
>>> is_valid_legal_process('455323423QQWEQWSsasd&*(()')
False
>>>
```

### format_legal_process

Format a legal process ID into a standard format.

Args:

- legal_process_id (str): A 20-digits string representing the legal
                            process ID.

Returns:

- str: The formatted legal process ID or None if the input is invalid.

Example:

```python
>>> from brutils import format_legal_process
>>> format_legal_process('23141945820055070079')
'2314194-58.2005.5.07.0079'
>>> format_legal_process('00000000000000000000')
'0000000-00.0000.0.00.0000'
>>> format_legal_process("123")
None
```

### remove_symbols_legal_process

Removes specific symbols from a given legal process.

This function takes a legal process as input and removes all occurrences
of the '.' and '-' characters from it.

Args:

- legal_process (str): A legal process containing symbols to be removed.

Returns:

- str: The legal process string with the specified symbols removed.

Example:

```python
from brutils import remove_symbols_legal_process
>>> remove_symbols_legal_process("6439067-89.2023.4.04.5902")
"64390678920234045902"
>>> remove_symbols_legal_process("4976023-82.2012.7.00.2263")
"49760238220127002263"
>>> remove_symbols_legal_process("4976023-82.2012.7.00.2263*!*&#")
"49760238220127002263*!*&#"
```

### generate_legal_process

Generate a random legal process ID number.

Args:

- year (int): The year for the legal process ID (default is the current
                year).
                The year should not be in the past
- orgao (int): The organization code (1-9) for the legal process ID
                 (default is random).

Returns:

- str: A randomly generated legal process ID.
         None if one of the arguments is invalid.

Example:

```python
>>> from brutils import generate_legal_process
>>> generate_legal_process()
"45676401020238170592"
>>> generate_legal_process(year=2025)
"32110268020258121130"
>>> generate_legal_process(orgao=5)
"37573041520235090313"
>>> generate_legal_process(year=2024, orgao=4)
"33158248820244017105"
```

## Voter ID

### is_valid_voter_id

Check if a Brazilian voter id number is valid.
It does not verify if the voter id actually exists.

References:

- <https://pt.wikipedia.org/wiki/T%C3%ADtulo_de_eleitor>,
- <http://clubes.obmep.org.br/blog/a-matematica-nos-documentos-titulo-de-eleitor/>

Args:

- voter_id(str): string representing the voter id to be verified.

Returns:

- bool: True if the voter id is valid. False otherwise.

Example:

```python
>>> from brutils import is_valid_voter_id
>>> is_valid_voter_id('123456789011')
False
>>> is_valid_voter_id('427503840213')
True
```

### format_voter_id

Formats a voter ID number for visual display.

This function takes a voter ID string containing only numbers as input
and adds the standard formatting spaces for display.

Arguments:
  * voter_id (str): A voter ID string containing only numbers.

Returns:
  * str: The formatted voter ID with spaces if valid.
         Returns None if not valid.

Example:

```python
>>> from brutils import format_voter_id
>>> format_voter_id("246593980493")
'2465 9398 04 93'
>>> format_voter_id("202715292895")
'2027 1529 28 95'
>>> format_voter_id("739035552205")
>>>
```

### generate_voter_id

Generate a valid random Voter ID string of digits from an informed Brazilian federation union.

Args:
  * federative_union(str): federative union for the voter id that will be generated. The default value "ZZ" is used for voter IDs issued to foreigners.

Returns:
  * str: A randomly generated valid voter ID.

Example:

```python
>>> from brutils import generate_voter_id
>>> generate_voter_id()
'183475722801'
>>> generate_voter_id(federative_union ="MG")
'950125640248'
```
## IBGE

### convert_code_to_uf
Converts a given IBGE code (2-digit string) to its corresponding UF (state abbreviation).

Args:
  * code (str): The 2-digit IBGE code to be converted.

Retorna:
  * str or None: The UF code corresponding to the IBGE code, or None if the
                 IBGE code is invalid.

Exemplo:

```python
>>> from brutils.ibge.uf import convert_code_to_uf
>>> convert_code_to_uf("12")
'AC'
>>> convert_code_to_uf("33")
'RJ'
>>> convert_code_to_uf("99")
>>>
```

### get_code_by_municipality_name

Returns the IBGE code for a given municipality name and uf code.

This function takes a string representing a municipality's name
and uf's code and returns the corresponding IBGE code (string). The function
will handle names by ignoring differences in case, accents, and
treating the character ç as c and ignoring case differences for the uf code.

Args:
  * municipality_name (str): The name of the municipality.
  * uf (str): The uf code of the state.

Returns:
  * str: The IBGE code of the municipality. Returns None if the name is not valid or does not exist.

Example:

```python
>>> from brutils import get_code_by_municipality_name
>>> get_code_by_municipality_name("São Paulo", "SP")
"3550308"
>>> get_code_by_municipality_name("goiania", "go")
"5208707"
>>> get_code_by_municipality_name("Conceição do Coité", "BA")
"2908408"
>>> get_code_by_municipality_name("conceicao do Coite", "Ba")
"2908408"
>>> get_code_by_municipality_name("Municipio Inexistente", "")
None
>>> get_code_by_municipality_name("Municipio Inexistente", "RS")
None
```

### get_municipality_by_code

Returns the municipality name and UF for a given IBGE code.

Args:
  * code (str): The IBGE code of the municipality.

Returns:
  * tuple: Returns a tuple formatted as ("Município", "UF").
  * None: Returns None if the code is not valid.

Example:

```python
>>> from brutils import get_municipality_by_code
>>> get_municipality_by_code(3550308)
("São Paulo", "SP")
```

### convert_uf_to_name
Converts a Brazilian UF code (e.g., 'SP') to the state's full name ('São Paulo').

The lookup is case-insensitive and ignores surrounding whitespace.

Args:
  * uf (str): Two-letter UF code.

Returns:
  * str | None: The full state name if found, or ``None`` if the code is invalid.

Example:

```python
>>> from brutils.ibge.uf import convert_uf_to_name
>>> convert_uf_to_name('SP')
'São Paulo'
>>> convert_uf_to_name('rj')
'Rio de Janeiro'
```

### convert_name_to_uf
Converts a Brazilian state name to its UF code.

This function takes the full name of a Brazilian state and returns its corresponding two-letter UF code. The comparison is case-insensitive and ignores accents.

Args:
  * state_name (str): The full name of the state (e.g., 'São Paulo', 'sao paulo').

Returns:
  * str | None: The UF code if found, or None if the state name is invalid.

Example:

```python
>>> from brutils.ibge.uf import convert_name_to_uf
>>> convert_name_to_uf('São Paulo')
'SP'
>>> convert_name_to_uf('sao paulo')
'SP'
>>> convert_name_to_uf('Rio de Janeiro')
'RJ'
>>> convert_name_to_uf('rio de janeiro')
'RJ'
>>> convert_name_to_uf('Invalid State')
>>>
```

## Holidays

### is_holiday

Checks if a given date is a national or state holiday in Brazil.

This function takes a `datetime` object as the date and an optional state abbreviation (UF) to specify state holidays. It returns `True` if the date is a holiday, `False` if it’s not, or `None` if the date or UF are invalid. Note that the function does not cover municipal holidays.

Args:

- `date (datetime)`: The date to be checked.
- `uf (str, optional)`: The state abbreviation (UF) to check for state holidays. If not provided, only national holidays are considered.

Returns:

- `bool | None`: `True` if the date is a holiday, `False` if it’s not, or `None` if the date or UF are invalid.

Example:

```python
>>> from datetime import datetime
>>> from brutils import is_holiday
>>> is_holiday(datetime(2024, 1, 1))
True
>>> is_holiday(datetime(2024, 1, 2))
False
>>> is_holiday(datetime(2024, 3, 2), uf="SP")
False
>>> is_holiday(datetime(2024, 12, 25), uf="RJ")
True
```

## Monetary

### format_currency

Formats a number following the Brazilian monetary standard. The number will be
formatted by adding the R$ symbol as a prefix, a comma as a decimal separator, and a
period as a thousands grouper.

Args:
  * float or Decimal: A number with or without decimal places.

Returns:
  * str or None: The number formatted following the Brazilian standard.

Example:

```python
>>> from brutils.currency import format_currency
>>> format_currency(1259.03)
'R$ 1.259,03'
>>> format_currency(0)
'R$ 0,00'
>>> format_currency("not a number")
None
```

### convert_real_to_text

Converts a given monetary value in Brazilian Reais to its textual representation. It takes a decimal number representing a monetary value in Reais and converts it to a string with the amount written out in Brazilian Portuguese. It handles both the integer part (Reais) and the fractional part (centavos), respecting the correct grammar for singular and plural cases, as well as special cases like zero and negative values.

Args:

- amount (decimal): The monetary value to be converted into text.
  - The integer part represents Reais.
  - The decimal part represents centavos.
  - 2 decimal places

Returns:

- str: A string with the monetary value written out in Brazilian Portuguese.
  - Returns "Zero reais" for a value of 0.00.
  - Returns None if the amount is invalid or absolutely greater than 1 quadrillion.
  - Handles negative values, adding "Menos" at the beginning of the string.

Limitations:
  - This function may lose precision by ±1 cent for cases where the absolute value
    is beyond trillions due to floating-point rounding errors.

Example:

```python
>>> from brutils.currency import convert_real_to_text
>>> convert_real_to_text(1523.45)
'Mil, quinhentos e vinte e três reais e quarenta e cinco centavos'
>>> convert_real_to_text(0.01)
'Um centavo'
>>> convert_real_to_text(0.00)
'Zero reais'
>>> convert_real_to_text(-50.25)
'Menos cinquenta reais e vinte e cinco centavos'
>>> convert_real_to_text("invalid")
None
```

# Feature Request and Bug Report

If you want to suggest new features or report bugs, simply create
a new [issue][github-issues], and we will respond to you there!

(To learn more about GitHub issues, check out the [official GitHub documentation][github-issues-doc]).

# Questions? Ideas?

Questions on how to use the library? New ideas for the project?
Want to share something with us? Feel free to start a thread in our
[Discussions][github-discussions], and we'll interact with you there!

(To learn more about GitHub discussions, refer to the
[official GitHub documentation][github-discussions-doc]).

# Code Contribution

Your collaboration is always very welcome! We've prepared the [CONTRIBUTING.md][contributing] file
to assist you in getting started. There, you'll find all the information you need to contribute to
the project. Please, don't hesitate to ask us using [GitHub Discussions][github-discussions] if
you encounter any difficulties or have any questions. Every bit of help counts!

Let's build it together 🚀🚀

[contributing]: CONTRIBUTING_EN.md
[github-discussions-doc]: https://docs.github.com/en/discussions
[github-discussions]: https://github.com/brazilian-utils/brutils-python/discussions
[github-issues-doc]: https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue
[github-issues]: https://github.com/brazilian-utils/brutils-python/issues

## ❤️ Contributors

<a href="https://github.com/brazilian-utils/brutils-python/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=brazilian-utils/brutils-python" />
</a></br></br>

_Made with [contrib.rocks](https://contrib.rocks)._

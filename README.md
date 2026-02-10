![Logo do Brazilian Utils](https://github.com/brazilian-utils/brand/raw/main/github-hero/github-hero-python.png)

<div align="center">

<p>Biblioteca de utilitários projetada para validar, gerar e manipular dados de acordo com as particularidades do Brasil</p>

[![codecov](https://codecov.io/gh/brazilian-utils/brutils-python/branch/main/graph/badge.svg?token=5KNECS8JYF)](https://codecov.io/gh/brazilian-utils/brutils-python)
[![Downloads per Month](https://shields.io/pypi/dm/brutils)](https://pypistats.org/packages/brutils)
[![Package version](https://shields.io/pypi/v/brutils)](https://pypi.org/project/brutils/)

### [Looking for the english version?](README_EN.md)

</div>

# Introdução

Brazilian Utils é uma biblioteca com foco na resolução de problemas que enfrentamos diariamente no
desenvolvimento de aplicações para o business Brasileiro.

- [Instalação](#instalação)
- [Utilização](#utilização)
- [Utilitários](#utilitários)
- [Novos Utilitários e Reportar Bugs](#novos-utilitários-e-reportar-bugs)
- [Dúvidas? Ideias?](#dúvidas-ideias)
- [Contribuindo com o Código do Projeto](#contribuindo-com-o-código-do-projeto)

# Instalação

```bash
pip install brutils
```

# Utilização

Para usar um de nossos utilitários, basta importar a função necessária, como no exemplo abaixo:

```python
>>> from brutils import is_valid_cpf
>>> is_valid_cpf('00011122233')
False
```

# Utilitários
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
- [Telefone](#telefone)
  - [is\_valid\_phone](#is_valid_phone)
  - [format\_phone](#format_phone)
  - [remove\_symbols\_phone](#remove_symbols_phone)
  - [remove\_international\_dialing\_code](#remove_international_dialing_code)
  - [generate\_phone](#generate_phone)
- [Email](#email)
  - [is\_valid\_email](#is_valid_email)
- [Data](#data)
- [convert\_date\_to\_text](#convert_date_to_text)
- [CNH](#cnh)
  - [is\_valid\_cnh](#is_valid_cnh)
- [Placa de Carro](#placa-de-carro)
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
- [Processo Jurídico](#processo-jurídico)
- [is\_valid\_legal\_process](#is_valid_legal_process)
  - [format\_legal\_process](#format_legal_process)
  - [remove\_symbols\_legal\_process](#remove_symbols_legal_process)
  - [generate\_legal\_process](#generate_legal_process)
- [Titulo Eleitoral](#titulo-eleitoral)
  - [is\_valid\_voter\_id](#is_valid_voter_id)
  - [format\_voter\_id](#format_voter_id)
  - [generate\_voter\_id](#generate_voter_id)
- [IBGE](#ibge)
  - [convert\_code\_to\_uf](#convert_code_to_uf)
  - [get\_code\_by\_municipality\_name](#get_code_by_municipality_name)
  - [get\_municipality\_by\_code](#get_municipality_by_code)
  - [convert\_uf\_to\_name](#convert_uf_to_name)
  - [convert\_name\_to\_uf](#convert_name_to_uf)
- [Feriados](#feriados)
  - [is\_holiday](#is_holiday)
- [Monetário](#monetário)
  - [format\_currency](#format_currency)
  - [convert\_real\_to\_text](#convert_real_to_text)
- [Natureza Jurídica](#natureza-jurídica)
  - [is\_valid\_legal\_nature](#is_valid_legal_nature)
  - [get\_legal\_nature\_description](#get_legal_nature_description)
  - [list\_all\_legal\_nature](#list_all_legal_nature)
- [RENAVAM](#renavam)
  - [is\_valid\_renavam](#is_valid_renavam)
- [Passaporte](#passaporte)
  - [is\_valid\_passport](#is_valid_passport)
  - [format\_passport](#format_passport)
  - [remove\_symbols\_passport](#remove_symbols_passport)
  - [generate\_passport](#generate_passport)

## CPF

### is_valid_cpf

Retorna se os dígitos de verificação do CPF fornecido
correspondem ao seu número base. Esta função não verifica a existência do CPF;
ela apenas valida o formato da string.

Argumentos:

- cpf (str): O CPF a ser validado, uma string de 11 dígitos

Retorna:

- bool: Verdadeiro se os dígitos de verificação corresponderem ao número base,
          Falso caso contrário.

Exemplo:

```python
>>> from brutils import is_valid_cpf
>>> is_valid_cpf("82178537464")
True
>>> is_valid_cpf('00011122233')
False
```

### format_cpf

Formata um CPF (Cadastro de Pessoa Física brasileiro) para exibição visual.
Esta função recebe uma string de CPF contendo apenas números como entrada e
adiciona símbolos de formatação padrão para exibição.

Argumentos:

- cpf (str): Uma string de CPF contendo apenas números.

Retorna:

- str: O CPF formatado com símbolos visuais se for válido,
         None se não for válido.

Exemplo:

```python
>>> from brutils import format_cpf
>>> format_cpf('82178537464')
'821.785.374-64'
>>> format_cpf("55550207753")
'555.502.077-53'
```

### remove_symbols_cpf

Remove símbolos específicos de uma string de CPF (Cadastro de Pessoa Física
brasileiro). Esta função recebe como entrada uma string de CPF e remove todas as
ocorrências dos caracteres '.', '-' dela.

Argumentos:

- cpf (str): A string de CPF contendo os símbolos a serem removidos.

Retorna:

- str: Uma nova string com os símbolos especificados removidos.

Exemplo:

```python
>>> from brutils import remove_symbols_cpf
>>> remove_symbols_cpf('000.111.222-33')
'00011122233'
```

### generate_cpf

Gerar uma string de dígitos de CPF válida aleatória.

Retorna:

- str: Um CPF válido gerado aleatoriamente.

Exemplo:

```python
>>> from brutils import generate_cpf
>>> generate_cpf()
'17433964657'
>>> generate_cpf()
"10895948109"
```

## CNPJ

### is_valid_cnpj

Verifica se os dígitos de verificação do CNPJ (Cadastro Nacional da Pessoa
Jurídica) fornecido correspondem ao seu número base. A entrada deve ser uma
string de dígitos com o comprimento apropriado. Esta função não verifica a
existência do CNPJ; ela só valida o formato da string.

Argumentos:

- cnpj (str): O CNPJ a ser validado.

Retorna:

- bool: True se os dígitos de verificação corresponderem ao número base,
        False caso contrário.

Exemplo:

```python
>>> from brutils import is_valid_cnpj
>>> is_valid_cnpj('03560714000142')
True
>>> is_valid_cnpj('00111222000133')
False
```

### format_cnpj

Formata uma string de CNPJ (Cadastro Nacional da Pessoa Jurídica) para exibição
visual.
Esta função recebe uma string de CNPJ como entrada, valida seu formato e a
formata com símbolos visuais padrão para fins de exibição.

Argumentos:

- cnpj (str): A string de CNPJ a ser formatada para exibição.

Retorna:

- str: O CNPJ formatado com símbolos visuais se for válido, None se não for válido.

Exemplo:

```python
>>> from brutils import format_cnpj
>>> format_cnpj("03560714000142")
'03.560.714/0001-42'
>>> format_cnpj("98765432100100")
None
```

### remove_symbols_cnpj

Remove símbolos específicos de uma string de CNPJ (Cadastro Nacional da Pessoa
Jurídica).
Esta função recebe uma string de CNPJ como entrada e remove todas as
ocorrências dos caracteres '.', '/' e '-' dela.

Argumentos:

- cnpj (str): A string de CNPJ que contém os símbolos a serem removidos.

Retorna:

- str: Uma nova string com os símbolos especificados removidos.

Exemplo:

```python
>>> from brutils import remove_symbols_cnpj
>>> remove_symbols_cnpj('00.111.222/0001-00')
'00111222000100'
```

### generate_cnpj

Gera uma string de dígitos CNPJ válida aleatória. Um número de filial
opcional pode ser fornecido; o padrão é 1.

Argumentos:

- branch (int): Um número de filial opcional a ser incluído no CNPJ.

Retorna:

- str: Um CNPJ válido gerado aleatoriamente.

Exemplo:

```python
>>> from brutils import generate_cnpj
>>> generate_cnpj()
'34665388000161'
>>> generate_cnpj(1234)
"01745284123455"
```

## CEP

### is_valid_cep

Verifica se um CEP (Código de Endereçamento Postal) brasileiro é válido.
Para que um CEP seja considerado válido, a entrada deve ser uma string contendo
exatamente 8 dígitos. Esta função não verifica se o CEP é um CEP real, pois
valida apenas o formato da string.

Argumentos:

- cep (str): A string contendo o CEP a ser verificado.

Retorno:

- bool: True se o CEP for válido (8 dígitos), False caso contrário.

Exemplo:

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

Formata um CEP (Código de Endereçamento Postal) brasileiro em um formato padrão.
Esta função recebe um CEP como entrada e, se for um CEP válido com 8 dígitos,
o formata no padrão "12345-678".

Argumentos:

- cep (str): O CEP (Código de Endereçamento Postal) de entrada a ser
              formatado.

Retorna:

- str: O CEP formatado no formato "12345-678" se for válido, None se não for
        válido.

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

Remove símbolos específicos de um CEP (Código de Endereçamento Postal)
fornecido. Esta função recebe um CEP como entrada e remove todas as ocorrências
dos caracteres '.' e '-' dele.

Argumentos:

- cep (str): O CEP (Código de Endereçamento Postal) de entrada que contém os
               símbolos a serem removidos.

Retorna:

- str: Uma nova string com os símbolos especificados removidos.

Exemplo:

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

Gera um número de CEP (Código de Endereçamento Postal) aleatório de 8 dígitos
como uma string.

Retorna:

- str: Um número de 8 dígitos gerado aleatoriamente.

Exemplo:

```python
>>> from brutils import generate_cep
>>> generate_cep()
'77520503'
>>> generate_cep()
'29641407'
```

### get_address_from_cep

Busca as informações de endereço a partir de um CEP (Código de Endereçamento Postal) utilizando a API da ViaCEP.

Argumentos:

- cep (str): O CEP a ser utilizado na busca.
- raise_exceptions (bool, opcional): Se deve gerar exceções quando o CEP for inválido ou não for encontrado. O padrão é False.

Retorna:

- Address | None: Um objeto Address (TypedDict) contendo as informações de endereço se o CEP for encontrado, caso contrário, None.

Exemplo:

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

Busca o CEP e outras informações a partir de um endereço utilizando a API da ViaCEP.

Argumentos:

- federal_unit (str): Abreviação de duas letras do estado brasileiro.
- city (str): Nome da cidade.
- street (str): Nome (ou substring) da rua.
- raise_exceptions (bool, opcional): Se deve gerar exceções quando o endereço é inválido ou não foi encontrado. O padrão é False.

Retorna:

- list[Address] | None: Uma lista de objetos Address (TypedDict) contendo as informações de endereço se o endereço for encontrado, None caso contrário.

Exemplo:

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

## Telefone

### is_valid_phone

Retorna se um número de telefone brasileiro é válido conforme o formato da string.
Não verifica se o número realmente existe.
```

is_valid_phone(phone_number, type)

```

Argumentos:

- phone_number (str):
  - o número de telefone a ser validado
  - apenas dígitos, sem símbolos
  - sem o código do país
  - deve incluir o número de DDD com dois dígitos
  - exemplo: '+55 48 9999 9999' deve ser utilizado como '4899999999'
  - obrigatório

- type (str):
  - 'mobile' para validar apenas números de celular
  - 'landline' para validar apenas números de telefone fixo
  - caso não especificado, valida para um para o outro.
  - opcional

Retorna:

- bool: True se o número é válido, False caso contrário.

Exemplo:

```python
>>> from brutils import is_valid_phone
>>> is_valid_phone('11994029275')
True
>>> is_valid_phone('11994029275', 'mobile')
True
>>> is_valid_phone('1938814933', 'landline')
True
```

### format_phone

Formata um número de telefone para exibição visual. Esta função recebe uma string representando um número de telefone contendo apenas números como entrada e adiciona símbolos de formatação padrão para exibição.

Argumentos:

- phone (str): Uma string representando um número de telefone.

Retorna:

- str: O número de telefone formatado para exibição ou None se não for válido.

Exemplo:

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

Remove símbolos do número de telefone. Esta função recebe um número de telefone como entrada e remove todos os símbolos, como parênteses '()', traços '-' e espaços ' '.

Argumentos:

- phone (str): O número de telefone de entrada que contém os símbolos a serem removidos.

Retorna:

- str: Uma nova string com os símbolos especificados removidos.

Exemplo:

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

Remove o código internacional (+55) de uma string que contém um número de telefone brasileiro, mantendo outros caracteres especiais.

Argumentos:

- phone (str): O número de telefone de entrada que pode conter o código internacional.

Retorna:

- str: Uma nova string sem o código internacional, preservando outros caracteres especiais.

Exemplo:

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

Gera um número de telefone aleatório válido.

Argumentos:

- type (str): Pode ser "landline" ou "mobile".
                Se não for especificado, a função gera um número
                aleatório de qualquer tipo.

Retorna:

- str: Um número de telefone válido gerado aleatoriamente.

Exemplo:

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

Verificar se uma string corresponde a um endereço de e-mail válido.

Argumentos:

- email (str): A string de entrada a ser verificada.

Retorna:

- bool: Verdadeiro se o email for um endereço de e-mail válido, Falso
          caso contrário.

Exemplo:

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

## Data

## convert_date_to_text

Converte uma data em sua representação textual.

Argumentos:
 - date (str): Uma string no formato dd/mm/aaaa

Retorna:
 - A represetação textual da data ou None caso a data esteja mal formatada ou a data seja inválida.

Exemplo:

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

## CNH

### is_valid_cnh

Verifica se o número de registro de CNH (Carteira de Habilitação Nacional) brasileiro é válido.
Para que um número de CNH seja considerado válido, a entrada deve ser uma string contendo
exatamente 11 dígitos numéricos. Esta função não verifica se o número da CNH é real, apenas
valida os dígitos verificadores.

Argumentos:

- cnh (str): A string contendo o número de registro de CNH a ser verificado.

Retorno:

- bool: True se o número de registro da CNHN for válido (11 dígitos), False caso contrário.

Exemplo:

```python
>>> from brutils import is_valid_cnh
>>> is_valid_cnh("12345678901")
False
>>> is_valid_cnh("A2C45678901")
False
>>> is_valid_cnh("98765432100")
True
>>> is_valid_cnh("987654321-00")
True
```


## Placa de Carro

### is_valid_license_plate

Verifica se uma placa de carro é válida.
Esta função não verifica se a placa de carro é uma placa de carro real,
apenas valida o formato da string.

Argumentos:

- license_plate (str): Uma string representando uma placa de carro.
- type (str): "old_format" ou "mercosul".
                Se não especificado, verifica um ou outro.

Retorna:

- bool: True se a placa de carro for válida, False caso contrário.

Exemplo:

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

Formata uma placa de carro no padrão correto.
Esta função recebe uma placa de carro em qualquer formato (LLLNNNN ou LLLNLNN) e retorna uma versão formatada.

Argumentos:

- license_plate (str): Uma string representando uma placa de carro.

Retorna:

- str: A string da placa de carro formatada ou
         'None' se a entrada for inválida.

Exemplo:

```python
>>> from brutils import format_license_plate
>>> format_license_plate("ABC1234")
"ABC-1234"
# formato antigo (contém traço)
>>> format_license_plate("abc1234")
"ABC-1234"
# formato antigo (contém traço)
>>> format_license_plate("ABC1D23")
"ABC1D23"
# formato mercosul
>>> format_license_plate("abc1d23")
"ABC1D23"
# formato mercosul
>>> format_license_plate("ABCD123")
None
```

### remove_symbols_license_plate

Remove o símbolo de hífen (-) de uma string de placa de carro.

Argumentos:

- license_plate_number (str): Uma string de placa de carro contendo símbolos a serem removidos.

Retorna:

- str: A string da placa de carro com os símbolos especificados removidos.

Exemplo:

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

Gera uma placa de carro válida no formato especificado. Caso nenhum formato seja fornecido, ele retornará uma placa de carro no formato Mercosul.

Argumentos:

- format (str): O formato desejado para a placa de carro. 'LLLNNNN' para o formato antigo ou 'LLLNLNN' para o formato Mercosul. O padrão é 'LLLNLNN'.

Retorna:

- str: Um número de placa de carro gerado aleatoriamente ou
   None se o formato for inválido.

Exemplo:

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

Converte uma placa de carro no formato antigo (LLLNNNN) para o formato Mercosul (LLLNLNN).

Argumentos:

- license_plate(str): Uma string com o tamanho adequado que representa a placa no formato antigo.

Retorna:

- str: A placa Mercosul convertida (LLLNLNN) ou None se a entrada for inválida.

Exemplo:

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

Retorna o formato de uma placa de carro. 'LLLNNNN' para o formato antigo e
'LLLNLNN' para o formato Mercosul.

Argumentos:

- license_plate (str): Uma string de placa de carro sem símbolos.

Retorna:

- str: O formato da placa de carro (LLLNNNN, LLLNLNN) ou
         'None' se o formato for inválido.

Exemplo:

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

Verifica se o número PIS/PASEP é valido. Apenas números, formatados como string. Não verifica se o PIS/PASEP realmente existe.

Referências:

- <https://www.macoratti.net/alg_pis.htm>.

Argumentos:

- pis (str): Número PIS como uma string com o comprimento apropriado.

Retorna:

- bool: True se o PIS for válido, False caso contrário.

Exemplo:

```python
from brutils import is_valid_pis
>>> is_valid_pis("82178537464")
False
>>> is_valid_pis("12082043519")
True
```

### format_pis

Formata uma string de PIS (Programa de Integração Social) válida com símbolos e adiciona símbolos de formatação padrão para exibição.

Argumentos:

- pis (str): Uma string válida de PIS contendo apenas números.

Retorna:

- str: Uma string de PIS formatada com símbolos visuais padrão ou None se a entrada for inválida.

Exemplo:

```python
from brutils import format_pis
>>> format_pis("17033259504")
'170.33259.50-4'
>>> format_pis("12013128292")
'120.13128.29-2'
```

### remove_symbols_pis

Esta função recebe uma string de PIS (Programa de Integração Social) com símbolos de formatação e retorna uma versão limpa sem símbolos. Remove apenas os símbolos "-" e "." , propositalmente não remove outros símbolos.

Argumentos:

- pis (str): Uma string de PIS que pode conter símbolos de formatação.

Retorna:

- str: Uma string de PIS limpa, sem símbolos de formatação.

Exemplo:

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

Gera uma string de dígitos contendo um número de um PIS brasileiro válido aleatório.

Retorna:

- str: Um número PIS válido gerado aleatoriamente como string.

Exemplo:

```python
from brutils import generate_pis
>>> generate_pis()
'61352489741'
>>> generate_pis()
'73453349671'
```

## Processo Jurídico

## is_valid_legal_process

Verifica se um ID de processo jurídico é válido, não verifica se o ID de processo jurídico é um ID de processo
jurídico real; ela apenas valida o formato da string.

Argumentos:

- legal_process_id (str): Uma string contendo apenas dígitos que representa
                            o ID do processo jurídico.

Retorna:

- bool: True se o ID do processo jurídico for válido, False caso
          contrário.

Examplo:

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

Formata um ID de processo jurídico em um formato padrão.

Argumentos:

- legal_process_id (str): Uma string de 20 dígitos que representa o ID do
                            processo jurídico.

Retorna:

- str: O ID do processo jurídico formatado ou None se a entrada for inválida.

Exemplo:

```python
>>> from brutils import format_legal_process
>>> format_legal_process('23141945820055070079')
'2314194-58.2005.5.07.0079'
>>> format_legal_process('00000000000000000000')
'0000000-00.0000.0.00.0000'
>>>
```

### remove_symbols_legal_process

Remove símbolos específicos de um processo jurídico fornecido.

Esta função recebe um processo jurídico como entrada e remove todas as
ocorrências dos caracteres '.' e '-' dele.

Argumentos:

- legal_process (str): Um processo jurídico contendo símbolos a serem
                         removidos.

Retorna:

- str: A string do processo jurídico com os símbolos especificados removidos.

Exemplo:

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

Gera um número válido aleatório de ID de processo jurídico.

Argumentos:

- year (int): O ano para o ID do processo jurídico (o padrão é o ano atual).
                Não pode ser um ano do passado.
- orgao (int): O órgão (1-9) para o ID do processo jurídico
                 (o padrão é aleatório).

Retorna:

- str: Um ID de processo jurídico gerado aleatoriamente.
         None caso algum dos argumento seja inválido.

Exemplo:

```python
>>> from brutils import generate_legal_process
>>> generate_legal_process()
"45676401020238170592"
>>> generate_legal_process(ano=2025)
"32110268020258121130"
>>> generate_legal_process(orgao=5)
"37573041520235090313"
>>> generate_legal_process(ano=2024, orgao=4)
"33158248820244017105"
```

## Titulo Eleitoral

### is_valid_voter_id

Verifica se um número de Título de Eleitor brasileiro é válido. Não verifica se realmente existe.

Referências:

- <https://pt.wikipedia.org/wiki/T%C3%ADtulo_de_eleitor>
- <http://clubes.obmep.org.br/blog/a-matematica-nos-documentos-titulo-de-eleitor/>

Argumentos:

- voter_id (str): string representando o número do título de eleitor a ser verificado.

Retorna:

- bool: True se o número do título de eleitor for válido. False, caso contrário.

Exemplo:

```python
>>> from brutils import is_valid_voter_id
>>> is_valid_voter_id('123456789011')
False
>>> is_valid_voter_id('427503840213')
True
```

### format_voter_id

Formata um número de Título de Eleitor para exibição visual.

Esta função recebe uma string de Título de Eleitor contendo
apenas números como entrada e adiciona os espaços de formatação
padrão para exibição.

Argumentos:
  * voter_id (str): Uma string de Título de Eleitor contendo apenas números.

Retorna:
  * str: O Título de Eleitor formatado com os espaços, se for válido.
         Retorna None se não for válido.

Exemplo:

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

Gera uma string de dígitos de Título de Eleitor válida aleatória a partir de um estado brasileiro informado.

Args:
  * federative_union (str): Unidade Federativa para o título de eleitor que será gerado. O valor padrão "ZZ" é usado para Títulos de Eleitor emitidos para estrangeiros.

Retorna:
  * str: Um Título de Eleitor válido gerado aleatoriamente.

Exemplo:

```python
>>> from brutils import generate_voter_id
>>> generate_voter_id()
'183475722801'
>>> generate_voter_id(federative_union ="MG")
'950125640248'
```

## IBGE

### convert_code_to_uf
Converte um determinado código do IBGE (string de 2 dígitos) para sua UF (abreviatura estadual) correspondente.

Args:
  * code (str): O código IBGE de 2 dígitos a ser convertido.

Retorna:
  * str or None: O código UF correspondente ao código IBGE, ou None se o
                 código IBGE for inválido.

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

Retorna o código IBGE para um dado nome de município e código de UF.

Essa função recebe uma string representando o nome de um município e o código da UF, e retorna o código IBGE correspondente (string). A função lida com os nomes ignorando diferenças de maiúsculas, acentos, tratando o caractere "ç" como "c", e ignorando diferenças de maiúsculas para o código da UF.

Argumentos:
  * municipality_name (str): O nome do município.
  * uf (str): O código UF do estado.

Retorna:
  * str: O código IBGE do município. Retorna None se o nome não for válido ou não existir.

Exemplo:

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

Retorna o nome do município e a UF para um código do IBGE.

Args:
  * code (str): O código do IBGE para o município.

Returns:
  * tuple: Retorna uma Tupla formatado como ("Município", "UF").
  * None: Retorna None se o código for inválido.

Example:

```python
>>> from brutils import get_municipality_by_code
>>> get_municipality_by_code(3550308)
("São Paulo", "SP")
```

### convert_uf_to_name
Converte um código de UF brasileiro (por exemplo, 'SP') no nome completo do estado ('São Paulo').

A busca é case-insensitive (não diferencia maiúsculas de minúsculas) e ignora espaços em branco ao redor.

Argumentos:
  * uf (str): Código de UF com duas letras.

Retorna:
  * str | None: O nome completo do estado, ou ``None`` se o código for inválido.

Exemplo:

```python
>>> from brutils.ibge.uf import convert_uf_to_name
>>> convert_uf_to_name('SP')
'São Paulo'
>>> convert_uf_to_name('rj')
'Rio de Janeiro'
```

### convert_name_to_uf
Converte o nome completo de um estado brasileiro para seu código UF.

Esta função recebe o nome completo de um estado brasileiro e retorna o código UF de duas letras correspondente. A comparação ignora maiúsculas/minúsculas e acentos.

Argumentos:
  * state_name (str): O nome completo do estado (por exemplo, 'São Paulo', 'sao paulo').

Retorna:
  * str | None: O código UF se encontrado, ou None se o nome do estado for inválido.

Exemplo:

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
>>> convert_name_to_uf('Estado Inválido')
>>>
```

## Feriados

### is_holiday

Verifica se uma determinada data é um feriado nacional ou estadual no Brasil.

Esta função recebe um objeto `datetime` como a data e uma UF opcional (Unidade Federativa) para especificar feriados estaduais. Retorna `True` se a data for um feriado, `False` se não for, ou `None` se a data ou UF forem inválidas. Nota: a função não abrange feriados municipais.

Argumentos:

- `date (datetime)`: A data a ser verificada.
- `uf (str, opcional)`: A abreviação do estado (UF) para verificar feriados estaduais. Se não fornecido, apenas feriados nacionais são considerados.

Retorna:

- `bool | None`: `True` se a data for um feriado, `False` se não for, ou `None` se a data ou UF forem inválidas.

Exemplo:

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

## Monetário

### format_currency

Formata um número seguindo o padrão monetário brasileiro. O número será formatado
adicionando o símbolo R$ como prefixo, vírgula como separador decimal, e ponto como
agrupador de milhar.

Argumentos:
  * float ou Decimal: Um número com ou sem casas decimais.

Retorna:
  * str ou None: O número formatado seguindo o padrão brasileiro.

Exemplo:

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

Converte um valor monetário em reais para sua representação por extenso. Esta função recebe um número decimal representando um valor monetário em reais e o converte para uma string com o valor escrito por extenso em português do Brasil. Ela trata tanto a parte inteira (reais) quanto a parte fracionária (centavos), respeitando a gramática correta para os casos de singular e plural, bem como casos especiais como zero e valores negativos.

Argumentos:
- amount (decimal): O valor monetário a ser convertido por extenso.
  - A parte inteira representa os reais.
  - A parte decimal representa os centavos.
  - 2 casas decimais.

Retorna:
- str: Uma string com o valor monetário escrito por extenso em português do Brasil.
  - Retorna "Zero reais" para o valor 0,00.
  - Retorna None se o valor for inválido ou absolutamente maior que 1 quatrilhão.
  - Trata valores negativos, adicionando "Menos" no início da string.

Limitações:
  - Esta função pode perder precisão em ±1 centavo para casos em que o valor absoluto
    ultrapasse trilhões devido a erros de arredondamento de ponto flutuante.

Exemplo:

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

## Natureza Jurídica

### is_valid_legal_nature

Valida se o código informado existe na tabela oficial. Aceita `NNNN` ou `NNN-N`.  
O valor é **normalizado** antes da checagem: remove espaços, mantém apenas dígitos e aceita hífen entre o 3º e 4º dígitos.

**Argumentos**
- `code (str)`: Código de 4 dígitos (ex.: `"2062"` ou `"206-2"`)

**Retorna**
- `bool`: `True` se existir na tabela, `False` caso contrário.

**Exemplo**
```python
>>> from brutils import legal_nature
>>> legal_nature.is_valid("2062")   
True
>>> legal_nature.is_valid("206-2")  
True
>>> legal_nature.is_valid("9999")   
False
```

### get_legal_nature_description

Retorna a **descrição oficial** do código de Natureza Jurídica. Aceita `NNNN` ou `NNN-N`. Aplica a mesma normalização do `is_valid`.

**Argumentos**

* `code (str)`: Código de 4 dígitos

**Retorna**

* `str | None`: Descrição correspondente ou `None` se o código for inválido ou inexistente.

**Exemplo**

```python
>>> from brutils import legal_nature
>>> legal_nature.get_description("2062")   
'Sociedade Empresária Limitada'
>>> legal_nature.get_description("101-5")  
'Órgão Público do Poder Executivo Federal'
>>> legal_nature.get_description("0000")   
None
```

### list_all_legal_nature

Retorna uma cópia do dicionário completo `{codigo: descricao}`.

**Retorna**

* `dict[str, str]`: Mapeamento de todos os códigos para suas descrições.

**Exemplo**

```python
>>> from brutils import legal_nature 
>>> data = legal_nature.list_all()
>>> len(data) > 0               
True
>>> data["2062"]                 
'Sociedade Empresária Limitada'
```

## RENAVAM

### is_valid_renavam

Valida se os dígitos de verificação do RENAVAM fornecido
correspondem aos seus 10 dígitos iniciais. Esta função não verifica a existência do veículo;
ela apenas valida o formato da string e o dígito verificador.

Argumentos:

- renavam (str): O RENAVAM a ser validado, uma string de 11 dígitos.

Retorna:

- bool: Verdadeiro se o RENAVAM for válido  
  Falso caso contrário.

Exemplo:

```python
>>> from brutils import is_valid_renavam
>>> is_valid_renavam("86769597308")
True
>>> is_valid_renavam("12345678901")
False
```

## Passaporte

### is_valid_passport

Verifica se um número de passaporte brasileiro é válido.

Para ser considerado válido, a entrada deve ser uma string contendo exatamente dois caracteres alfabéticos seguidos de exatamente seis dígitos numéricos.

Esta função não verifica se a entrada é um número de passaporte real, pois não existem dígitos verificadores para o passaporte brasileiro.

Argumentos:
- passport (str): A string contendo o número do passaporte a ser verificado.

Retorna:
- bool: True se o número do passaporte for válido (2 letras seguidas de 6 dígitos). False caso contrário.

Exemplo: 
```python
>>> from brutils import is_valid_passport
>>> is_valid_passport("Ab123456")
True
>>> is_valid_passport("12345678")
False
>>> is_valid_passport("DC-221345")
False
```
### format_passport

Formata um número de passaporte brasileiro para exibição.

Esta função recebe uma string representando um número de passaporte válido e o retorna formatado (maiúsculas, sem símbolos).

Argumentos:
- passport (str | None): Um número de passaporte brasileiro (minúsculas ou maiúsculas, possivelmente incluindo símbolos)

Retorna:
- str: O número do passaporte formatado (maiúsculas, sem símbolos) ou None se a entrada for inválida

Exemplo:
```python
>>> from brutils import format_passport
>>> format_passport("Ab123456")
AB123456
>>> format_passport("Ab-123456")
AB123456
>>> format_passport("111111")
None
```
### remove_symbols_passport

Remove símbolos ('-', '.' e espaços em branco) de um número de passaporte.

Esta função recebe uma string com um número de passaporte como entrada e remove todas as ocorrências dos caracteres '.', '-' e espaço em branco.

Argumentos:
- passport (str): A string contendo um número de passaporte

Retorna:
- str: O número do passaporte com hífens (-), pontos (.) e espaços em branco ( ) removidos.

Exemplo:
```python 
>>> from brutils import remove_symbols_passport
>>> remove_symbols_passport("Ab123456")
Ab123456
>>> remove_symbols_passport("Ab-123456")
Ab123456
>>> remove_symbols_passport("Ab -. 123456")
Ab123456
```
### generate_passport

Gera uma string com um número de passaporte brasileiro válido aleatório.

Esta função gera uma string com um número de passaporte brasileiro aleatório.

Retorna:
- str: Uma string com um número de passaporte válido aleatório.

Exemplo:
```python 
>>> from brutils import generate_passport
>>> generate_passport()
"RY393097"
>>> generate_passport()
"ZS840088"
```

# Novos Utilitários e Reportar Bugs

Caso queira sugerir novas funcionalidades ou reportar bugs, basta criar
uma nova [issue][github-issues] e iremos lhe responder por lá!

(Para saber mais sobre github issues, confira a [documentação oficial do GitHub][github-issues-doc]).

# Dúvidas? Ideias?

Dúvidas de como utilizar a biblioteca? Novas ideias para o projeto?
Quer compartilhar algo com a gente? Fique à vontade para criar um tópico no nosso
[Discussions][github-discussions] que iremos interagir por lá!

(Para saber mais sobre github discussions, confira a
[documentação oficial do GitHub][github-discussions-doc]).

# Contribuindo com o Código do Projeto

Sua colaboração é sempre muito bem-vinda! Preparamos o arquivo [CONTRIBUTING.md][contributing] para
te ajudar nos primeiros passos. Lá você encontrará toda a informação necessária para contribuir com
o projeto. Não hesite em nos perguntar utilizando o [GitHub Discussions][github-discussions] caso
haja qualquer dificuldade ou dúvida. Toda ajuda conta!

Vamos construir juntos! 🚀🚀

[contributing]: CONTRIBUTING.md
[github-discussions-doc]: https://docs.github.com/pt/discussions
[github-discussions]: https://github.com/brazilian-utils/brutils-python/discussions
[github-issues-doc]: https://docs.github.com/pt/issues/tracking-your-work-with-issues/creating-an-issue
[github-issues]: https://github.com/brazilian-utils/brutils-python/issues

## ❤️ Quem já Contribuiu

<a href="https://github.com/brazilian-utils/brutils-python/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=brazilian-utils/brutils-python" />
</a></br></br>

_Feito por [contrib.rocks](https://contrib.rocks)._

# Prompt ChatGPT para Criar Issues

## Exemplo: formatar moeda brasileira

- Criar uma issue para o repositório brutils-python.
- Issue: formatar moeda brasileira
- nome da função: format_brl
- entrada: float
- saída: string formatada
- caso entrada seja inválida, retornar None
- Não implementar a lógica da função. Apenas deixar a docstring e um comentário `# implementar a lógica da função aqui`
- Considerar o maior número de edge cases possíveis
- Criar testes unitários para todos os edge cases
- Estes são os utilitários já existentes na lib:

```md
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
- [Título Eleitoral](#titulo-eleitoral)
  - [is_valid_voter_id](#is_valid_voter_id)
  - [format_voter_id](#format_voter_id)
  - [generate_voter_id](#generate_voter_id)
- [IBGE](#ibge)
  - [convert_code_to_uf](#convert_code_to_uf)
```

- Seguindo exatamento o mesmo modelo dessa issue:

```md
Título da Issue: Conversão de Nome de Estado para UF

**Seu pedido de recurso está relacionado a um problema? Por favor, descreva.**

Dado o nome completo de um estado brasileiro, quero obter o código de Unidade Federativa (UF) correspondente. Isso é útil para conversão de nomes completos de estados em siglas utilizadas em sistemas e documentos.

Por exemplo, converter `"São Paulo"` para `"SP"`.

**Descreva a solução que você gostaria**

* Uma função `convert_text_to_uf`, que recebe o nome completo do estado (string) e retorna o código UF correspondente.
* A função deve ignorar maiúsculas e minúsculas, e também deve desconsiderar acentos e o caractere especial ç (considerando c também).
* A função deve verificar se o nome completo é válido e retornar o código UF correspondente.
* Se o nome completo não for válido, a função deve retornar `None`.
* A função deve lidar com todos os estados e o Distrito Federal do Brasil.
* A lista das UFs e seus nomes completos já existe no arquivo `brutils/data/enums/uf.py`. Ela deve ser reutilizada.

**Descreva alternativas que você considerou**

1. Seguir até o passo 8 do [guia de contribuição](https://github.com/brazilian-utils/brutils-python/blob/main/CONTRIBUTING.md#primeira-contribui%C3%A7%C3%A3o).

2. Como parte do passo 8, criar o arquivo: `brutils-python/brutils/ibge/uf.py`.

    ```python
    def convert_text_to_uf(state_name): # type: (str) -> str | None
        """
        Converts a given Brazilian state full name to its corresponding UF code.

        This function takes the full name of a Brazilian state and returns the corresponding
        2-letter UF code. It handles all Brazilian states and the Federal District.

        Args:
            state_name (str): The full name of the state to be converted.

        Returns:
            str or None: The UF code corresponding to the full state name,
                or None if the full state name is invalid.

        Example:
            >>> convert_text_to_uf('São Paulo')
            "SP"
            >>> convert_text_to_uf('Rio de Janeiro')
            "RJ"
            >>> convert_text_to_uf('Minas Gerais')
            "MG"
            >>> convert_text_to_uf('Distrito Federal')
            "DF"
            >>> convert_text_to_uf('Estado Inexistente')
            None
        """
        # implementar a lógica da função aqui
    ```

    Importar a nova função no arquivo `brutils-python/brutils/__init__.py`:

    ```python
    # UF Imports
    from brutils.ibge.uf import (
        convert_text_to_uf,
    )
    ```

    E adicionar o nome da nova função na lista `__all__` do mesmo arquivo `brutils-python/brutils/__init__.py`:

    ```python
    __all__ = [
        ...
        # UF
        'convert_text_to_uf',
    ]
    ```

3. Como parte do passo 9, criar o arquivo de teste: `brutils-python/tests/test_uf.py`.

    ```python
    from unittest import TestCase
    from brutils.ibge.uf import convert_text_to_uf


    class TestUF(TestCase):
        def test_convert_text_to_uf(self):
            # Testes para nomes válidos
            self.assertEqual(convert_text_to_uf("São Paulo"), "SP")
            self.assertEqual(convert_text_to_uf("Rio de Janeiro"), "RJ")
            self.assertEqual(convert_text_to_uf("Minas Gerais"), "MG")
            self.assertEqual(convert_text_to_uf("Distrito Federal"), "DF")
            self.assertEqual(
                convert_text_to_uf("são paulo"), "SP"
            )  # Teste com minúsculas
            self.assertEqual(
                convert_text_to_uf("riO de janeiRo"), "RJ"
            )  # Teste com misturas de maiúsculas e minúsculas
            self.assertEqual(
                convert_text_to_uf("minas gerais"), "MG"
            )  # Teste com minúsculas
            self.assertEqual(
                convert_text_to_uf("sao paulo"), "SP"
            )  # Teste sem acento

            # Testes para nomes inválidos
            self.assertIsNone(
                convert_text_to_uf("Estado Inexistente")
            )  # Nome não existe
            self.assertIsNone(convert_text_to_uf(""))  # Nome vazio
            self.assertIsNone(convert_text_to_uf("123"))  # Nome com números
            self.assertIsNone(
                convert_text_to_uf("São Paulo SP")
            )  # Nome com sigla incluída
            self.assertIsNone(convert_text_to_uf("A"))  # Nome com letra não mapeada
            self.assertIsNone(
                convert_text_to_uf("ZZZ")
            )  # Nome com mais de 2 letras

            # implementar mais casos de teste aqui se necessário
    ```

4. Seguir os passos seguintes do [guia de contribuição](https://github.com/brazilian-utils/brutils-python/blob/main/CONTRIBUTING.md#primeira-contribui%C3%A7%C3%A3o).

**Contexto adicional**

* A lista de estados e suas siglas é definida pelo Instituto Brasileiro de Geografia e Estatística (IBGE). Para mais detalhes, consulte o [site do IBGE](https://atendimento.tecnospeed.com.br/hc/pt-br/articles/360021494734-Tabela-de-C%C3%B3digo-de-UF-do-IBGE).
* A função deve lidar com a normalização de texto, incluindo a remoção de acentos e a conversão para minúsculas para garantir que o texto seja comparado de forma consistente.
```

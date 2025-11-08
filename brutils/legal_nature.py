"""
brutils.legal_nature
~~~~~~~~~~~~~~~~~~~~~~~~~

Utilities for consulting and validating the official
*Natureza Jurídica* (Legal Nature) codes defined by the
Receita Federal do Brasil (RFB).

.. note::
    The codes and descriptions in this module are sourced from the
    official **Tabela de Natureza Jurídica** (RFB), as provided in the
    document used by the Cadastro Nacional (e.g., FCN).

    This module offers simple lookups and validation helpers based on
    the official table. It does not infer the current legal/registration
    status of any entity.

    Source: https://www.gov.br/empresas-e-negocios/pt-br/drei/links-e-downloads/arquivos/TABELADENATUREZAJURDICA.pdf
"""

from typing import Dict, Optional

# FORMATTING
############


# Helper to normalize inputs like "101-5" => "1015"
def _normalize(code: str) -> Optional[str]:
    if not isinstance(code, str):
        return None

    digits = "".join(ch for ch in code.strip() if ch.isdigit())

    return digits if len(digits) == 4 else None


LEGAL_NATURE: Dict[str, str] = {
    # 1. ADMINISTRAÇÃO PÚBLICA
    "1015": "Órgão Público do Poder Executivo Federal",
    "1023": "Órgão Público do Poder Executivo Estadual ou do Distrito Federal",
    "1031": "Órgão Público do Poder Executivo Municipal",
    "1040": "Órgão Público do Poder Legislativo Federal",
    "1058": "Órgão Público do Poder Legislativo Estadual ou do Distrito Federal",
    "1066": "Órgão Público do Poder Legislativo Municipal",
    "1074": "Órgão Público do Poder Judiciário Federal",
    "1082": "Órgão Público do Poder Judiciário Estadual",
    "1104": "Autarquia Federal",
    "1112": "Autarquia Estadual ou do Distrito Federal",
    "1120": "Autarquia Municipal",
    "1139": "Fundação Federal",
    "1147": "Fundação Estadual ou do Distrito Federal",
    "1155": "Fundação Municipal",
    "1163": "Órgão Público Autônomo da União",
    "1171": "Órgão Público Autônomo Estadual ou do Distrito Federal",
    "1180": "Órgão Público Autônomo Municipal",
    # 2. ENTIDADES EMPRESARIAIS
    "2011": "Empresa Pública",
    "2038": "Sociedade de Economia Mista",
    "2046": "Sociedade Anônima Aberta",
    "2054": "Sociedade Anônima Fechada",
    "2062": "Sociedade Empresária Limitada",
    "2076": "Sociedade Empresária em Nome Coletivo",
    "2089": "Sociedade Empresária em Comandita Simples",
    "2097": "Sociedade Empresária em Comandita por Ações",
    "2100": "Sociedade Mercantil de Capital e Indústria (extinta pelo NCC/2002)",
    "2127": "Sociedade Empresária em Conta de Participação",
    "2135": "Empresário (Individual)",
    "2143": "Cooperativa",
    "2151": "Consórcio de Sociedades",
    "2160": "Grupo de Sociedades",
    "2178": "Estabelecimento, no Brasil, de Sociedade Estrangeira",
    "2194": "Estabelecimento, no Brasil, de Empresa Binacional Argentino-Brasileira",
    "2208": "Entidade Binacional Itaipu",
    "2216": "Empresa Domiciliada no Exterior",
    "2224": "Clube/Fundo de Investimento",
    "2232": "Sociedade Simples Pura",
    "2240": "Sociedade Simples Limitada",
    "2259": "Sociedade em Nome Coletivo",
    "2267": "Sociedade em Comandita Simples",
    "2275": "Sociedade Simples em Conta de Participação",
    "2305": "Empresa Individual de Responsabilidade Limitada",
    # 3. ENTIDADES SEM FINS LUCRATIVOS
    "3034": "Serviço Notarial e Registral (Cartório)",
    "3042": "Organização Social",
    "3050": "Organização da Sociedade Civil de Interesse Público (Oscip)",
    "3069": "Outras Formas de Fundações Mantidas com Recursos Privados",
    "3077": "Serviço Social Autônomo",
    "3085": "Condomínio Edilícios",
    "3093": "Unidade Executora (Programa Dinheiro Direto na Escola)",
    "3107": "Comissão de Conciliação Prévia",
    "3115": "Entidade de Mediação e Arbitragem",
    "3123": "Partido Político",
    "3131": "Entidade Sindical",
    "3204": "Estabelecimento, no Brasil, de Fundação ou Associação Estrangeiras",
    "3212": "Fundação ou Associação Domiciliada no Exterior",
    "3999": "Outras Formas de Associação",
    # 4. PESSOAS FÍSICAS
    "4014": "Empresa Individual Imobiliária",
    "4022": "Segurado Especial",
    "4081": "Contribuinte individual",
    # 5. ORGANIZAÇÕES INTERNACIONAIS E OUTRAS INSTITUIÇÕES EXTRATERRITORIAIS
    "5002": "Organização Internacional e Outras Instituições Extraterritoriais",
}

# OPERATIONS
############


def is_valid(code: str) -> bool:
    """
    Check if a string corresponds to a valid *Natureza Jurídica* code.

    Args:
        code (str): The code to be validated. Accepts either "NNNN" or "NNN-N".

    Returns:
        bool: True if the normalized code exists in the official table, False otherwise.

    Example:
        >>> is_valid("2062")
        True
        >>> is_valid("206-2")
        True
        >>> is_valid("9999")
        False

    .. note::
        Validation is based solely on the presence of the code in the
        official RFB table. It does not verify the current legal status
        or registration of the entity.
    """
    normalized = _normalize(code)
    return normalized in LEGAL_NATURE if normalized else False


def get_description(code: str) -> Optional[str]:
    """
    Retrieve the description of a *Natureza Jurídica* code.

    Args:
        code (str): The code to look up. Accepts either "NNNN" or "NNN-N".

    Returns:
        str | None: The full description if the code is valid, otherwise None.

    Example:
        >>> get_description("2062")
        'Sociedade Empresária Limitada'
        >>> get_description("101-5")
        'Órgão Público do Poder Executivo Federal'
        >>> get_description("0000")
        None
    """
    normalized = _normalize(code)
    return LEGAL_NATURE.get(normalized) if normalized else None


def list_all() -> Dict[str, str]:
    """
    Return a copy of the full *Natureza Jurídica* table.

    Returns:
        dict[str, str]: Mapping from "NNNN" codes to descriptions.
    """
    return dict(LEGAL_NATURE)

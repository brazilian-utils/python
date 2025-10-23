# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Automatiza geração do CHANGELOG com git-cliff
- Add close-stale-issues-v1.yml by @niltonpimentel02 in [#661](https://github.com/brazilian-utils/python/pull/661)
- Add Natureza Jurídica utilities by @MatheusPaivaa in [#653](https://github.com/brazilian-utils/python/pull/653)
- Renavam add is_valid_renavam function with validation, tests, and docs by @Fontebasso-JV in [#652](https://github.com/brazilian-utils/python/pull/652)
- Adiciona suporte a anotações modernas em voter_id by @felipecolen in [#638](https://github.com/brazilian-utils/python/pull/638)
- Adiciona suporte a anotações modernas em legal_process by @felipecolen in [#634](https://github.com/brazilian-utils/python/pull/634)
- CNH add is_valid_cnh function with validation, tests, and docs by @willkraemer in [#651](https://github.com/brazilian-utils/python/pull/651)
- Adiciona utilitário convert_name_to_uf by @morais90 in [#606](https://github.com/brazilian-utils/python/pull/606)

### Changed
- Remover diretório 'types' que não está mais sendo utilizado by @rochamrcs in [#650](https://github.com/brazilian-utils/python/pull/650)
- Migrar type hints de license_plate.py de acordo com PEP 484 by @lucasjl in [#646](https://github.com/brazilian-utils/python/pull/646)
- Migração  de type hints para anotações modernas by @camilotmundim in [#637](https://github.com/brazilian-utils/python/pull/637)
- Adiciona suporte a anotações modernas em phone.py by @willkraemer in [#636](https://github.com/brazilian-utils/python/pull/636)
- Adiciona img de capa aos arquivos README by @camilamaia in [#612](https://github.com/brazilian-utils/python/pull/612)
- Add commit message for release pr by @niltonpimentel02 in [#602](https://github.com/brazilian-utils/python/pull/602)

### Fixed
- Corrigir conflito entre módulo local types e módulo padrão types by @rochamrcs in [#647](https://github.com/brazilian-utils/python/pull/647)
- Teste intermitente by @camilamaia in [#605](https://github.com/brazilian-utils/python/pull/605)
- Add new options to bot by @niltonpimentel02 in [#603](https://github.com/brazilian-utils/python/pull/603)
- Delete cleanup-inactive-issues.yml by @niltonpimentel02 in [#600](https://github.com/brazilian-utils/python/pull/600)
- Delete stale.yml by @niltonpimentel02 in [#598](https://github.com/brazilian-utils/python/pull/598)

### New Contributors
* @MatheusPaivaa made their first contribution in [#653](https://github.com/brazilian-utils/python/pull/653)
* @Fontebasso-JV made their first contribution in [#652](https://github.com/brazilian-utils/python/pull/652)
* @felipecolen made their first contribution in [#638](https://github.com/brazilian-utils/python/pull/638)
* @willkraemer made their first contribution in [#651](https://github.com/brazilian-utils/python/pull/651)
* @rochamrcs made their first contribution in [#650](https://github.com/brazilian-utils/python/pull/650)
* @lucasjl made their first contribution in [#646](https://github.com/brazilian-utils/python/pull/646)
* @ronaldofas made their first contribution in [#643](https://github.com/brazilian-utils/python/pull/643)
* @camilotmundim made their first contribution in [#637](https://github.com/brazilian-utils/python/pull/637)
* @luizweb made their first contribution in [#645](https://github.com/brazilian-utils/python/pull/645)
* @guyrux made their first contribution in [#640](https://github.com/brazilian-utils/python/pull/640)

## [2.3.0] - 2025-10-07

### Added
- Remove deprecated python versions by @niltonpimentel02 in [#561](https://github.com/brazilian-utils/python/pull/561)
- Add convert_uf_to_name by @niltonpimentel02 in [#554](https://github.com/brazilian-utils/python/pull/554)
- Add validate-pr-title-v1.yml by @niltonpimentel02 in [#553](https://github.com/brazilian-utils/python/pull/553)
- Conversão de Moeda Real para Texto by @dinalivia in [#525](https://github.com/brazilian-utils/python/pull/525)
- Adicionar automação para gerenciar PRs inativos com GitHub Actions by @tiagornandrade in [#479](https://github.com/brazilian-utils/python/pull/479)
- Retorna codigo do ibge do nome do municipio e da uf by @CarduCaldeira in [#411](https://github.com/brazilian-utils/python/pull/411)

### Changed
- Busca de municípios by @camilamaia in [#595](https://github.com/brazilian-utils/python/pull/595)
- Improve functions format_currency, convert_real_to_text and tests by @niltonpimentel02 in [#577](https://github.com/brazilian-utils/python/pull/577)
- Unifica date e date-utils by @camilamaia in [#576](https://github.com/brazilian-utils/python/pull/576)
- Módulo uf.py by @camilamaia in [#575](https://github.com/brazilian-utils/python/pull/575)
- Add new contact method by @niltonpimentel02 in [#570](https://github.com/brazilian-utils/python/pull/570)
- Update convert_date_to_text to return None when invalid input by @niltonpimentel02 in [#569](https://github.com/brazilian-utils/python/pull/569)
- Padroniza changelog by @camilamaia in [#560](https://github.com/brazilian-utils/python/pull/560)
- Arruma a ordem dos utilitários do IBGE by @camilamaia in [#557](https://github.com/brazilian-utils/python/pull/557)
- Adicionando MAINTAINING.md by @camilamaia in [#427](https://github.com/brazilian-utils/python/pull/427)

### New Contributors
* @niltonpimentel02 made their first contribution in [#596](https://github.com/brazilian-utils/python/pull/596)
* @renata-machado made their first contribution in [#500](https://github.com/brazilian-utils/python/pull/500)
* @gabriel-lima258 made their first contribution in [#532](https://github.com/brazilian-utils/python/pull/532)
* @laistdomiciano made their first contribution in [#530](https://github.com/brazilian-utils/python/pull/530)
* @Joaolpridolficarvalho made their first contribution in [#516](https://github.com/brazilian-utils/python/pull/516)
* @dinalivia made their first contribution in [#525](https://github.com/brazilian-utils/python/pull/525)
* @tiagornandrade made their first contribution in [#489](https://github.com/brazilian-utils/python/pull/489)
* @devid8642 made their first contribution in [#491](https://github.com/brazilian-utils/python/pull/491)
* @jaimenunes made their first contribution in [#480](https://github.com/brazilian-utils/python/pull/480)
* @alphabraga made their first contribution in [#442](https://github.com/brazilian-utils/python/pull/442)
* @morais90 made their first contribution in [#434](https://github.com/brazilian-utils/python/pull/434)
* @vianaz made their first contribution in [#455](https://github.com/brazilian-utils/python/pull/455)
* @FloraSauerbronn made their first contribution in [#439](https://github.com/brazilian-utils/python/pull/439)
* @CarduCaldeira made their first contribution in [#411](https://github.com/brazilian-utils/python/pull/411)
* @BeneBr made their first contribution in [#415](https://github.com/brazilian-utils/python/pull/415)
* @carlos-moreno made their first contribution
* @melissawm made their first contribution in [#409](https://github.com/brazilian-utils/python/pull/409)

## [2.2.0] - 2024-09-12

### New Contributors
* @gtkacz made their first contribution in [#376](https://github.com/brazilian-utils/python/pull/376)

## [2.1.1] - 2024-01-06

## [2.1.0] - 2024-01-05

### Added
- Gerar número de telefone fixo aleatório by @MarcelFox in [#249](https://github.com/brazilian-utils/python/pull/249)
- Suporte ao python 3.12 by @camilamaia in [#245](https://github.com/brazilian-utils/python/pull/245)
- Adiciona `format_pis` #206 by @patricia-salles in [#224](https://github.com/brazilian-utils/python/pull/224)
- Adiciona `get_license_plate_format` by @kaioduarte in [#243](https://github.com/brazilian-utils/python/pull/243)
- Add is_valid_license_plate by @kaioduarte in [#240](https://github.com/brazilian-utils/python/pull/240)
- Remover Símbolos do PIS by @kaioduarte in [#239](https://github.com/brazilian-utils/python/pull/239)
- Add generate_pis by @kaioduarte in [#218](https://github.com/brazilian-utils/python/pull/218)
- Add is_valid_pis by @kaioduarte in [#216](https://github.com/brazilian-utils/python/pull/216)
- Validate license plate by @hebertn88 in [#214](https://github.com/brazilian-utils/python/pull/214)
- Add is_email_valid by @Anurag-Nagpal in [#213](https://github.com/brazilian-utils/python/pull/213)

### Changed
- Refactor no utilitário de validar título eleitoral by @camilamaia in [#296](https://github.com/brazilian-utils/python/pull/296)

### Feature
- Titulo eleitoral by @VPeron in [#235](https://github.com/brazilian-utils/python/pull/235)
- Gerar um numero de celular aleatório #191 by @jhonatacaiob in [#232](https://github.com/brazilian-utils/python/pull/232)
- Formatando numero de telefone #189 by @jhonatacaiob in [#231](https://github.com/brazilian-utils/python/pull/231)
- Validação de telefone by @antoniamaia in [#150](https://github.com/brazilian-utils/python/pull/150)

### Refactor
- Using regex to enhance phone validation by @antoniamaia in [#154](https://github.com/brazilian-utils/python/pull/154)
- Incluindo `Test` no nome das Classes by @antoniamaia in [#149](https://github.com/brazilian-utils/python/pull/149)
- Alterando os métodos de `assert` python para unittest by @antoniamaia in [#148](https://github.com/brazilian-utils/python/pull/148)

### Doc
- Arrumando license_plate para ter apenas um método is_valid by @camilamaia in [#294](https://github.com/brazilian-utils/python/pull/294)

### New Contributors
* @MarcelFox made their first contribution in [#291](https://github.com/brazilian-utils/python/pull/291)
* @joseevilasio made their first contribution in [#276](https://github.com/brazilian-utils/python/pull/276)
* @cuducos made their first contribution in [#273](https://github.com/brazilian-utils/python/pull/273)
* @VPeron made their first contribution in [#235](https://github.com/brazilian-utils/python/pull/235)
* @magnunleno made their first contribution in [#241](https://github.com/brazilian-utils/python/pull/241)
* @patricia-salles made their first contribution in [#224](https://github.com/brazilian-utils/python/pull/224)
* @jhonatacaiob made their first contribution in [#232](https://github.com/brazilian-utils/python/pull/232)
* @kaioduarte made their first contribution in [#243](https://github.com/brazilian-utils/python/pull/243)
* @pontes-guilherme made their first contribution in [#223](https://github.com/brazilian-utils/python/pull/223)
* @hebertn88 made their first contribution in [#214](https://github.com/brazilian-utils/python/pull/214)
* @Anurag-Nagpal made their first contribution in [#213](https://github.com/brazilian-utils/python/pull/213)
* @giovannism20 made their first contribution in [#188](https://github.com/brazilian-utils/python/pull/188)

## [2.0.0] - 2023-07-23

### Added
- Add parse cnpj method by @antoniamaia in [#58](https://github.com/brazilian-utils/python/pull/58)
- Add parse_cpf by @camilamaia in [#57](https://github.com/brazilian-utils/python/pull/57)
- Is_valid_cnpj by @antoniamaia in [#36](https://github.com/brazilian-utils/python/pull/36)
- Is_valid_cpf by @camilamaia in [#34](https://github.com/brazilian-utils/python/pull/34)

### Changed
- Create a folder with old documentation by @antoniamaia in [#71](https://github.com/brazilian-utils/python/pull/71)
- English readme by @camilamaia in [#60](https://github.com/brazilian-utils/python/pull/60)
- Improve imports usability for cnpj by @antoniamaia in [#48](https://github.com/brazilian-utils/python/pull/48)
- Improve imports usability for cpf by @camilamaia in [#47](https://github.com/brazilian-utils/python/pull/47)
- Add CONTRIBUTING.md by @camilamaia in [#28](https://github.com/brazilian-utils/python/pull/28)
- Change the default readme to the english one by @camilamaia
- Add black by @camilamaia in [#22](https://github.com/brazilian-utils/python/pull/22)
- Add FUNDING.yml by @camilamaia

### Feature
- Implementando a função `remove_symbols_cep` by @antoniamaia in [#126](https://github.com/brazilian-utils/python/pull/126)
- Implementando o método `format_cep` by @antoniamaia in [#125](https://github.com/brazilian-utils/python/pull/125)
- `generate_cep` by @antoniamaia in [#124](https://github.com/brazilian-utils/python/pull/124)
- Validação CEP by @antoniamaia in [#123](https://github.com/brazilian-utils/python/pull/123)

### Fixed
- Make install by @antoniamaia in [#32](https://github.com/brazilian-utils/python/pull/32)
- Fixed statistically negligible bug in generators by @luizberti

### Packaging
- Remove python 2 from classifiers by @camilamaia

### New Contributors
* @camilamaia made their first contribution in [#128](https://github.com/brazilian-utils/python/pull/128)
* @antoniamaia made their first contribution in [#126](https://github.com/brazilian-utils/python/pull/126)
* @dependabot[bot] made their first contribution in [#103](https://github.com/brazilian-utils/python/pull/103)
* @luizberti made their first contribution

[unreleased]: https://github.com/brazilian-utils/python/compare/v2.3.0...HEAD
[2.3.0]: https://github.com/brazilian-utils/python/compare/v2.2.0...v2.3.0
[2.2.0]: https://github.com/brazilian-utils/python/compare/v2.1.1...v2.2.0
[2.1.1]: https://github.com/brazilian-utils/python/compare/v2.1.0...v2.1.1
[2.1.0]: https://github.com/brazilian-utils/python/compare/v2.0.0...v2.1.0

<!-- generated by git-cliff -->

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Utilitário `convert_name_to_uf`

## [2.3.0] - 2025-10-07

### Added

- Utilitário `convert_code_to_uf` [#410](https://github.com/brazilian-utils/brutils-python/pull/410)
- Utilitário `is_holiday` [#446](https://github.com/brazilian-utils/brutils-python/pull/446)
- Utilitário `convert_date_to_text`[#415](https://github.com/brazilian-utils/brutils-python/pull/415)
- Utilitário `get_municipality_by_code` [412](https://github.com/brazilian-utils/brutils-python/pull/412)
- Utilitário `get_code_by_municipality_name` [#411](https://github.com/brazilian-utils/brutils-python/pull/411)
- Utilitário `format_currency` [#434](https://github.com/brazilian-utils/brutils-python/pull/434)
- Utilitário `convert_real_to_text` [#525](https://github.com/brazilian-utils/brutils-python/pull/525)
- Utilitário `convert_uf_to_name` [#554](https://github.com/brazilian-utils/brutils-python/pull/554)

### Deprecated

- **BREAKING CHANGES** Suporte ao Python 3.8 [#236](https://github.com/brazilian-utils/brutils-python/pull/561)
- **BREAKING CHANGES** Suporte ao Python 3.9 [#236](https://github.com/brazilian-utils/brutils-python/pull/561)

## [2.2.0] - 2024-09-12

### Added

- Utilitário `get_address_from_cep` [#358](https://github.com/brazilian-utils/brutils-python/pull/358)
- Utilitário `get_cep_information_from_address` [#358](https://github.com/brazilian-utils/brutils-python/pull/358)
- Utilitário `format_voter_id` [#363](https://github.com/brazilian-utils/brutils-python/pull/363)
- Utilitário `generate_voter_id` [#220](https://github.com/brazilian-utils/brutils-python/pull/220)

## [2.1.1] - 2024-01-06

### Fixed

- `generate_legal_process` [#325](https://github.com/brazilian-utils/brutils-python/pull/325)
- `is_valid_legal_process` [#325](https://github.com/brazilian-utils/brutils-python/pull/325)
- Import do utilitário `convert_license_plate_to_mercosul` [#324](https://github.com/brazilian-utils/brutils-python/pull/324)
- Import do utilitário `generate_license_plate` [#324](https://github.com/brazilian-utils/brutils-python/pull/324)
- Import do utilitário `get_format_license_plate` [#324](https://github.com/brazilian-utils/brutils-python/pull/324)

## [2.1.0] - 2024-01-05

### Added

- Suporte ao Python 3.12 [#245](https://github.com/brazilian-utils/brutils-python/pull/245)
- Utilitário `convert_license_plate_to_mercosul` [#226](https://github.com/brazilian-utils/brutils-python/pull/226)
- Utilitário `format_license_plate` [#230](https://github.com/brazilian-utils/brutils-python/pull/230)
- Utilitário `format_phone` [#231](https://github.com/brazilian-utils/brutils-python/pull/231)
- Utilitário `format_pis` [#224](https://github.com/brazilian-utils/brutils-python/pull/224)
- Utilitário `format_legal_process` [#210](https://github.com/brazilian-utils/brutils-python/pull/210)
- Utilitário `generate_license_plate` [#241](https://github.com/brazilian-utils/brutils-python/pull/241)
- Utilitário `generate_phone` [#295](https://github.com/brazilian-utils/brutils-python/pull/295)
- Utilitário `generate_pis` [#218](https://github.com/brazilian-utils/brutils-python/pull/218)
- Utilitário `generate_legal_process` [#208](https://github.com/brazilian-utils/brutils-python/pull/208)
- Utilitário `get_format_license_plate` [#243](https://github.com/brazilian-utils/brutils-python/pull/243)
- Utilitário `is_valid_email` [#213](https://github.com/brazilian-utils/brutils-python/pull/213)
- Utilitário `is_valid_license_plate` [#237](https://github.com/brazilian-utils/brutils-python/pull/237)
- Utilitário `is_valid_phone` [#147](https://github.com/brazilian-utils/brutils-python/pull/147)
- Utilitário `is_valid_pis` [#216](https://github.com/brazilian-utils/brutils-python/pull/216)
- Utilitário `is_valid_legal_process` [#207](https://github.com/brazilian-utils/brutils-python/pull/207)
- Utilitário `is_valid_voter_id` [#235](https://github.com/brazilian-utils/brutils-python/pull/235)
- Utilitário `remove_international_dialing_code` [192](https://github.com/brazilian-utils/brutils-python/pull/192)
- Utilitário `remove_symbols_license_plate` [#182](https://github.com/brazilian-utils/brutils-python/pull/182)
- Utilitário `remove_symbols_phone` [#188](https://github.com/brazilian-utils/brutils-python/pull/188)
- Utilitário `remove_symbols_pis` [#236](https://github.com/brazilian-utils/brutils-python/pull/236)
- Utilitário `remove_symbols_legal_process` [#209](https://github.com/brazilian-utils/brutils-python/pull/209)

### Removed

- **BREAKING CHANGE** Suporte ao Python 3.7 [#236](https://github.com/brazilian-utils/brutils-python/pull/236)

## [2.0.0] - 2023-07-23

### Added

- Utilitário `is_valid_cep` [123](https://github.com/brazilian-utils/brutils-python/pull/123)
- Utilitário `format_cep` [125](https://github.com/brazilian-utils/brutils-python/pull/125)
- Utilitário `remove_symbols_cep` [126](https://github.com/brazilian-utils/brutils-python/pull/126)
- Utilitário `generate_cep` [124](https://github.com/brazilian-utils/brutils-python/pull/124)
- Utilitário `is_valid_cpf` [34](https://github.com/brazilian-utils/brutils-python/pull/34)
- Utilitário `format_cpf` [54](https://github.com/brazilian-utils/brutils-python/pull/54)
- Utilitário `remove_symbols_cpf` [57](https://github.com/brazilian-utils/brutils-python/pull/57)
- Utilitário `is_valid_cnpj` [36](https://github.com/brazilian-utils/brutils-python/pull/36)
- Utilitário `format_cnpj` [52](https://github.com/brazilian-utils/brutils-python/pull/52)
- Utilitário `remove_symbols_cnpj` [58](https://github.com/brazilian-utils/brutils-python/pull/58)

### Deprecated

- Utilitário `cpf.sieve`
- Utilitário `cpf.display`
- Utilitário `cpf.validate`
- Utilitário `cnpj.sieve`
- Utilitário `cnpj.display`
- Utilitário `cnpj.validate`

[Unreleased]: https://github.com/brazilian-utils/brutils-python/compare/v2.3.0...HEAD
[2.3.0]: https://github.com/brazilian-utils/brutils-python/releases/tag/v2.3.0
[2.2.0]: https://github.com/brazilian-utils/brutils-python/releases/tag/v2.2.0
[2.1.1]: https://github.com/brazilian-utils/brutils-python/releases/tag/v2.1.1
[2.1.0]: https://github.com/brazilian-utils/brutils-python/releases/tag/v2.1.0
[2.0.0]: https://github.com/brazilian-utils/brutils-python/releases/tag/v2.0.0

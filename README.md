[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

# Deprecated

This repository is no longer supported, please consider using
[brutils-python][brutils-python] instead.

<div align="center">
<h1>🇧🇷 Brazilian Utils</h1>

<p>Utils library for Brazilian-specific businesses.</p>
</div>

# Getting Started

Brazilian Utils is a library focused on solving problems that we face daily in the development of applications for the Brazilian business.

## Installation

Using **Brazilian Utils** is quite simple and you can install it using [pip][pip-installation]:

```bash
pip install brazilian-utils
```

## Usage

To use one of our utilities you just need to import the required function as in the example below:

```python
from brazilian_utils import is_valid_cpf

is_valid_cpf("1232454233345") # False
```

You can check the list containing all utilities [here][utilities].

[brutils-python]: https://github.com/brazilian-utils/brutils-python
[pip-installation]: https://pip.pypa.io/en/stable/installing/
[utilities]: https://github.com/brazilian-utils/python/blob/master/brazilian_utils/__init__.py

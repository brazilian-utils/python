# Contribuindo

Obrigado por dedicar o seu tempo para contribuir! 🙇‍♀️🙇‍♂️ Toda ajuda é bem-vinda!

- [Primeira Contribuição](#primeira-contribuição)
- [Lançar uma Nova Versão](#lançar-uma-nova-versão)

## 💌 Quer contribuir, mas não se sente à vontade?

Você tem vontade de contribuir, mas não se sente à vontade em abrir issues, PRs ou fazer perguntas publicamente?

Nós sabemos como pode ser difícil dar o primeiro passo em um espaço aberto. A insegurança, o medo de errar ou até a sensação de “será que minha dúvida é boba?” podem pesar bastante. E tá tudo bem sentir isso. 💜

Queremos que você saiba que aqui ninguém precisa enfrentar esse caminho sem apoio. Se preferir um espaço mais reservado, você pode mandar um e-mail para cumbucadev@gmail.com e teremos o maior prazer em ajudar. Seja para tirar dúvidas, pedir orientação ou simplesmente ter alguém para conversar sobre como começar.

O importante é que você saiba: sua participação é muito bem-vinda, e cada contribuição, por menor que pareça, faz uma grande diferença. ✨

## Primeira Contribuição

Como fazer a sua primeira contribuição:

- [1. Crie uma Conta no GitHub](#1-crie-uma-conta-no-github)
- [2. Encontre uma Issue para Trabalhar](#2-encontre-uma-issue-para-trabalhar)
- [3. Instale o Git](#3-instale-o-git)
- [4. Faça um Fork do Projeto](#4-faça-um-fork-do-projeto)
- [5. Clone o Seu Fork](#5-clone-o-seu-fork)
- [6. Crie um Novo Branch](#6-crie-um-novo-branch)
- [7. Execute o brutils Localmente](#7-execute-o-brutils-localmente)
- [8. Faça as Suas Alterações](#8-faça-as-suas-alterações)
- [9. Teste as Suas Alterações](#9-teste-as-suas-alterações)
- [10. Atualizar READMEs](#10-atualizar-readmes)
- [11. Faça o Commit e Envie as Suas Alterações](#11-faça-o-commit-e-envie-as-suas-alterações)
- [12. Adicione Entradas no CHANGELOG.md](#12-adicione-entradas-no-changelogmd)
- [13. Crie um PR no GitHub](#13-crie-um-pr-no-github)
- [14. Atualizar a Sua Branch se Necessário](#14-atualizar-a-sua-branch-se-necessário)

### 1. Crie uma Conta no GitHub

Certifique-se de ter uma [conta no GitHub][github-join] e de estar com a sessão iniciada.

Caso não tenha uma conta, siga os passos de [como criar de uma conta pessoal no GitHub][github-essentials-criar-conta].

### 2. Encontre uma Issue para Trabalhar

Visite a [página de issues do brutils][brutils-issues] e encontre uma issue com a qual você gostaria
de trabalhar e que ainda não tenha sido atribuída a ninguém.

Deixe um comentário na issue com conteúdo "bora!" Em seguida, um bot vai atribuir a issue a você. Uma vez atribuída, você pode prosseguir para a próxima etapa.

Sinta-se à vontade para fazer qualquer pergunta na página da issue antes ou durante o processo de
desenvolvimento.

Ao começar a contribuir para o projeto, é recomendável que você pegue uma issue por vez. Isso ajuda a garantir que outras pessoas também tenham a oportunidade de colaborar e evita que recursos fiquem inativos por muito tempo.

### 3. Instale o Git

Certifique-se de ter o git instalado, seguindo os passos do [tutorial de instalação do git][github-essentials-instalando-o-git].

### 4. Faça um Fork do Projeto

[Faça um fork do repositório brutils][github-forking].

### 5. Clone o Seu Fork

[Clone][github-cloning] o seu fork localmente.

### 6. Crie um Novo Branch

Entre na pasta do brutils:

```bash
$ cd brutils-python
>
```

E crie uma nova branch com o nome da issue em que você irá trabalhar através do comando:

```bash
$ git checkout -b <issue_number>
>
```

Exemplo:

```bash
$ git checkout -b 386
Switched to a new branch '386'
>
```

### 7. Execute o brutils Localmente

#### Instalação com poetry

##### Requisitos

- [Python 3.10+][python]
- [Poetry][poetry]

Crie um [virtualenv][virtualenv] para o brutils e o ative através do comando:

```shell
$ make shell
Spawning shell within ...-py3.x
emulate bash -c '. .../bin/activate'
```

Para testar se o ambiente virtual está ativo corretamente, execute o comando e verifique se a resposta é algo parecido com a seguinte:

```sh
$ poetry env info
Virtualenv
Python:         3.x.y
Implementation: CPython
...
```

**Observação: Você precisa executar `make shell` toda vez que abrir uma nova janela ou aba do terminal.**

Instale as dependências:

```shell
$ make install
git config --local core.hooksPath .githooks/
chmod -R +x .githooks
Installing dependencies from lock file
...
```

#### Instalação com pip

Se preferir usar pip, você pode instalar o projeto em modo de desenvolvimento da seguinte forma:

##### Requisitos

- [Python 3.10+][python]
- [pip][pip]

Crie um [virtualenv][virtualenv] para o brutils e o ative através do comando:

```sh
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
```

Utilize o comando pip para instalar as dependencias de dev e testes através do arquivo requirements-dev.txt

```sh
pip install -r requirements-dev.txt
```

#### Utilizando Localmente

Agora você pode usá-lo [da mesma forma descrita no arquivo README.md](/README.md#utilização).

## Testes 

Execute os testes através do seguinte comando:

```shell
$ make test
make test
test__is_valid_mercosul (license_plate.test_is_valid.TestIsValidMercosul.test__is_valid_mercosul) ... ok
test__is_valid_old_format (license_plate.test_is_valid.TestIsValidOldFormat.test__is_valid_old_format) ... ok
....

----------------------------------------------------------------------
Ran XX tests in 0.000s

OK
```

Certifique-se de que o retorno é `OK`, o quê indica todos os testes estão passando e que não tem nenhum falhando.

---

## Testes no Windows

Caso os testes não funcionem ou se você precisar configurar o ambiente do zero, siga as etapas abaixo para preparar o ambiente no Windows.

### Instalar o Chocolatey

Primeiro, abra o PowerShell como administrador e execute o seguinte comando para instalar o **Chocolatey**, que é um gerenciador de pacotes para o Windows:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

### Instalar o `make`

Após a instalação do Chocolatey, instale o **make** com o seguinte comando:

```powershell
choco install make
```

Verifique se o `make` foi instalado corretamente com:

```powershell
where.exe make
```

### Instalar o Poetry

Instale o **Poetry**, que é uma ferramenta de gerenciamento de dependências e ambientes Python, usando o comando:

```powershell
choco install poetry
```

### Instalar as dependências do projeto

Dentro do diretório do seu projeto, abra o terminal e instale as dependências do projeto usando o **Poetry**:

```powershell
poetry install
```

### Verificar e configurar o `Makefile`

No arquivo `Makefile` do seu projeto, verifique se a seção de testes está configurada corretamente. Se estiver no Windows, use a seguinte configuração para o alvo `test`:

```makefile
test:
ifeq ($(OS),Windows_NT)
	@set PYTHONDONTWRITEBYTECODE=1 && poetry run python -m unittest discover tests/ -v
else
	@PYTHONDONTWRITEBYTECODE=1 poetry run python3 -m unittest discover tests/ -v
endif
```



### 8. Faça as Suas Alterações

Agora é a etapa em que você pode implementar as suas alterações no código.

Normalmente existem instruções/ideias de como você pode implementar a solução diretamente na descrição da issue, na seção "Descreva alternativas que você considerou". Leia atentamente tudo que está escrito na issue para garantir que
suas modificações resolvem tudo que está sendo solicitado.

É importante notar que documentamos o nosso código usando [docstrings][docstring-definition].
Módulos, classes, funções e métodos devem ser documentados. Suas alterações também devem ser bem
documentadas e refletir docstrings atualizadas, caso algum dos parâmetros tenha sido alterado para
um classe/atributo ou mesmo funções.

Todas as docstring devem estar em Inglês. Fique à vontade para utilizar ferramentas como Google Tradutor ou ChatGPT caso precise. Iremos sugerir mudanças na tradução se necessário, então não se preocupe com possíveis erros de inglês.

Seguimos o padrão abaixo para manter consistência nas docstrings:

```python
class Example:
    """
    Explain the purpose of the class

    Attributes:
        x[dict]: Short explanation here
        y[type, optional]: Short explanation here
    """

    def __init__(self, x, y=None):
        self.x = x
        self.y = y

    def foobar(self, w):
        """
        Purpose of the function

        Args:
            name[type]: Short explanation here

        Returns:
            type: Short explanation here

        Example:
            >>> command 1
            output 1
            >>> command 2
            output 2
        """
        ...
        return value
```

Exemplo:

```python
def format_cep(cep):  # type: (str) -> str | None
    """
    Formats a Brazilian CEP (Postal Code) into a standard format.

    This function takes a CEP (Postal Code) as input and, if it is a valid
    8-digit CEP, formats it into the standard "12345-678" format.

    Args:
        cep (str): The input CEP (Postal Code) to be formatted.

    Returns:
        str: The formatted CEP in the "12345-678" format if it's valid,
             None if it's not valid.

    Example:
        >>> format_cep("12345678")
        "12345-678"
        >>> format_cep("12345")
        None
    """

    return f"{cep[:5]}-{cep[5:8]}" if is_valid(cep) else None
```

Algo a se ter em mente ao documentar o código com docstrings é que você pode ignorar docstrings em
decoradores de propriedade e métodos mágicos.

### 9. Teste as Suas Alterações

#### Escreva Novos Testes

Certifique-se de ter criado os testes necessários para cada nova alteração que você fez.

#### Certifique-se de que Todos os Testes Passam

Execute todos os testes com o comando `make test` e certifique-se de que todos passam.

**Os PRs não serão mesclados se houver algum teste faltando ou falhando.**

#### Teste manualmente

Abra um ambiente interativo para testar manualmente as suas mudanças:

```sh
$ python
Python 3.x.y ...
Type "help", "copyright", "credits" or "license" for more information.
>>> # Teste as suas mudanças aqui!
```

Exemplo:

```sh
$ python
Python 3.12.5 (main, Aug  6 2024, 19:08:49) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import brutils
>>> from brutils import cpf
>>> cpf.generate()
'13403202232'
>>> from brutils import generate_cpf
>>> generate_cpf()
'64590379228'
```

### 10. Atualizar READMEs

Atualize os arquivos `brutils-python/README.md` e `brutils-python/README_EN.md` com suas alterações.

Esses arquivos são essenciais para a documentação da biblioteca, ajudando os usuários a entender como utilizar os recursos oferecidos. Portanto, é importante mantê-los sempre atualizados.

- O arquivo brutils-python/README_EN.md contém a documentação em Inglês, e pode usar o conteúdo já descrito na docstring diretamente.
- O arquivo brutils-python/README.md contém a documentação em Português. Para este, basta traduzir a docstring da função.

Se precisar de assistência na tradução para o Português, ferramentas como Google Tradutor ou ChatGPT podem ajudar. Não se preocupe com possíveis erros de tradução, pois sugeriremos ajustes quando necessário.

Exemplo em Inglês (README_EN.md):

````md
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
````

Exemplo em Português (README.md):

````md
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
````

### 11. Faça o Commit e Envie as Suas Alterações

Fomarte o seu código executando o comando:

```bash
$ make format
...
```

Exemplo:

```bash
$ make format
31 files left unchanged
All checks passed!
```

Adicione suas mudanças para staging area:

```bash
$ git add --all
...
```

Faça o commit das alterações:

```bash
$ git commit -a -m "<commit_message>"
...
```

Exemplo:

```bash
$ git commit -m 'Adicionando mais info aos arquivos de contribuição'
[386 173b7e6] Adicionando mais info aos arquivos de contribuição
 2 files changed, 144 insertions(+), 34 deletions(-)
```

Push o seu commit para o GitHub:

```bash
$ git push --set-upstream origin <issue_number>
...
```

Exemplo:

```bash
$ git push --set-upstream origin 386
Running pre-push hook checks
All checks passed!
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 10 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 2.36 KiB | 2.36 MiB/s, done.
Total 4 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
remote:
remote: Create a pull request for '386' on GitHub by visiting:
remote:      https://github.com/brazilian-utils/brutils-python/pull/new/386
remote:
To github.com:brazilian-utils/brutils-python.git
 * [new branch]      386 -> 386
```

Faça as alterações e commits necessários e envie-os quando estiverem prontos.

### 12. Adicione Entradas no CHANGELOG.md

#### O que é um changelog?

Um changelog é um arquivo que contém uma lista organizada cronologicamente de mudanças notáveis para cada versão de um projeto.

#### Por que manter um changelog?

Para facilitar para usuários e contribuintes verem exatamente quais mudanças notáveis foram feitas entre cada release (ou versão) do projeto.

#### Quem precisa de um changelog?

Pessoas. Sejam consumidores ou desenvolvedores, os usuários finais de software são seres humanos que se importam com o que está no software. Quando o software muda, as pessoas querem saber por que e como.

#### Onde está o changelog do brutils?

O changelog do brutils está disponível em [CHANGELOG.md][changelog]

#### Princípios orientadores

- Changelogs são para humanos, não máquinas.
- Deve haver uma entrada para cada versão.
- Os mesmos tipos de mudanças devem ser agrupados.
- Versões e seções devem ser linkáveis.
- A versão mais recente vem primeiro.
- A data de lançamento de cada versão é exibida.

#### O que justifica uma entrada no changelog?

- Correções de segurança: Devem ser documentadas com o tipo definido como "segurança" para alertar os usuários sobre questões de segurança resolvidas.
Exemplo: “Corrigido um vulnerabilidade crítica que permitia a execução remota de código.”

- Mudanças voltadas ao usuário: Alterações que afetam diretamente a forma como os usuários interagem com o software, incluindo novas funcionalidades, alterações em funcionalidades existentes ou melhorias na interface.
Exemplo: “Adicionada uma nova opção de filtro na página de resultados para facilitar a busca.”

- Melhorias significativas de desempenho: Devem ser registradas quando resultam em melhorias notáveis na velocidade ou na eficiência do software que impactam a experiência do usuário.
Exemplo: “O tempo de carregamento da página inicial foi reduzido em 40% após a otimização do backend.”

- Alterações que afetam a compatibilidade: Mudanças que ajustam o software para manter a compatibilidade com outras ferramentas, sistemas ou versões.
Exemplo: “Atualizada a biblioteca X para a versão 2.0 para suportar a nova versão do Python.”

- Mudanças na API pública:
Alterações que afetam como os desenvolvedores interagem com a API pública do software, seja adicionando novas rotas ou alterando as existentes.
Exemplo: “Adicionada uma nova rota /api/v1/users para gerenciamento de usuários.”

- Alterações nas dependências: Atualizações ou mudanças nas dependências do projeto que podem afetar o comportamento ou a compatibilidade do software.
Exemplo: “Atualizado o pacote de dependência Y para a versão 3.1.4, que inclui correções importantes de segurança.”

#### O quê NÃO deve ir no changelog

Embora o changelog seja uma ferramenta valiosa para documentar mudanças, algumas informações não devem ser incluídas. Aqui estão alguns exemplos do que não deve aparecer no changelog:

- Mudanças Internas de Código: Alterações que não afetam o comportamento do usuário final, como refatorações de código interno que não alteram a funcionalidade, não precisam ser documentadas no changelog. Exemplo: “Refatoração de funções internas” ou “Correção testes inconsistentes.”

- Melhorias de Desempenho Não Notáveis: Melhorias de desempenho que não resultam em mudanças perceptíveis ou benefícios claros para o usuário final não precisam de uma entrada específica. Exemplo: “Otimização de algoritmos internos.”

- Correções de Bugs Menores: Correções para bugs que não afetam o uso geral ou a experiência do usuário final podem ser omitidas. Exemplo: “Correção de um pequeno erro de digitação no código.”

- Mudanças Somente de Documentação: Alterações que afetam apenas a documentação, sem modificar o comportamento do software, geralmente não precisam ser incluídas no changelog. Exemplo: “Atualização do README.md para refletir novas dependências.”

- Detalhes Técnicos Excessivos: Informações excessivamente técnicas que não são relevantes para o usuário final ou não oferecem contexto sobre o impacto da mudança devem ser evitadas. Exemplo: “Mudança no gerenciamento de memória na classe X.”

- Entradas de Mantenedor: Mudanças que são relacionadas apenas ao processo de desenvolvimento ou manutenção interna, como ajustes de configuração de ferramentas de CI/CD, geralmente não são relevantes para o changelog. Exemplo: “Atualização na configuração do GitHub Actions.”

- Uma correção de bug introduzida e corrigida na mesma release não precisa de uma entrada no changelog.

Evite incluir essas informações no changelog para manter o documento focado e útil para os usuários e contribuintes do projeto.

#### Escrevendo boas entradas no changelog

Uma boa entrada no changelog deve ser descritiva e concisa. Deve explicar a mudança a um leitor que não tem nenhum contexto sobre a mudança. Se for difícil ser ao mesmo tempo conciso e descritivo, opte por ser mais descritivo.

- **Ruim**: Ir para a ordem do projeto.
- **Bom**: Mostrar os projetos estrelados do usuário no topo do dropdown “Ir para o projeto”.

O primeiro exemplo não dá contexto sobre onde a mudança foi feita, nem por que, nem como beneficia o usuário.

- **Ruim**: Copiar (algum texto) para a área de transferência.
- **Bom**: Atualizar o tooltip de “Copiar para a área de transferência” para indicar o que está sendo copiado.

Novamente, o primeiro exemplo é muito vago e não fornece contexto.

- **Ruim**: Corrige e melhora problemas de CSS e HTML no gráfico de mini pipeline e dropdown de builds.
- **Bom**: Corrigir tooltips e estados de hover no gráfico de mini pipeline e dropdown de builds.

O primeiro exemplo está muito focado nos detalhes de implementação. O usuário não se importa que mudamos CSS e HTML, ele se importa com o resultado final dessas mudanças.

- **Ruim**: Remover valores nulos no Array de objetos Commit retornados por find_commits_by_message_with_elastic
- **Bom**: Corrigir erros 500 causados por resultados do Elasticsearch referenciando commits já recolhidos pelo garbage collector.

O primeiro exemplo foca em como corrigimos algo, não no que foi corrigido. A versão reescrita descreve claramente o benefício final para o usuário (menos erros 500) e quando isso acontece (ao buscar commits com Elasticsearch).

Use seu melhor julgamento e tente se colocar na posição de alguém lendo o changelog compilado. Essa entrada agrega valor? Oferece contexto sobre onde e por que a mudança foi feita?

### Como adicionar uma entrada no changelog

O changelog está disponível no arquivo [CHANGELOG.md][changelog].

Primeiro, você precisa identificar o tipo da sua mudança. Tipos de mudanças:

- `Added` para novas funcionalidades.
- `Changed` para mudanças em funcionalidades existentes.
- `Deprecated` para funcionalidades que serão removidas em breve.
- `Fixed` para qualquer correção de bugs.
- `Removed` para funcionalidades que foram removidas.
- `Security` em caso de vulnerabilidades.

Você deve sempre adicionar novas entradas no changelog na seção `Unreleased`. No momento do release, moveremos as mudanças da seção `Unreleased` para uma nova seção de versão.

Portanto, dentro da seção `Unreleased`, você deve adicionar sua entrada na seção apropriada por tipo. Se ainda não houver uma seção para o tipo da sua mudança, você deve adicioná-la.

Vamos ver alguns exemplos. Suponhamos que você tenha uma nova mudança `Fixed` para adicionar, e o arquivo atual do CHANGELOG.md está assim:

```md
## [Unreleased]
### Added
- Utilitário `get_address_from_cep` [#358](https://github.com/brazilian-utils/brutils-python/pull/358)

### Changed
- Utilitário `fmt_voter_id` renomeado  para `format_voter_id` [#221](https://github.com/brazilian-utils/brutils-python/issues/221)
```

Você precisará adicionar uma nova seção `Fixed` e incluir a nova entrada lá:

```md
## [Unreleased]
### Added
- Utilitário `get_address_from_cep` [#358](https://github.com/brazilian-utils/brutils-python/pull/358)

### Changed
- Utilitário `fmt_voter_id` renomeado  para `format_voter_id` [#221](https://github.com/brazilian-utils/brutils-python/issues/221)

### Fixed
- Minha mensagem de changelog aqui. [#<número_da_issue>](<link_da_issue>)
```

Note que a ordem das seções por tipo importa. Temos um lint que verifica isso, então as seções devem ser ordenadas alfabeticamente. Primeiro `Added`, depois `Changed`, terceiro `Deprecated` e assim por diante.

Agora, digamos que você tem mais uma entrada para adicionar e o tipo dela é `Added`. Como já temos uma seção para isso, você devve apenas adicionar uma nova linha:

```md
## [Unreleased]
### Added
- Utilitário `get_address_from_cep` [#358](https://github.com/brazilian-utils/brutils-python/pull/358)
- Minha outra mensagem de changelog aqui. [#<número_da_issue>](<link_da_issue>)

### Changed
- Utilitário `fmt_voter_id` renomeado  para `format_voter_id` [#221](https://github.com/brazilian-utils/brutils-python/issues/221)

### Fixed
- Minha mensagem de changelog aqui. [#<número_da_issue>](<link_da_issue>)
```

_Este conteúdo é baseado no [site do keep a changelog][keep-a-changelog], já que seguimos suas diretrizes._

### 13. Crie um PR no GitHub

[Crie um PR no GitHub][github-creating-a-pr] para enviar suas alterações para revisão. Para garantir que seu Pull Request (PR) seja claro, eficaz e revisado rapidamente, siga estas boas práticas:

#### Escreva um Título Descritivo para o PR
- Use títulos claros e específicos para descrever o propósito das suas alterações. Um bom título ajuda às pessoas mantenedoras a entender a intenção do PR rapidamente e melhora a rastreabilidade do projeto.
- **Exemplo**: Em vez de “Corrigir problema”, use “Adiciona utilitário `convert_uf_to_text` para lidar com códigos de estados brasileiros.”
- **Benefícios**:
  - Títulos claros facilitam a priorização e o entendimento pelos revisores.
  - Melhoram a organização e a busca no projeto.

#### Forneça uma Descrição Detalhada do PR
- Inclua uma descrição completa no seu PR para explicar:
  - **O que** foi feito (ex.: adicionou uma nova função, corrigiu um bug).
  - **Por que** foi feito (ex.: para resolver uma issue específica ou melhorar o desempenho).
  - **Quais problemas** foram resolvidos ou melhorias aplicadas (ex.: referencie a issue ou descreva a melhoria).
- **Exemplo**:
Este PR adiciona o utilitário convert_uf_to_text para converter códigos de estados brasileiros (ex.: “SP”) em nomes completos (ex.: “São Paulo”). Resolve a issue #474, melhorando a reutilização de código para formatação de endereços. A função inclui validação de entrada e testes atualizados.
- **Benefícios**:
- Descrições detalhadas agilizam o processo de revisão ao fornecer contexto.
- Ajudam futuros mantenedores a entender o propósito e o histórico do código.

#### Vincule o PR à Issue Relacionada
- Referencie a issue que seu PR resolve usando palavras-chave como `Closes #474` ou `Fixes #474` na descrição do PR. Isso fecha a issue automaticamente quando o PR for mesclado.
- **Exemplo**: `Closes #474`
- **Benefícios**:
- Vincular issues mantém o repositório organizado e garante o rastreamento de tarefas.
- Automatiza o fechamento de issues, reduzindo trabalho manual para mantenedores.
- Para mais detalhes, consulte a [documentação do GitHub sobre fechamento automático de issues](https://docs.github.com/pt/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue).

#### Verifique o Template de Descrição do PR
- Certifique-se de que seu PR segue o template de descrição do repositório. Verifique todos os itens obrigatórios, como cobertura de testes, atualizações de documentação ou entradas no changelog.
- **Exemplo de Checklist**: (mostrando como fica quando preenchido):
- [x] Alterações no código foram testadas.
- [x] Documentação (READMEs) foi atualizada.
- [ ] Entrada no changelog foi adicionada (marque apenas se aplicável).
- **Nota sobre a Sintaxe**:
- Use [x] para marcar itens concluídos e [ ] para itens não concluídos, sem espaços dentro dos colchetes (ex.: [ x ] ou [x ] não será renderizado corretamente no GitHub).
- **Benefícios**:
- Seguir o template garante que o PR esteja completo e pronto para revisão.
- Reduz a necessidade de idas e vindas com revisores, acelerando o processo de mesclagem.

### 14. Atualizar a Sua Branch se Necessário

[Certifique-se de que sua branch esteja atualizado com o main][github-sync-pr]

## Lançar uma Nova Versão

Aqui você encontrará como lançar uma nova versão em produção do brutils:

- [1. Criar uma Issue de Release](#1-criar-uma-issue-de-release)
- [2. Criar um Release PR](#2-criar-um-release-pr)
- [3. Deploy via GitHub](#3-deploy-via-github)

### 1. Criar uma Issue de Release

#### Crie a Issue

Para a criação da issue, pode ser utilizado o template de feature, sendo o nome da issue `Release v<versão>`. [Exemplo](https://github.com/brazilian-utils/brutils-python/issues/322)

#### Crie uma Branch

O nome da branch criada para o release é relacionado ao número da Issue, como mostra [este exemplo](https://github.com/brazilian-utils/brutils-python/pull/326)

#### Faça o Commit

A mensagem do commit deve seguir a estrutura `chore: release <versão>`

Exemplo: `chore: release 2.3.0`

### 2. Criar um Release PR

#### Atualizar a Versão da Biblioteca

Incremente o número da versão, seguindo o [Versionamento Semântico][semantic-versioning],
no arquivo `pyproject.toml`:

- [https://github.com/brazilian-utils/brutils-python/blob/main/pyproject.toml#L3]([https://github.com/brazilian-utils/brutils-python/blob/main/pyproject.toml#L3])

#### Atualizar o CHANGELOG.md

Adicione um título para a nova versão com o novo número e a data atual, como
[neste exemplo](https://github.com/brazilian-utils/brutils-python/blob/main/CHANGELOG.md?plain=1#L9).

E adicione os links da versão, como [neste exemplo](https://github.com/antoniamaia/brutils-python/blob/eac770e8b213532d2bb5948d117f6f4684f65be2/CHANGELOG.md?plain=1#L76)

#### Crie o PR

Crie um PR com o nome `chore: release <versão>` contendo as duas alterações acima. Na descrição da Pull Request, adicione o trecho do changelog alterado.

Exemplo de Release PR: https://github.com/brazilian-utils/brutils-python/pull/596

#### Faça o Merge do PR

Assim que o PR for aceito e passar em todas as verificações, faça o merge.

### 3. Deploy via GitHub

O lançamento da nova versão em produção é feita automaticamente quando uma
[nova release é criada][creating-releases] no GitHub.

- Preencha o campo `tag version` com: `v<versão>` (por exemplo, `v2.0.0`).
- Preencha o campo `release title` com o mesmo valor que a versão da tag (por exemplo, `v2.0.0`).
- Preencha o campo `release description` com o conteúdo copiado do arquivo CHANGELOG.md da seção de
versão correspondente.

Exemplos reais estão disponíveis em: [https://github.com/brazilian-utils/brutils-python/releases][brutils-releases]

Quando o Deploy via GitHub for concluído, a nova versão também será lançada automaticamente no
[PyPI][brutils-on-pypi]. Baixe a nova versão do brutils do PyPI e teste se tudo está
funcionando conforme o esperado.

[brutils-issues]: https://github.com/brazilian-utils/brutils-python/issues
[brutils-on-pypi]: https://pypi.org/project/brutils/
[brutils-releases]: https://github.com/brazilian-utils/brutils-python/releases
[changelog]: https://github.com/brazilian-utils/brutils-python/blob/main/CHANGELOG.md
[creating-releases]: https://docs.github.com/pt/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release
[docstring-definition]: https://www.python.org/dev/peps/pep-0257/#what-is-a-docstring
[github-cloning]: https://docs.github.com/pt/repositories/creating-and-managing-repositories/cloning-a-repository
[github-creating-a-pr]: https://docs.github.com/pt/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request
[github-essentials-criar-conta]: https://github-essentials.cumbuca.dev/dia-5-contas-e-planos/criacao-de-uma-conta-pessoal-no-github
[github-essentials-instalando-o-git]: https://github-essentials.cumbuca.dev/dia-2-controle-de-versao-basico-com-git/git/instalando-o-git
[github-forking]: https://docs.github.com/pt/get-started/quickstart/contributing-to-projects
[github-join]: https://github.com/join
[github-sync-pr]: https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/keeping-your-pull-request-in-sync-with-the-base-branch
[keep-a-changelog]: https://keepachangelog.com/en/1.0.0/
[poetry]: https://python-poetry.org/docs/#installation
[python]: https://www.python.org/downloads/
[release-pr-example]: https://github.com/brazilian-utils/brutils-python/pull/326
[semantic-versioning]: https://semver.org/lang/pt-BR/
[virtualenv]: https://virtualenv.pypa.io/en/latest/

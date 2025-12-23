# Contributing

Thanks for taking the time to contribute! 🙇‍♀️🙇‍♂️ Every little bit of help counts!

- [First Contribution](#first-contribution)
- [Release a New Version](#release-a-new-version)

### 💌 Want to contribute, but don’t feel comfortable?

Do you feel like contributing but feel uncomfortable opening issues, PRs, or asking questions publicly?

We know how hard it can be to take the first step in an open space. Insecurity, the fear of making mistakes, or even wondering “is my question silly?” can weigh heavily. And it’s okay to feel that way. 💜

We want you to know that no one has to face this journey alone. If you’d prefer a more private space, you can send an email to cumbucadev@gmail.com, and we’ll be happy to help. Whether it’s to clear up doubts, ask for guidance, or simply have someone to talk to about how to get started.

What matters is that you know: your participation is very welcome, and every contribution, no matter how small it may seem, makes a big difference. ✨

## First Contribution

How to make your first contribution:

- [Contributing](#contributing)
    - [💌 Want to contribute, but don’t feel comfortable?](#-want-to-contribute-but-dont-feel-comfortable)
  - [First Contribution](#first-contribution)
    - [1. Create a GitHub Account](#1-create-a-github-account)
    - [2. Find an Issue to Work With](#2-find-an-issue-to-work-with)
    - [3. Install Git](#3-install-git)
    - [4. Fork the Project](#4-fork-the-project)
    - [5. Clone your Fork](#5-clone-your-fork)
    - [6. Create a New Branch](#6-create-a-new-branch)
    - [7. Run brutils locally](#7-run-brutils-locally)
      - [Installation with poetry](#installation-with-poetry)
        - [Requirements](#requirements)
      - [Installation with pip](#installation-with-pip)
        - [Requirements](#requirements-1)
      - [Using locally](#using-locally)
  - [Tests](#tests)
    - [8. Make your changes](#8-make-your-changes)
    - [9. Test your changes](#9-test-your-changes)
      - [Write new tests](#write-new-tests)
      - [Make sure all tests passed](#make-sure-all-tests-passed)
      - [Test it manually](#test-it-manually)
    - [11. Commit and push your changes](#11-commit-and-push-your-changes)
    - [12. Create a GitHub PR](#12-create-a-github-pr)
      - [Write a Descriptive PR Title](#write-a-descriptive-pr-title)
      - [Provide a Detailed PR Description](#provide-a-detailed-pr-description)
      - [Link the PR to the Related Issue](#link-the-pr-to-the-related-issue)
      - [Verify the PR Description Template](#verify-the-pr-description-template)
    - [13. Update your branch if needed.](#13-update-your-branch-if-needed)
  - [Release a New Version](#release-a-new-version)
    - [1. Create a Release Issue](#1-create-a-release-issue)
      - [Create the Issue](#create-the-issue)
      - [Create a Branch](#create-a-branch)
    - [2. Create a Release PR](#2-create-a-release-pr)
      - [Update the Library Version](#update-the-library-version)
      - [Update the CHANGELOG.md](#update-the-changelogmd)
      - [Create the PR](#create-the-pr)
      - [Merge the PR](#merge-the-pr)
    - [3. Deploy via GitHub](#3-deploy-via-github)

### 1. Create a GitHub Account

Ensure you have a [GitHub account][github-join] and you are logged in.

### 2. Find an Issue to Work With

Visit the [brutils issues page][brutils-issues] and find an issue that interests you and hasn't been assigned yet.

Leave a comment in the issue with "bora!" (in Brazilian Portuguese, that means "let's go!"). A bot will assign the issue to you. Once assigned, proceed to the next step.

Feel free to ask any questions in the issue's page before or during the development process.

When starting to contribute, it is advised to handle one issue at a time. This ensures others have the chance to collaborate and avoids inactive resources.

### 3. Install Git

Make sure you have [Git installed][install-git].

### 4. Fork the Project

[Fork the brutils repository][github-forking].

### 5. Clone your Fork

[Clone your fork][github-cloning] locally.

### 6. Create a New Branch

Go into the brutils folder:

```bash
$ cd brutils-python
>
```

And create a new branch with the issue number you’re working on:

```bash
$ git checkout -b <issue_number>
>
```
Example:

```bash
$ git checkout -b 386
Switched to a new branch '386'
>
```

### 7. Run brutils locally

#### Installation with poetry

##### Requirements

- [Python 3.10+][python]
- [Poetry][poetry]

Create a [virtualenv][virtualenv] for brutils and activate it:

```shell
$ make shell
Spawning shell within ...-py3.x
emulate bash -c '. .../bin/activate'
```

To test if the virtual environment is correctly activated, run:

```sh
$ poetry env inf
Virtualenv
Python:         3.x.y
Implementation: CPython
...
```

**Note: You need to run `make shell` every time you open a new terminal window/tab.**

Install the dependencies:

```shell
$ make install
git config --local core.hooksPath .githooks/
chmod -R +x .githooks
Installing dependencies from lock file
...
```

#### Installation with pip

If you prefer to use pip, you can install the project in development mode as follows:

##### Requirements

- [Python 3.10+][python]
- [pip][pip]

Create a [virtualenv][virtualenv] for brutils and activate it using the following command:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

Use the pip command to install the dev and test dependencies through the requirements-dev.txt file:

```sh
pip install -r requirements-dev.txt
```

#### Using locally

Now, you can use it [in the same way described in the README.md file](/README_EN.md#usage).

## Tests

Run tests using the following command:

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

### 8. Make your changes

Now it’s time to implement your changes.

Check the issue description for instructions or ideas in the section “Describe alternatives you considered.” Make sure your changes resolve everything mentioned in the issue.

We document our code using [docstrings][docstring-definition]. All modules, classes, functions, and methods should have docstrings. Your changes should reflect updated docstrings, especially if any parameters were changed.

All docstrings must be written in English. You can use tools like Google Translate or ChatGPT for help. We’ll suggest changes to the translation if needed.

We follow this pattern for docstring consistency:

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

Example:

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

One last thing to keep in mind while self-documenting code with docstrings that you can ignore
docstrings in property decorators and magic methods.

### 9. Test your changes

#### Write new tests

Make sure you have created the necessary tests for every new change you made.

#### Make sure all tests passed

Run all the tests with `make test` and make sure that they all passed.

**PRs will not be merged if there is any test missing or failing.**

#### Test it manually

Open an interactive environment to manually test your changes:

```sh
$ python
Python 3.x.y ...
Type "help", "copyright", "credits" or "license" for more information.
>>> # Test your changes here!

### 10. Update READMEs

Update the `brutils-python/README.md` and `brutils-python/README_EN.md` files with your changes.

These files are essential for the library’s documentation, helping users understand how to use the provided features. Therefore, it’s important to always keep them up to date.

	•	The brutils-python/README_EN.md file contains the documentation in English, and you can use the content already described in the docstring directly.
	•	The brutils-python/README.md file contains the documentation in Portuguese. For this one, simply translate the function’s docstring.

If you need help translating into Portuguese, tools like Google Translate or ChatGPT can assist. Don’t worry about potential translation mistakes, as we will suggest adjustments when necessary.

Example in Portuguese (README.md):

````md
### format_cep

Esta função recebe um CEP como entrada e, se for um CEP válido de 8 dígitos, formata-o no padrão "12345-678".

Argumentos:

- cep (str): O CEP a ser formatado.

Retorna:

- str: O CEP formatado no padrão "12345-678" se for válido, ou
         None se não for válido.

Exemplo:

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
Example in English (README_EN.md):

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

### 11. Commit and push your changes

Format your code by running the command:


```bash
$ make format
...
```

Exemple:

```bash
$ make format
31 files left unchanged
All checks passed!
```

Add your changes to the staging area:

```bash
$ git add --all
...
```

Commit your changes:

```bash
$ git commit -a -m "<commit_message>"
...
```

Example:

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

Make the necessary changes and commits and push them when ready.

**Note about CHANGELOG:** The CHANGELOG.md is automatically generated from commits using [git-cliff](https://git-cliff.org/). When your PR is merged into the `main` branch, your changes will automatically appear in the `[Unreleased]` section of the CHANGELOG. Therefore, it's important to follow the [Conventional Commits](https://www.conventionalcommits.org/) pattern in your commit messages:

- `feat:` for new features (will appear in "Added")
- `fix:` for bug fixes (will appear in "Fixed")
- `refactor:` or `perf:` for changes to existing features (will appear in "Changed")
- `docs:`, `test:`, `ci:`, `chore:` are ignored in the changelog

### 12. Create a GitHub PR

[Create a GitHub PR][github-creating-a-pr] to submit your changes for review. To ensure your Pull Request (PR) is clear, effective, and reviewed quickly, follow these best practices:

#### Write a Descriptive PR Title
- Use clear and specific titles to describe the purpose of your changes. A good title helps maintainers understand the PR’s intent at a glance and improves project traceability.
- **Example**: Instead of “Fix issue,” use “Add utility `convert_uf_to_text` to handle Brazilian state codes.”
- **Benefits**:
  - Clear titles make it easier for reviewers to prioritize and understand the PR.
  - They improve the project’s organization and searchability.

#### Provide a Detailed PR Description
- Include a comprehensive description in your PR to explain:
  - **What** was done (e.g., added a new function, fixed a bug).
  - **Why** it was done (e.g., to address a specific issue or improve performance).
  - **What issues** were resolved or improvements applied (e.g., link to the issue or describe the enhancement).
- **Example**:
This PR adds the convert_uf_to_text utility to convert Brazilian state codes (e.g., "SP") to full state names (e.g., "São Paulo"). It addresses issue #474 by improving code reusability for address formatting. The function includes input validation and updated tests.
- **Benefits**:
- Detailed descriptions speed up the review process by providing context.
- They help future maintainers understand the code’s purpose and history.

#### Link the PR to the Related Issue
- Reference the issue your PR addresses using keywords like `Closes #474` or `Fixes #474` in the PR description. This automatically closes the issue when the PR is merged.
- **Example**: `Closes #474`
- **Benefits**:
- Linking issues keeps the repository organized and ensures tasks are tracked.
- It automates issue closure, reducing manual work for maintainers.
- For more details, see the [GitHub documentation on closing issues automatically](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue).

#### Verify the PR Description Template
- Ensure your PR follows the repository's PR description template (if provided). Check all required items, such as test coverage and documentation updates.
- **Example Checklist**: (showing how it looks when completed):
- [x] Code changes are tested.
- [x] Documentation (READMEs) is updated.
- [x] Commit messages follow Conventional Commits pattern.
- **Syntax Note**:
- Use [x] to mark completed items and [ ] for incomplete ones, with no spaces inside the brackets (e.g., [ x ] or [x ] will not render correctly on GitHub).
- **Benefits**:
- Adhering to the template ensures your PR is complete and ready for review.
- It reduces back-and-forth with reviewers, speeding up the merge process.

### 13. Update your branch if needed.

[Ensure your branch is up to date with main][github-sync-pr].

## Release a New Version

Here you will find how to deploy a new production version of brutils:

- [1. Create a Release Issue](#1-create-a-release-issue)
- [2. Create a Release PR](#2-create-a-release-pr)
- [3. Deploy via GitHub](#3-deploy-via-github)

### 1. Create a Release Issue

#### Create the Issue

To create the issue, you can use the feature template, naming the issue Release v<version>. [Example](https://github.com/brazilian-utils/brutils-python/issues/322)

#### Create a Branch

The name of the branch created for the release is related to the Issue number, as shown in [this example](https://github.com/brazilian-utils/brutils-python/pull/326)


### 2. Create a Release PR

#### Update the Library Version

Increment the version number, following the [Semantic Versioning][semantic-versioning],
in the `pyproject.toml` file: https://github.com/brazilian-utils/brutils-python/blob/main/pyproject.toml#L3

#### Update the CHANGELOG.md

Run `git cliff --bump --output CHANGELOG.md`

#### Create the PR

Create a PR named `Release v<version>` containing the two changes mentioned above. In the description of the Pull Request, add the modified section of the changelog.

[Example of Release PR](https://github.com/brazilian-utils/brutils-python/pull/128)

#### Merge the PR

Once the PR is accepted and passes all checks, merge it.

### 3. Deploy via GitHub

The new version release in production is done automatically when a [new release is created][creating-releases] on GitHub.

- Fill in the `tag version` should be `v<version>` (e.g `v2.0.0`).
- Fill in the `release title` should be the same as tag version (e.g `v2.0.0`).
- Fill in the `release description` should be the content copied from the CHANGELOG.md file from the
corresponding version section.

Real examples are available at: https://github.com/brazilian-utils/brutils-python/releases

When the GitHub deployment is completed, the new version will also be automatically released on 
[PyPI][brutils-on-pypi]. Download the new brutils version from PyPI and test to ensure everything is working as expected.


[brutils-issues]: https://github.com/brazilian-utils/brutils-python/issues
[brutils-on-pypi]: https://pypi.org/project/brutils/
[brutils-releases]: https://github.com/brazilian-utils/brutils-python/releases
[changelog]: https://github.com/brazilian-utils/brutils-python/blob/main/CHANGELOG.md
[creating-releases]: https://docs.github.com/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release
[docstring-definition]: https://www.python.org/dev/peps/pep-0257/#what-is-a-docstring
[github-cloning]: https://docs.github.com/repositories/creating-and-managing-repositories/cloning-a-repository
[github-creating-a-pr]: https://docs.github.com/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request
[github-forking]: https://docs.github.com/get-started/quickstart/contributing-to-projects
[github-join]: https://github.com/join
[github-sync-pr]: https://docs.github.com/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/keeping-your-pull-request-in-sync-with-the-base-branch
[keep-a-changelog]: https://keepachangelog.com/en/1.0.0/
[poetry]: https://python-poetry.org/docs/#installation
[python]: https://www.python.org/downloads/
[release-pr-example]: https://github.com/brazilian-utils/brutils-python/pull/326
[semantic-versioning]: https://semver.org
[virtualenv]: https://virtualenv.pypa.io/en/latest/

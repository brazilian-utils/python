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

- [1. Create a GitHub Account](#1-create-a-github-account)
- [2. Find an Issue to Work On](#2-find-an-issue-to-work-on)
- [3. Install Git](#3-install-git)
- [4. Fork the Project](#4-fork-the-project)
- [5. Clone your Fork](#5-clone-your-fork)
- [6. Create a New Branch](#6-create-a-new-branch)
- [7. Run brutils Locally](#7-run-brutils-locally)
- [8. Make your Changes](#8-make-your-changes)
- [9. Test your Changes](#9-test-your-changes)
- [10. Update READMEs](#10-update-readmes)
- [11. Commit and push your Changes](#11-commit-and-push-your-changes)
- [12. Add changelog Entries](#12-add-changelog-entries)
- [13. Create a GitHub PR](#13-create-a-github-pr)
- [14. Update your branch if Needed.](#14-update-your-branch-if-needed)

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

### 12. Add changelog entries

#### What is a changelog?

A changelog is a file that contains a chronologically organized list of notable changes for each version of a project.

#### Why maintain a changelog?

To make it easier for users and contributors to see exactly what notable changes have been made between each release (or version) of the project.

####  Who needs a changelog?

People. Whether they are consumers or developers, the end users of software are human beings who care about what’s in the software. When the software changes, people want to know why and how.

####  Where is the brutils changelog?

The brutils changelog is available at [CHANGELOG.md][changelog].

####  Guiding principles

- Changelogs are for humans, not machines.
- There should be an entry for every version.
- The same types of changes should be grouped together.
- Versions and sections should be linkable.
- The most recent version comes first.
- The release date of each version is displayed.

####  What justifies an entry in the changelog?

- Security fixes: These should be documented with the type labeled as “security” to alert users to resolved security issues.
Example: “Fixed a critical vulnerability that allowed remote code execution.”

- User-facing changes: Changes that directly affect how users interact with the software, including new features, changes to existing features, or UI improvements.
Example: “Added a new filter option on the results page to make searching easier.”

- Significant performance improvements: Should be recorded when they result in noticeable improvements in speed or efficiency that impact the user experience.
Example: “The home page loading time was reduced by 40% after backend optimization.”

- Changes affecting compatibility: Adjustments to maintain compatibility with other tools, systems, or versions.
Example: “Updated library X to version 2.0 to support the new version of Python.”

- Changes to the public API: Changes that affect how developers interact with the public API, such as adding new routes or modifying existing ones.
Example: “Added a new /api/v1/users route for user management.”

- Dependency changes: Updates or changes to the project’s dependencies that may affect software behavior or compatibility.
Example: “Updated dependency package Y to version 3.1.4, which includes important security fixes.”

#### What should NOT go in the changelog

Although the changelog is a valuable tool for documenting changes, some information should not be included. Here are some examples of what should not appear in the changelog:

- Internal Code Changes: Changes that do not affect the end-user experience, such as internal refactoring that does not alter functionality, need not be documented.
Example: “Refactored internal functions” or “Fixed inconsistent tests.”

- Non-notable performance improvements: Performance improvements that do not result in noticeable changes or clear benefits for the end user do not need to be included.
Example: “Optimized internal algorithms.”

- Minor bug fixes: Bug fixes that do not impact the general use or end-user experience can be omitted.
Example: “Fixed a small typo in the code.”

- Documentation-only changes: Changes that affect only the documentation, without modifying the software behavior, usually don’t need to be included.
Example: “Updated README.md to reflect new dependencies.”

- Excessive technical details: Overly technical information that is irrelevant to the end user or does not provide context on the impact of the change should be avoided.
Example: “Changed memory management in class X.”

- Maintainer entries: Changes related only to the development or internal maintenance process, such as CI/CD tool configuration adjustments, are generally not relevant for the changelog.
Example: “Updated GitHub Actions configuration.”

- A bug introduced and fixed in the same release does not need a changelog entry.

Avoid including this information to keep the changelog focused and useful for project users and contributors.

#### Writing good changelog entries

A good changelog entry should be both descriptive and concise. It should explain the change to a reader with no prior context about the change. If it’s hard to be both concise and descriptive, lean toward being more descriptive.

- **Bad** : Go to the project order.
- **Good**: Display the user’s starred projects at the top of the “Go to project” dropdown.

The first example provides no context on where the change was made, why it was made, or how it benefits the user.

- **Bad**: Copy (some text) to the clipboard.
- **Good**: Update the tooltip of “Copy to clipboard” to indicate what is being copied.

Again, the first example is too vague and provides no context.

- **Bad**: Fix and improve CSS and HTML issues in the mini pipeline graph and builds dropdown.
- **Good**: Fix tooltips and hover states in the mini pipeline graph and builds dropdown.

The first example is too focused on implementation details. Users don’t care that we changed CSS and HTML, they care about the final result of those changes.

- **Bad**: Remove null values in the Commit object array returned by find_commits_by_message_with_elastic.
- **Good**: Fix 500 errors caused by Elasticsearch results referencing commits already collected by the garbage collector.

The first example focuses on how we fixed something, not on what was fixed. The rewritten version clearly describes the final benefit to the user (fewer 500 errors) and when it happens (when searching for commits with Elasticsearch).

Use your best judgment and try to put yourself in the position of someone reading the compiled changelog. Does this entry add value? Does it provide context on where and why the change was made?

#### How to add an entry to the changelog

The changelog is available in the [CHANGELOG.md][changelog] file.

First, you need to identify the type of your change. Types of changes:

- `Added` for new features. 
- `Changed` for changes to existing features. 
- `Deprecated` for features that will soon be removed. 
- `Fixed` for any bug fixes. 
- `Removed` for features that were removed. 
- `Security` in case of vulnerabilities.

You should always add new entries to the changelog in the `Unreleased` section. At the time of release, we will move the changes from the `Unreleased` section to a new version section.

So, within the `Unreleased` section, you should add your entry to the appropriate section by type. If there is no section yet for the type of your change, you should add one.

Let’s see some examples. Suppose you have a new `Fixed` change to add, and the current CHANGELOG.md file looks like this:

```md
## [Unreleased]
### Added
- Utility `get_address_from_cep` [#358](https://github.com/brazilian-utils/brutils-python/pull/358)

### Changed
- Utility `fmt_voter_id` renamed to `format_voter_id` [#221](https://github.com/brazilian-utils/brutils-python/issues/221)
```

You would need to add a new `Fixed` section and include your new entry there:

```md
## [Unreleased]
### Added
- Utility `get_address_from_cep` [#358](https://github.com/brazilian-utils/brutils-python/pull/358)

### Changed
- Utility `fmt_voter_id` renamed to `format_voter_id` [#221](https://github.com/brazilian-utils/brutils-python/issues/221)

### Fixed
- My changelog message here. [#<issue_number>](<issue_link>)
```

Note that the order of sections by type matters. We have a lint that checks this, so the sections must be ordered alphabetically. First `Added`, then `Changed`, third `Deprecated`, and so on.

Now, let’s say you have another entry to add, and its type is `Added`. Since we already have a section for that, you should just add a new line:

```md
## [Unreleased]
### Added
- Utility `get_address_from_cep` [#358](https://github.com/brazilian-utils/brutils-python/pull/358)
- My other changelog message here. [#<issue_number>](<issue_link>)

### Changed
- Utility `fmt_voter_id` renamed to `format_voter_id` [#221](https://github.com/brazilian-utils/brutils-python/issues/221)

### Fixed
- My changelog message here. [#<issue_number>](<issue_link>)
```

This content is based on the [Keep a Changelog][keep-a-changelog] site, as we follow its guidelines.

### 13. Create a GitHub PR

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
- Ensure your PR follows the repository’s PR description template (if provided). Check all required items, such as test coverage, documentation updates, or changelog entries.
- **Example Checklist**: (showing how it looks when completed):
- [x] Code changes are tested.
- [x] Documentation (READMEs) is updated.
- [ ] Changelog entry is added.
- **Syntax Note**:
- Use [x] to mark completed items and [ ] for incomplete ones, with no spaces inside the brackets (e.g., [ x ] or [x ] will not render correctly on GitHub).
- **Benefits**:
- Adhering to the template ensures your PR is complete and ready for review.
- It reduces back-and-forth with reviewers, speeding up the merge process.

### 14. Update your branch if needed.

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

Add a title for the new version with the new number and the current date, as seen in [this example](https://github.com/brazilian-utils/brutils-python/blob/main/CHANGELOG.md?plain=1#L9).

And add the version links, like [this example](https://github.com/antoniamaia/brutils-python/blob/eac770e8b213532d2bb5948d117f6f4684f65be2/CHANGELOG.md?plain=1#L76)

#### Create the PR

Create a PR named `Release v<version>` containing the two changes mentioned above. In the description of the Pull Request, add the modified section of the changelog.


[Example of Release PR](https://github.com/brazilian-utils/brutils-python/pull/128)

#### Merge the PR

Once the PR is accepted and passes all checks, merge it.

### 2. Deploy via GitHub

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

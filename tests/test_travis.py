import pytest


@pytest.mark.parametrize('version', ['3.7', '3.6'])
@pytest.mark.parametrize('pipenv', ['y', 'n'])
def test_travis_total_lines(cookies, context, version, pipenv):
    """
    We expect .travis.yml has below content
    ```
    1 sudo: required
    2
    3 language: python
    4
    5 install:
    6   - make
    ```
    """
    ctx = context(version=version, pipenv=pipenv)
    result = cookies.bake(extra_context=ctx)

    makefile = result.project.join('.travis.yml')
    lines = makefile.readlines(cr=False)

    expected = 32
    expected -= 2 if version == '3.6' else 0
    expected -= 6 if pipenv == 'n' else 0
    assert len(lines) == expected


@pytest.mark.parametrize('version', ['3.7', '3.6'])
@pytest.mark.parametrize('pipenv', ['y', 'n'])
def test_travis_total_section(cookies, context, version, pipenv):
    ctx = context(version=version, pipenv=pipenv)
    result = cookies.bake(extra_context=ctx)

    makefile = result.project.join('.travis.yml')
    content = makefile.read()
    sections = content.strip().split('\n\n')

    expected = 10
    expected -= 1 if version == '3.6' else 0
    expected -= 1 if pipenv == 'n' else 0
    assert len(sections) == expected

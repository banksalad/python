import re

import pytest


@pytest.mark.parametrize('black', ['y', 'n'])
@pytest.mark.parametrize('pipenv', ['y', 'n'])
@pytest.mark.parametrize('mypy', ['do not use', 'beginner', 'expert'])
def test_makefile_total_lines(cookies, context, black, pipenv, mypy):
    """
    We expect Makefile has below content
    ```
    1 .PHONY: check
    2 check:
    3     isort
    4     black
    5
    6 .PHONY: format
    7 format:
    8     isort
    9     black
    ```
    """
    ctx = context(black=black, pipenv=pipenv, mypy=mypy)
    result = cookies.bake(extra_context=ctx)

    makefile = result.project.join('Makefile')
    lines = makefile.readlines(cr=False)

    expected = 31
    expected -= 2 if black == 'n' else 0
    expected -= 1 if mypy == 'do not use' else 0
    expected += 5 if pipenv == 'y' else 0
    assert len(lines) == expected


@pytest.mark.parametrize('black', ['y', 'n'])
@pytest.mark.parametrize('pipenv', ['y', 'n'])
@pytest.mark.parametrize('mypy', ['do not use', 'beginner', 'expert'])
def test_makefile_total_section(cookies, context, black, pipenv, mypy):
    ctx = context(black=black, pipenv=pipenv, mypy=mypy)
    result = cookies.bake(extra_context=ctx)

    makefile = result.project.join('Makefile')
    content = makefile.read()
    sections = content.strip().split('\n\n')

    expected = 7
    expected -= 1 if pipenv == 'n' else 0
    assert len(sections) == expected


@pytest.mark.parametrize('pipenv', ['y', 'n'])
def test_makefile_phony(cookies, context, pipenv):
    ctx = context(pipenv=pipenv)
    result = cookies.bake(extra_context=ctx)

    makefile = result.project.join('Makefile')

    phonies = re.findall(r'\.PHONY: (\w+)', makefile.read())

    expected = 7
    expected -= 1 if pipenv == 'n' else 0
    assert len(set(phonies)) == expected

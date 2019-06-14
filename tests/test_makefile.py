import pytest


@pytest.mark.parametrize('black', ['y', 'n'])
@pytest.mark.parametrize('pipenv', ['y', 'n'])
@pytest.mark.parametrize('mypy', ['do not use', 'beginner', 'expert'])
def test_makefile_total_lines(cookies, context, black, pipenv, mypy):
    """
    We expect Makefile has below content
    ```
    1 check:
    2     isort
    3     black
    4
    5 format:
    6     isort
    7     black
    ```
    """
    ctx = context(black=black, pipenv=pipenv, mypy=mypy)
    result = cookies.bake(extra_context=ctx)

    makefile = result.project.join('Makefile')
    lines = makefile.readlines(cr=False)

    expected = 27
    expected -= 2 if black == 'n' else 0
    expected -= 1 if mypy == 'do not use' else 0
    expected += 4 if pipenv == 'y' else 0
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

    expected = 8
    expected -= 1 if pipenv == 'n' else 0
    assert len(sections) == expected


@pytest.mark.parametrize('pipenv', ['y', 'n'])
def test_makefile_phony(cookies, context, pipenv):
    ctx = context(pipenv=pipenv)
    result = cookies.bake(extra_context=ctx)

    makefile = result.project.join('Makefile')
    lines = makefile.readlines()
    phony = lines[0]

    expected = 8
    expected -= 1 if pipenv == 'n' else 0
    assert len(phony.split(' ')) == expected

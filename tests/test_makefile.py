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
    assert len(lines) == expected

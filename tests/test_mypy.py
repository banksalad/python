import pytest


@pytest.mark.parametrize('mypy', ['beginner', 'expert'])
def test_makefile_total_lines(cookies, context, mypy):
    """
    We expect mypy.ini has below content
    ```
    1 [mypy]
    2 python_version = 3.7
    3 ignore_missing_imports = True
    4 check_untyped_defs = False
    5 disallow_untyped_defs = False
    6 disallow_any_generics = True
    7 warn_no_return = True
    8 no_implicit_optional = True
    9
    ```
    """
    ctx = context(mypy=mypy)
    result = cookies.bake(extra_context=ctx)

    ini = result.project.join('mypy.ini')
    lines = ini.readlines(cr=False)

    expected = 9
    assert len(lines) == expected

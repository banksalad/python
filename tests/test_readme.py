import pytest


def test_bake_project(cookies):
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'python-project'
    assert result.project.isdir()


@pytest.mark.parametrize('version', ['3.7', '3.6'])
@pytest.mark.parametrize('black', ['y', 'n'])
@pytest.mark.parametrize('travis', ['y', 'n'])
def test_readme_total_lines(cookies, context, version, black, travis):
    """
    We expect README.md has below context
    ```
    1 # Python Project
    2
    3 [python][black][travis] ...
    4
    5 (TBD)
    6
    ```
    """
    ctx = context(version=version, black=black, travis=travis)
    result = cookies.bake(extra_context=ctx)

    readme = result.project.join('README.md')
    lines = readme.readlines(cr=False)

    assert len(lines) == 6

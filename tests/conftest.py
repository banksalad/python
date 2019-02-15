import pytest


@pytest.fixture
def context():
    def builder(
        version='3.7', mypy='do not use', black='n', pipenv='n', travis='y'
    ):
        return {
            'project_name': 'Rainist',
            'project_slug': 'rainist',
            'package_name': 'cookie',
            'python_version': version,
            'use_mypy': mypy,
            'use_black': black,
            'use_pipenv': pipenv,
            'use_travis': travis,
        }

    return builder

#!/usr/bin/env python
import os


def remove_file(name):
    os.remove(name)


if __name__ == '__main__':
    if '{{ cookiecutter.use_mypy|lower }}' == 'do not use':
        remove_file('mypy.ini')
    if '{{ cookiecutter.user_pipenv|lower }}' == 'n':
        remove_file('.gitattributes')
        remove_file('Pipfile')

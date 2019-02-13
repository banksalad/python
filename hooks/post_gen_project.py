#!/usr/bin/env python
import os


def remove_file(name):
    os.remove(name)


if __name__ == '__main__':
    if '{{ cookiecutter.use_mypy|lower }}' == 'n':
        remove_file('mypy.ini')

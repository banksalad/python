# {{ cookiecutter.project_name }}

[![Python Version: {{ cookiecutter.python_version }}](https://badgen.net/badge/python/{{ cookiecutter.python_version }}/blue)](https://docs.python.org/{{ cookiecutter.python_version }}/)

{%- if cookiecutter.use_black|lower != 'n' -%}
[![Code Style: Black](https://badgen.net/badge/code%20style/black/black)](https://github.com/ambv/black)
{%- endif %}

{%- if cookiecutter.use_travis|lower != 'n' -%}
[![Build Status](https://badgen.net/badge/travis/passing/green)](https://travis-ci.com/)[![codecov](https://badgen.net/badge/coverage/100%25/green)](https://codecov.io/)
<!-- TODO: You should change codecov, travis badges to valid URL-->
{%- endif %}

(TBD)

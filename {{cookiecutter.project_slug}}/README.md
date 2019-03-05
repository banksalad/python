# {{ cookiecutter.project_name }}

[![Python Version: {{ cookiecutter.python_version }}](https://badgen.net/badge/python/{{ cookiecutter.python_version }}/blue)](https://docs.python.org/{{ cookiecutter.python_version }}/)

{%- if cookiecutter.use_black|lower != 'n' -%}
&nbsp;[![Code Style: Black](https://badgen.net/badge/code%20style/black/black)](https://github.com/ambv/black)
{%- endif %}

{%- if cookiecutter.use_travis|lower == 'y' -%}
&nbsp;[![Build Status](https://badgen.net/badge/travis/passing/green)](https://travis-ci.com/)[![codecov](https://badgen.net/badge/coverage/100%25/green)](https://codecov.io/)
<!-- TODO: You should change codecov, travis badges to valid URL-->
{%- endif %}

## Getting Started

<!-- TODO: Describe how to prepare to use this project -->

### Installation

```sh
$ make
$ ./bin/install_hooks.sh
```

## Test

```sh
$ make check
$ make test
```

## Requirements

<!-- TODO: Describe stack of this project -->

{%- if cookiecutter.use_pipenv|lower != 'n' %}
* [Pipenv](https://github.com/pypa/pipenv) - 의존성 관리
{%- endif %}

## Related Documents

<!-- TODO: Insert related documents here-->

## License

<!-- TODO: If you want, set license information here-->

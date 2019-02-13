# {{ cookiecutter.project_name }}

{% if cookiecutter.python_version == "3.7" -%}
[![Python Version: 3.7](https://badgen.net/badge/python/3.7/blue)](https://docs.python.org/3.7/)
{% else -%}
[![Python Version: 3.6](https://badgen.net/badge/python/3.6/blue)](https://docs.python.org/3.6/)
{%- endif -%}

{%- if cookiecutter.use_black|lower == 'y' -%}
[![Code Style: Black](https://badgen.net/badge/code%20style/black/black)](https://github.com/ambv/black)
{%- endif %}

(TBD)

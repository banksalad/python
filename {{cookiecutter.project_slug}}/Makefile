check:
	isort --recursive --check-only
{%- if cookiecutter.use_black|lower == 'y' %}
	black -S -l 79 --check .
{%- endif %}
	pylint {{ cookiecutter.package_name }}

format:
	isort -rc -y
{%- if cookiecutter.use_black|lower == 'y' %}
	black -S -l 79 .
{%- endif %}

test:
	python -m pytest

coverage:
	python -m pytest --cov {{ cookiecutter.package_name }} --cov-report term

htmlcov:
	python -m pytest --cov {{ cookiecutter.package_name }} --cov-report html
	rm -rf /tmp/htmlcov && mv htmlcov /tmp/
	open /tmp/htmlcov/index.html

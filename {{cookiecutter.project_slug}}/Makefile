.PHONY: init check format test coverage htmlcov

init:
{%- if cookiecutter.use_pipenv|lower != 'n' %}
	pip install pipenv
	pipenv install --dev
{%- else %}
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
{%- endif %}

check:
	isort --recursive --check-only {{ cookiecutter.package_name }} tests
{%- if cookiecutter.use_black|lower != 'n' %}
	black -S -l 79 --check {{ cookiecutter.package_name }} tests
{%- endif %}
	pylint {{ cookiecutter.package_name }}
{%- if cookiecutter.use_mypy|lower != 'do not use' %}
	mypy {{ cookiecutter.package_name }}
{%- endif %}

format:
	isort -rc -y {{ cookiecutter.package_name }} tests
{%- if cookiecutter.use_black|lower != 'n' %}
	black -S -l 79 {{ cookiecutter.package_name }} tests
{%- endif %}

test:
	python -m pytest

coverage:
	python -m pytest --cov {{ cookiecutter.package_name }} --cov-report term

htmlcov:
	python -m pytest --cov {{ cookiecutter.package_name }} --cov-report html
	rm -rf /tmp/htmlcov && mv htmlcov /tmp/
	open /tmp/htmlcov/index.html

{%- if cookiecutter.use_pipenv|lower != 'n' %}

requirements:
	pipenv lock -r > requirements.txt
	pipenv lock -dr > requirements-dev.txt
{%- endif %}

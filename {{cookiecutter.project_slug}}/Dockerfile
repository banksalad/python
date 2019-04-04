{%- if cookiecutter.python_version == "3.7" -%}
FROM python:3.7.2-alpine3.9 AS base
{%- else -%}
FROM python:3.6.8-alpine3.9 AS base
{%- endif %}

RUN pip install -U pip

# Build Stage
FROM base AS build

RUN apk update && apk add --no-cache --upgrade \
    build-base \
    gcc

WORKDIR /wheels
COPY requirements.txt .

RUN pip wheel -r requirements.txt

# Execution Stage
FROM base

ENV PYTHONUNBUFFERED=1

COPY --from=build /wheels /wheels

RUN pip install -r /wheels/requirements.txt -f /wheels && \
    rm -rf /wheels && \
    rm -rf /root/.cache/pip/*

WORKDIR /app

COPY {{ cookiecutter.package_name }} {{ cookiecutter.package_name }}

ENTRYPOINT ["python"]
CMD ["-m", "{{ cookiecutter.package_name }}"]

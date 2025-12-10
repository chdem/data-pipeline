# Modular python project

## Prerequisites

    - python 3
    - docker

## launch
    - update .env file
    - docker compose up -d

## use
{% if cookiecutter.include_minio == "yes" %}
### Minio
[Minio gui guide](https://blog.min.io/great-gui/)
{% endif %}

{% if cookiecutter.include_postgres == "yes" %}
### Postgres
[Pg_admin Gui guide](https://www.pgadmin.org/docs/pgadmin4/development/connect_to_server.html)
{% endif %}

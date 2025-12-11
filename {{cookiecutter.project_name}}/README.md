# Modular python project

## Prerequisites

    - python 3
    - docker

## launch
    - update .env file
    - docker compose up -d

## Modules
{% if cookiecutter.include_minio == "yes" %}
### Minio
Non structured storage client very similar to amazon S3 buckets.
[Minio gui guide](https://blog.min.io/great-gui/)
{% endif %}
{% if cookiecutter.include_postgres == "yes" %}
### Postgres

At first launch, every sql files in directory /src/postgres/scripts will be played by the potgres SGBD.

Postgres and Pgadmin share the same volume.

You can use command line to connect postgres :
```bash
docker exec -it templ_postgres sh 
psql -U bob templ_test #then use standard sql commands
```

or you can use Pgadmin4 gui :

[Pg_admin Gui guide](https://www.pgadmin.org/docs/pgadmin4/development/connect_to_server.html)
{% endif %}

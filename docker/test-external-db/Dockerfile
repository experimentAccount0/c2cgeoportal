FROM camptocamp/postgres:9.5

LABEL maintainer Camptocamp "info@camptocamp.com"

ENV POSTGRES_USER www-data
ENV POSTGRES_DB test

COPY *.sql /docker-entrypoint-initdb.d

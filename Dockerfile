FROM camptocamp/geomapfish_build_dev:jenkins
LABEL maintainer Camptocamp "info@camptocamp.com"

COPY . /tmp/

RUN \
  cd /tmp && \
  pip install . && \
  rm --recursive --force /tmp/*

WORKDIR /src

ENV PYTHONPATH /build/venv/lib/python2.7/site-packages/

FROM python:2
LABEL maintainer Camptocamp "info@camptocamp.com"

RUN \
  apt-get update && \
  apt-get install --assume-yes --no-install-recommends vim tree make git curl ca-certificates apt-transport-https libpq5 libgeos-c1 gettext libpq-dev libgeos-dev libjpeg-dev gcc && \
  curl --silent https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
  echo 'deb https://deb.nodesource.com/node_4.x jessie main' > /etc/apt/sources.list.d/nodesource.list && \
  apt-get update && \
  apt-get install --assume-yes --no-install-recommends nodejs && \
  apt-get clean && \
  rm --recursive --force /var/lib/apt/lists/*

COPY base-requirements.txt dev-requirements.txt fixversions.txt /tmp/

RUN \
  cd /tmp && \
  curl https://bootstrap.pypa.io/get-pip.py > get-pip.py && \
  python get-pip.py `cat base-requirements.txt` && \
  pip install --requirement dev-requirements.txt && \
  apt-get clean && \
  rm --recursive --force /tmp/* /var/tmp/* /root/.cache/*

COPY run /usr/bin/

WORKDIR /src

ENV PYTHONPATH /build/venv/lib/python2.7/site-packages/

ENTRYPOINT ["run"]

FROM python:3.7-slim-buster

RUN \
  addgroup --gid 1000 python &&\
  adduser --uid 1000 --gid 1000 python

USER python

RUN pip install pytest

WORKDIR /usr/src

COPY pytest.ini .
ENV HOME="/home/python"
ENV PATH="${PATH}:${HOME}/.local/bin"

ENTRYPOINT ["pytest"]

FROM ubuntu:focal

ARG TZ="UTC"

WORKDIR /usr/src/oura-stats

RUN apt-get update && \
    apt-get -y install python3 python3-pip

ADD . .

RUN pip3 --disable-pip-version-check --no-cache-dir install -r requirements.txt \
    && rm -rf /tmp/pip-tmp

ENTRYPOINT [ "python3", "main.py" ]
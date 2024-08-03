FROM python:3.12-alpine3.20

ENV PYTHONUNBUFFERED 1
ENV INSTALL_PATH /app

COPY ./requirements.txt /requirements.txt
COPY ./app /app
COPY ./scripts /scripts

WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev linux-headers && \
    apk add postgresql-dev && \
    apk add bash && \
    /py/bin/pip install -r /requirements.txt && \
    apk del build-deps && \
    adduser -D -H app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol && \
    chmod +x /scripts/*

ENV PATH="/scripts:/py/bin:$PATH"

USER app

CMD run.sh
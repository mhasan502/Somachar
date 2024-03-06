FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

USER appuser
RUN mkdir -p /code
WORKDIR /code

COPY requirements.txt /tmp/requirements.txt

RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

COPY . /code/

RUN python manage.py makemigrations &&  \
    python manage.py migrate --run-syncdb &&  \
    python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["uvicorn", "--port", "8000", "Somachar.asgi:application"]

FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV GOOGLE_CLIENT_ID "just_a_random_GOOGLE_CLIENT_ID"
ENV GOOGLE_CLIENT_SECRET "just_a_random_GOOGLE_CLIENT_SECRET"

RUN mkdir -p /code
WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
COPY . /code/

RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

RUN python manage.py makemigrations &&  \
    python manage.py migrate --run-syncdb &&  \
    python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["uvicorn", "--host", "0.0.0.0",  "--port", "8000", "Somachar.asgi:application"]

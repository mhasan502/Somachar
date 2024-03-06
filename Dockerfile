FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY ${{ secrets.SECRET_KEY }}
ENV GOOGLE_CLIENT_ID ${{ secrets.GOOGLE_CLIENT_ID }}
ENV GOOGLE_CLIENT_SECRET ${{ secrets.GOOGLE_CLIENT_SECRET }}

RUN useradd --create-home appuser
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

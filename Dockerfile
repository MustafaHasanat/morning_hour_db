version: '1.0.0'
services:
  web:
    build: .
    command: gunicorn project.wsgi:application --bind 0.0.0.0:8000 --workers 4
    volumes:
      - .:/code
    ports:
      - 8000:8000
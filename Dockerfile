# FROM python:3
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
# WORKDIR /code
# COPY requirements.txt /code/
# RUN pip install -r requirements.txt
# COPY . /code/

# Use an official Python runtime as a parent image
FROM python:3.8-slim
# Set the working directory in the container
WORKDIR /usr/src/app
# Copy only the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock ./
# Install Poetry and project dependencies
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi
# Copy the rest of the application code
COPY . .
# Make port 80 available to the world outside this container
EXPOSE 80
# Define environment variable
ENV DJANGO_SETTINGS_MODULE=morninghour.settings
# Run app.py when the container launches
CMD ["gunicorn", "morninghour.wsgi:application", "--bind", "0.0.0.0:80"]
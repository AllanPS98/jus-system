FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y build-essential libffi-dev

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH="/usr/local/lib/python3.11/site-packages"
ENV PYTHONPATH="${PYTHONPATH}:/app"


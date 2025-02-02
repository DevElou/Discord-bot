# syntax=docker/dockerfile:1

FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
COPY config.yml /app/sconfig.yml


ENV PYTHONPATH="${PYTHONPATH}:/app"
CMD ["python3","-u", "bot.py"]

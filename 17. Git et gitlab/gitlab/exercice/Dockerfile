FROM python:3.11.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

ENTRYPOINT [ "python", "calculatrice.py" ]
FROM python:3.11.9-slim

WORKDIR /app

COPY app.py .

RUN pip install mysql-connector-python

ENTRYPOINT [ "python", "app.py" ]
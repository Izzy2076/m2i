FROM python:3.11.9-slim

WORKDIR /app

ENV INPUT_CSV=./data.csv
ENV OUTPUT_JSON=./data.json

COPY . .

ENTRYPOINT [ "python", "app.py" ]

# docker build -t exercice02:1.0 .
# docker run -e INPUT_CSV=./data.csv -e OUTPUT_JSON=./data.json -d exercice02:1.0
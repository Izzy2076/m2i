FROM spark:3.5.7-scala2.12-java17-ubuntu

USER root

RUN apt update && apt upgrade -y
RUN apt install -y python3-pip

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./app /app

USER spark

ENTRYPOINT ["/opt/spark/bin/spark-submit", "--master", "spark://spark-master:7077", "/app/main.py"]
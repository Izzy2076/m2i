ARG PYTHON_VERSION=3.11.9
FROM python:${PYTHON_VERSION}-slim

# ARG -> disponible uniquement au build de l'application
ARG ARG_VERSION=dev

# ENV -> disponible au build ou au runtime
ENV ARG_VERSION=${ARG_VERSION}

WORKDIR /app

COPY . .

ENTRYPOINT [ "python", "app.py" ]

# pour changer les variables d'arg : 
#  docker build -t myapp:1.0 --build-arg PYTHON_VERSION=3.13 .
#  docker build -t myapp:1.0 --build-arg ARG_VERSION=test .

# Pour changer les variables d'environnement :
# docker run -d -e ARG_VERSION=toto myapp:1.0
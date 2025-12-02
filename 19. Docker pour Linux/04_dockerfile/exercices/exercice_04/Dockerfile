FROM node:19-alpine

WORKDIR /app

COPY . .

RUN npm i -g @angular/cli

RUN npm i

ENV NODE_OPTIONS=--openssl-legacy-provider

EXPOSE 4200

ENTRYPOINT ["ng", "serve", "--host", "0.0.0.0"]
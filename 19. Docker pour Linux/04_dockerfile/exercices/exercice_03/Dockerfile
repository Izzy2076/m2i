FROM nginx:1.29.2-alpine-slim

WORKDIR /usr/share/nginx/html

RUN rm -f ./*

RUN apk update && apk upgrade && apk add git

RUN git clone https://github.com/withaarzoo/3D-Rotate-Tube .

EXPOSE 80

ENTRYPOINT ["nginx","-g","daemon off;"]
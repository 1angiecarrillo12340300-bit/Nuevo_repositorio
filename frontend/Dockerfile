FROM nginx:1.20ne

RUN apk update && apk upgrade

COPY index.html /usr/share/nginx/html/index.html
COPY static /usr/share/nginx/html/static

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
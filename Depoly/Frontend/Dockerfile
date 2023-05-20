
FROM nginx:stable-alpine

RUN rm -rf /usr/share/nginx/html/*

# copy
COPY dist /usr/share/nginx/html

# expose 80
EXPOSE 80

# start nginx
CMD ["nginx", "-g", "daemon off;"]

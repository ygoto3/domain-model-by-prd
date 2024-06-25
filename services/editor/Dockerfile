FROM node:22-alpine AS build
ADD . /workspace
WORKDIR /workspace
RUN npm install && npm run build

FROM nginx:latest
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=build /workspace/dist/* /usr/share/nginx/html/
RUN service nginx start

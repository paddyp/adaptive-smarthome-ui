# Create based on ubuntu 22.04 an angular Docker-Container 
FROM --platform=$BUILDPLATFORM ubuntu:22.04
RUN apt update && apt upgrade -y && apt install curl -y && curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh && bash nodesource_setup.sh && apt install nodejs -y 
RUN npm install -g @angular/cli
RUN mkdir app
COPY ./init.sh /app/init.sh
RUN chmod 755 /app/init.sh

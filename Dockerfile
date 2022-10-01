FROM python:3.8-bullseye AS builder
RUN apt-get update

RUN apt install -y postgresql vim libpq-dev  python3-dev

FROM builder AS bakery-backend
COPY backend /app

WORKDIR /app
RUN pip3 install -r requirements.txt

CMD ["sh", "start.sh"]

FROM builder AS bakery-frontend

RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt install -y nodejs
#RUN npm run build

COPY frontend /app
WORKDIR /app

CMD ["npm", "start"]

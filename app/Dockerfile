
FROM python:3.8

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-qqy", "netcat"]

WORKDIR /usr/src

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

ENV HOST="0.0.0.0"
ENV PORT=8000

COPY ./src ./app
RUN pwd
RUN ls
RUN ls app
COPY ./docker-entrypoint.sh ./docker-entrypoint.sh
RUN ["chmod", "+x", "./docker-entrypoint.sh"]
ENTRYPOINT ["./docker-entrypoint.sh"]

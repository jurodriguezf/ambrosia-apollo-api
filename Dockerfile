# syntax=docker/dockerfile:1

FROM python:3.10-alpine

WORKDIR /ambrosia-apollo-api

COPY requirements.txt requirements.txt
RUN apk add build-base
RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
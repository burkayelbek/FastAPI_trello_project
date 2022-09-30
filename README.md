# FastAPI_Case
<hr>

## Requirements in the App

* Python 3.10
* PostgreSQL 14
* Docker
* Redis
* .env file in the project

## Description
This project is built FastAPI microframework with similarity of trello app. 
Apart from these dockerized with the docker application. 

## Installation

Installation easy with docker-compose:

#### Example .env file content:
* POSTGRES_DB=fastapi-basic
* POSTGRES_HOST=postgres
* POSTGRES_USER=fastapi
* POSTGRES_PASSWORD=007007
* POSTGRES_PORT=5432

And after that

```shell
$ docker-compose build
$ docker-compose up
```
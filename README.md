# PatientTracker

# Table of Contents
- [PatientTracker](#mobilehop)
- [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Enviroment variables](#enviroment-variables)
  - [Docker](#docker)
    - [Docker run](#docker-run)
    - [Docker-compose example](#docker-compose-example)

## Description

This service allows you to launch a telegram chatbot to record patients.

## Enviroment variables
- BOT_TOKEN - Auth token for your bot
- DB_LOCATION - Database location
- LOG_FILE_LOCATION - Location of log file

## Docker
### Docker run
```sh
docker-compose up -d --build
```

### Docker stop
```sh
docker-compose down
```

### Docker-compose example
```yml
services:
  patients_tracker:
    build: .
    image: ptracker
    container_name: patients_tracker
    environment:
      BOT_TOKEN: your_bot_token
      DB_LOCATION: ./db/patients.db
      LOG_FILE_LOCATION: ./logs/app.log
      TZ: Europe/Moscow
    volumes:
      - ./db:/app/db
      - ./logs:/app/logs
    restart: always
    labels:
      log_type: "json"
```

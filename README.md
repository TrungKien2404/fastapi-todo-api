# FastAPI Todo API

This project is a Todo API built using FastAPI.

## Features

Level 0
- Basic FastAPI application

Level 4
- Database using SQLAlchemy
- Todo model and CRUD

Level 5
- User authentication
- JWT login system

Level 6
- Deadline for tasks
- Tags
- Overdue tasks
- Today's tasks

## Run project

Install dependencies

pip install -r requirements.txt

Run server

uvicorn app.main:app --reload

Open API docs

http://127.0.0.1:8000/docs

## Run tests

pytest

## Docker

docker build -t todo-api .
docker run -p 8000:8000 todo-api
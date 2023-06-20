# Sophiplabs Recruitment Procees - Django app
_Dev by. **Andrés Peña Diaz**_

## What is this?
This is a Python app that I've developed in order to show off a little bit my skills as
a python programmer, and in this case using Django. The app emulates basically the recruitment
process.

The app has a CRUD, through REST Api, of the three important objects:
- Recruiter
- Candidate
- Interview

This Django project also supports a docker deployment, allowing having a container for Django project
and other for the PostgreSQL service.

## What I have used to built this app?
- Python3
- Django
- PostgreSQL
- REST Api
- Swagger
- Docker

## How to run it locally?

If you want to run the app in .venv, that also supports, in local without using Docker,
follow these steps:

1. Clone this GitHub repository
2. Checkout to `dev` branch
3. Run this command, in the repository/app folder, `python manage.py runserver`.
This will runs Django project in localhost:8000
4. Open `http://localhost:8000/` url in a web browser. This will send you to Swagger where
all the endpoints are exposed.

## How to run it in Docker?

This is also a simple process, so follow these steps:

1. Clone this GitHub repository
2. Checkout to `dev` branch
3. Run this command, in the repository folder, `docker-compose up`
4. Open `http://localhost:8000/` url in a web browser. This will send you to Swagger where
all the endpoints are exposed.




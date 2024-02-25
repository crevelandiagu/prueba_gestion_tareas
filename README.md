# Task Manager

## CI/CD
This use a git workflow with github actions. the project 
has 3 branches: master, develop and feature/HU**
### Test
first github actions run test if this past, it will run the merge with develop
### Build
in this stept we could build a image and pull
### Deploy
in this stept we could deploy a k8s

## Documentation

## docker

```shell
 docker build -t django-python . 
```
when the container is finish

```shell
docker run -p 5000:5000 django-python
```
you must have a Postgres in your local machine and set de env in **.env**

If you aren't a postgres you must use a next docker compose

### docker compose 

You must copy the file **.env.test** and create a file
**.env**

```shell
docker-compose up --build
```

After, you must run a sh file

```shell
sh migrations_test.sh
```
or
```shell
./migrations_test.sh
```

once inside you could run this commands, for the migrate databases

```shell
python manage.py makemigrations
```
```shell
python manage.py migrate
```

### Documentation api 
1. swagger http://127.0.0.1:5000/docs/

### docuemntacion coverage
You can go in this link( is like a sonarcloud)
https://app.codecov.io/gh/crevelandiagu/prueba_gestion_tareas/new

OR
```shell
./migrations_test.sh
```

once inside you could run this commands 

```shell
coverage run manage.py test
```
for show in console the coverage
```shell
coverage report -m
```
for show in html the coverage
```shell
coverage coverage html
```

## Design

The project has two folder the **config** and the app (app_task_manager).

Inside the **config** you find the django config and urls, that was for separate
the configuration and api

Inside the **app_task_manager** you find the python code and urls, that was for separate
the core and for each app you can use a different code for made microservices

About the databases model that was made simple and only used a 1 model and 1 serializer


## Technologies
1. Postman
2. Python
3. Docker
4. Posgres
5. Django 
6. Git
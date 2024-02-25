FROM python:3.10-slim-buster
WORKDIR /django-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV USERS_URL default
ENV DATABASE_URL default
ENV GCP_JSON default

COPY . .

CMD ["python","manage.py", "runserver", "0.0.0.0:5000"]
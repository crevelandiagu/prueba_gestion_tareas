#!/bin/bash

# Buscar la imagen por nombre
image_id=$(docker ps -a | grep "prueba_gestion_tareas_app_task_manager" | awk '{print $1}')

# Validar si se encontró la imagen
if [[ -z "$image_id" ]]; then
  echo "No se encontró la imagen '$image_name'."
  exit 1
fi

# Ejecute docker run con el ID de la imagen
docker exec -it "$image_id" bash

#python manage.py makemigrations
#docker run prueba_gestion_tareas_app_task_manager python manage.py migrate
#docker run prueba_gestion_tareas_app_task_manager coverage run manage.py test
#docker run prueba_gestion_tareas_app_task_manager coverage report -m
#docker run prueba_gestion_tareas_app_task_manager coverage html


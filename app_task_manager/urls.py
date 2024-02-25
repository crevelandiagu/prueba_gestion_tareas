from django.urls import path
from .views import (
    Health,
    AssignmentView,
    create_task,
    AssignmentTranView
)


urlpatterns = [
    path(r'ping/', Health.as_view(), name='health'),
    path(r'task/<int:id_task>', AssignmentView.as_view(), name='get-task'),
    path(r'tasks/', AssignmentView.as_view(), name='get-task'),
    path(r'task/', create_task, name='create-task'),
    path(r'task/<int:id_task>/', AssignmentTranView.as_view(), name='update-task'),
]

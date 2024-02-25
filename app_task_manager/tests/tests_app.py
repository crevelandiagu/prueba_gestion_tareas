import json
from faker import Faker
from django.test import TestCase
from app_task_manager.models import Assignment
from django.test import Client
from app_task_manager.helpers import STATUS


class TestAssignment(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.data_factory = Faker()
        cls.task_fake = {
            "title": cls.data_factory.name(),
            "description": cls.data_factory.name(),
            "status": STATUS[Faker().random_int(0, 3)]
        }

    def test_health_check(self):
        response = Client().get('/api/ping/')
        respon = json.loads(response.content)
        self.assertEqual(respon,{"message": "ok"})

    def test_create_task(self):
        response = Client().post('/api/task/', self.task_fake)
        respon = json.loads(response.content)
        self.assertEqual(respon['success'], True)

    def test_list_tasks(self):
        create_account_1 = Assignment(
            title=self.task_fake['title'],
            description=self.task_fake['description'],
            status=self.task_fake['status']
        )
        create_account_1.save()
        create_account_2 = Assignment(
            title=self.task_fake['title'],
            description=self.task_fake['description'],
            status=self.task_fake['status']
        )
        create_account_2.save()
        response = Client().get('/api/tasks/')
        respon = json.loads(response.content)
        self.assertEqual(len(respon), 2)

    def test_list_task(self):
        create_account_1 = Assignment(
            title=self.task_fake['title'],
            description=self.task_fake['description'],
            status=self.task_fake['status']
        )
        create_account_1.save()
        create_account_2 = Assignment(
            title=self.task_fake['title'],
            description=self.task_fake['description'],
            status=self.task_fake['status']
        )
        create_account_2.save()
        response = Client().get('/api/task/1')
        respon = json.loads(response.content)
        self.assertEqual(len(respon), 0)

    def test_delete_task(self):
        create_account_1 = Assignment(
            title=self.task_fake['title'],
            description=self.task_fake['description'],
            status=self.task_fake['status']
        )
        create_account_1.save()
        response = Client().delete('/api/task/1/')
        respon = json.loads(response.content)
        self.assertEqual(respon['success'], True)
        self.assertEqual(respon['message'], 'Assignment was delete')

    def test_update_task(self):
        create_account_1 = Assignment(
            title=self.task_fake['title'],
            description=self.task_fake['description'],
            status='Nuevo'
        )
        create_account_1.save()
        new_data = {
            'title': self.data_factory.name(),
            'description': self.data_factory.name(),
            'status': 'Completado'
        }
        response = Client().put('/api/task/1/', json.dumps(new_data),content_type='application/json')
        respon = json.loads(response.content)
        self.assertEqual(respon['success'], True)
        self.assertEqual(respon['task']['title'], new_data['title'])

    def test_update_status_task(self):
        create_account_1 = Assignment(
            title=self.task_fake['title'],
            description=self.task_fake['description'],
            status='Nuevo'
        )
        create_account_1.save()
        new_data = {
            'status': 'Completado'
        }
        response = Client().patch('/api/task/1/', json.dumps(new_data),content_type='application/json')
        respon = json.loads(response.content)
        self.assertEqual(respon['success'], True)
        self.assertEqual(respon['task']['status'], new_data['status'])
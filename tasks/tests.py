from django.contrib.auth.models import User
from django.test import Client, TestCase
from .models import Task

class TaskTestCase(TestCase):
    def setUp(self):
        # create test user
        self.username = 'testuser'
        self.password = 'password'
        self.user = User.objects.create_user(username=self.username, password=self.password)

        # log in test user
        self.client = Client()
        self.client.login(username=self.username, password=self.password)


    def test_task_create(self):
        # create a new task
        response = self.client.post('/task-create/', {'title': 'Test Task', 'description': 'Test Description', 'completed': False})

        # check that the task was created
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get(title='Test Task').description, 'Test Description')


    def test_task_edit(self):
        # create a new task
        response = self.client.post('/task-create/', {'title': 'Test Task', 'description': 'Test Description', 'completed': False})

        # edit the task
        task = Task.objects.get(title='Test Task')
        response = self.client.post(f'/task-update/{task.id}/', {'title': 'Updated Test Task', 'description': 'Updated Test Description', 'completed': True})

        # check that the task was edited
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get(title='Updated Test Task').description, 'Updated Test Description')
        self.assertTrue(Task.objects.get(title='Updated Test Task').completed)


    def test_task_delete(self):
        # create a new task
        response = self.client.post('/task-create/', {'title': 'Test Task', 'description': 'Test Description', 'completed': False})

        # delete the task
        task = Task.objects.get(title='Test Task')
        response = self.client.post(f'/task-delete/{task.id}/')

        # check that the task was deleted
        self.assertEqual(Task.objects.count(), 0)


    def test_task_display(self):
        # create a new task
        response = self.client.post('/task-create/', {'title': 'Test Task', 'description': 'Test Description', 'completed': False})

        # view the task
        task = Task.objects.get(title='Test Task')
        response = self.client.get(f'/task/{task.id}/')

        # check that the task data is displayed correctly
        self.assertContains(response, 'Test Task')

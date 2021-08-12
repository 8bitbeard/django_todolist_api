from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from todos.models import Todo


class TodosAPITestCase(APITestCase):

    def create_todo(self):
        sample_todo = {'title': "Hello", 'desc': "Test"}
        response = self.client.post(reverse('todos'), sample_todo)

        return response

    def authenticate(self):
        self.client.post(reverse('register'), { 'username': 'username', 'email': 'email@email.com', 'password': 'password'})
        response = self.client.post(reverse('login'), { 'email': 'email@email.com', 'password': 'password' })
        print(response)
        self.client.credentials (HTTP_AUTHORIZATION = "Bearer {}".format(response.data['token']))


class TestListCreateTodos(TodosAPITestCase):

    def test_should_not_create_todo_with_no_auth(self):
        response = self.create_todo()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_should_create_todo(self):
        previous_todo_count = Todo.objects.all().count()
        self.authenticate()
        response = self.create_todo()
        self.assertEqual(Todo.objects.all().count(), previous_todo_count + 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Hello')
        self.assertEqual(response.data['desc'], 'Test')

    def test_should_retrieve_all_todos(self):
        self.authenticate()
        self.create_todo()
        response = self.client.get(reverse('todos'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['results'], list)
        self.assertIsInstance(response.data['count'], int)
        self.assertEqual(response.data['count'], 1)


class TestTodoDetailAPIView(TodosAPITestCase):

    def test_should_retrive_one_item(self):
        self.authenticate()
        todo_data = self.create_todo()

        response = self.client.get(reverse('todo', kwargs = { 'id': todo_data.data['id'] }))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        todo = Todo.objects.get(id=todo_data.data['id'])

        self.assertEqual(todo.title, response.data['title'])

    def test_should_update_one_item(self):
        self.authenticate()
        todo_data = self.create_todo()

        response = self.client.put(reverse('todo', kwargs = { 'id': todo_data.data['id'] }), {
            "title": "New Title",
            "desc": "New Description",
            "is_complete": True
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_todo = Todo.objects.get(id=todo_data.data['id'])

        self.assertEqual(updated_todo.is_complete, True)
        self.assertEqual(updated_todo.title, response.data['title'])

    def test_should_not_update_when_no_title_is_informed(self):
        self.authenticate()
        todo_data = self.create_todo()

        response= self.client.put(reverse('todo', kwargs = { 'id': todo_data.data['id'] }), {
            "desc": "New Description",
            "is_complete": True
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_should_not_update_when_no_desc_is_informed(self):
        self.authenticate()
        todo_data = self.create_todo()

        response= self.client.put(reverse('todo', kwargs = { 'id': todo_data.data['id'] }), {
            "title": "New Title",
            "is_complete": True
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_should_delete_one_item(self):
        self.authenticate()
        todo_data = self.create_todo()
        prev_db_count = Todo.objects.all().count()

        self.assertGreater(prev_db_count, 0)
        self.assertEqual(prev_db_count, 1)

        response = self.client.delete(reverse('todo', kwargs = { 'id': todo_data.data['id'] }))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        post_db_count = Todo.objects.all().count()

        self.assertEqual(post_db_count, 0)

from common.testing import Play2LiveTestCase
from todo_list.factories import TodoFactory
from rest_framework import status as rest_status
from todo_list.models import Todo


class GetTodoListTestCase(Play2LiveTestCase):

    def test_get_list(self):
        TodoFactory.create(title='test1', is_checked=True)
        TodoFactory.create(title='test2', is_checked=False)

        response = self.client.get('/api/todo_list/list/')  # we use absolute url because we need to see failed test on changes api endpoint
        content_dict = self.content_to_dict(response.content)
        self.assertEquals(len(content_dict), 2)
        self.assertEquals(content_dict[0]['title'], 'test1')
        self.assertEquals(content_dict[0]['is_checked'], True)
        self.assertEquals(content_dict[1]['title'], 'test2')
        self.assertEquals(content_dict[1]['is_checked'], False)

    def test_create_entry(self):
        data = {
            'title': 'test100',
        }
        response = self.client.post('/api/todo_list/entry/', data=data, format="json")
        self.assertEquals(response.status_code, rest_status.HTTP_201_CREATED)
        self.assertEquals(Todo.objects.count(), 1)
        self.assertEquals(Todo.objects.get().title, 'test100')

    def test_edit_entry(self):
        todo_item = TodoFactory.create(title='test1', is_checked=True)
        data = {
            'title': 'test100',
            'is_checked': False,
        }
        response = self.client.put('/api/todo_list/entry/%s/' % todo_item.id, data=data, format="json")
        self.assertEquals(response.status_code, rest_status.HTTP_200_OK)
        self.assertEquals(Todo.objects.get().title, 'test100')
        self.assertEquals(Todo.objects.get().is_checked, False)


    def test_delete_entry(self):
        todo_item = TodoFactory.create(title='test1', is_checked=True)

        response = self.client.delete('/api/todo_list/entry/%s/' % todo_item.id, format="json")
        self.assertEquals(response.status_code, rest_status.HTTP_204_NO_CONTENT)
        self.assertEquals(Todo.objects.count(), 0)

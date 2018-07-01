import json

from django.test import TestCase
from mock import patch

from todo_client.views import TodoClient


def mock_request_get(*args, **kwargs):
    class FakeResponse(object):
        pass

    url = args[0]
    if url == 'http://127.0.0.1:8000/api/todo_list/list/':
        content = json.dumps(
            [{'title': 'test1', 'is_checked': True}, {'title': 'test2', 'is_checked': False}, {'title': 'test3', 'is_checked': False}]
        )
        fake_response = FakeResponse()
        fake_response.content = content
        fake_response.status_code = 200
        return fake_response


class TodoClientTestCase(TestCase):

    def test_ok_get_todo_list(self):
        with patch('todo_client.views.requests.get', new=mock_request_get):
            todo_list = TodoClient().get_list()

        self.assertEquals(len(todo_list), 3)
        self.assertEquals(todo_list[0]['title'], 'test1')

    def test_create_todo_entry(self):
        #TODO: add body here
        pass

    def test_update_todo_entry(self):
        # TODO: add body here
        pass

    def test_delete_todo_entry(self):
        # TODO: add body here
        pass
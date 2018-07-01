import json

import requests
from django.conf import settings


class TodoClient(object):

    def __init__(self):
        self.host = settings.TODO_HOST

    def _content_to_dict(self, content):
        return json.loads(content)

    def _get_url_content_as_dict(self, url):
        response = requests.get(url)
        if response.status_code == requests.codes.ok:
            content = response.content
            return self._content_to_dict(content)

    def get_list(self):
        tail = '/api/todo_list/list/'
        url = 'http://%s%s' % (self.host, tail)
        return self._get_url_content_as_dict(url)


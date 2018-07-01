import json

from rest_framework.test import APITestCase, APIClient


class CommonTestCaseMixin(object):
    user = None

    def login_as(self):
        # TODO: add login functionality here
        return self.user

    def content_to_dict(self, content):
        return json.loads(content)


class Play2LiveTestCase(APITestCase, CommonTestCaseMixin):
    client_class = APIClient

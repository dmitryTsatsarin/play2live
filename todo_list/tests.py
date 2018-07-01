from common.testing import Play2LiveTestCase
from todo_list.factories import TodoFactory


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

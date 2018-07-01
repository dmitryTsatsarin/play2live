from common.views import Play2LiveGenericView
from todo_list.models import Todo
from todo_list.serializers import GetTodoListSerializer


class GetTodoListView(Play2LiveGenericView):
    serializer_class = GetTodoListSerializer

    def get_queryset(self):
        return Todo.objects.filter()  # TODO: add some filtration by user

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

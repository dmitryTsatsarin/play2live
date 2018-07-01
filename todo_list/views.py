from common.views import Play2LiveGenericView
from todo_list.models import Todo
from todo_list.serializers import GetTodoListSerializer, CreateTodoSerializer, UpdateDeleteTodoSerializer


class GetTodoListView(Play2LiveGenericView):
    serializer_class = GetTodoListSerializer

    def get_queryset(self):
        return Todo.objects.filter()  # TODO: add some filtration by user

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CreateTodoView(Play2LiveGenericView):
    serializer_class = CreateTodoSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UpdateDeleteTodoView(Play2LiveGenericView):
    serializer_class = UpdateDeleteTodoSerializer

    def get_queryset(self):
        return Todo.objects.filter()  # TODO: add some filtration by user

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

import factory

from todo_list.models import Todo


class TodoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Todo

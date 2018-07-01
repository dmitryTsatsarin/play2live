from rest_framework.serializers import ModelSerializer

from todo_list.models import Todo


class GetTodoListSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'is_checked']


class CreateTodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title',]


class UpdateDeleteTodoSerializer(GetTodoListSerializer):
    pass


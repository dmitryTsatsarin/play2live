# Register your models here.
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from todo_list.models import Todo


class TodoList(ModelAdmin):
    pass


admin.site.register(Todo, TodoList)

from django.urls import path

from todo_list import views

urlpatterns = [
    path('list/', views.GetTodoListView.as_view()),
]

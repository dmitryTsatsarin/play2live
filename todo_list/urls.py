from django.urls import path

from todo_list import views

urlpatterns = [
    path('list/', views.GetTodoListView.as_view()),
    path('entry/<int:id>/', views.UpdateDeleteTodoView.as_view()),
    path('entry/', views.CreateTodoView.as_view()),
]

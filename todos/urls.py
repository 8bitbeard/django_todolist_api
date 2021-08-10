# from todos.views import CreateTodoAPIView, TodoListAPIView
from todos.views import TodoAPIView, TodoDetailAPIView
from django.urls import path


urlpatterns = [
    path('', TodoAPIView.as_view(), name='todos'),
    path('<int:id>', TodoDetailAPIView.as_view(), name='todo'),
    # path('create', CreateTodoAPIView.as_view(), name='create-todo'),
    # path('list', TodoListAPIView.as_view(), name='list-todo'),
]
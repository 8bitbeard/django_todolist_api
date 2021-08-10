from todos.serializers import TodoSerializer
from todos.models import Todo
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from authentication.jwt import JWTAuthentication


class TodoAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)


# class CreateTodoAPIView(CreateAPIView):
#     serializer_class = TodoSerializer

#     authentication_classes = [JWTAuthentication]

#     permission_classes=(IsAuthenticated,)
#     # permission_classes=[JWTAuthentication]

#     def perform_create(self, serializer):
#         return serializer.save(owner=self.request.user)


# class TodoListAPIView(ListAPIView):
#     serializer_class = TodoSerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes=(IsAuthenticated,)


#     def get_queryset(self):
#         return Todo.objects.filter(owner=self.request.user)
from todos.serializers import TodoSerializer
from todos.models import Todo
from rest_framework import filters
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from authentication.jwt import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from todos.pagination import CustomPageNumberPagination


class TodoAPIView(ListCreateAPIView):

    serializer_class = TodoSerializer
    pagination_class = CustomPageNumberPagination
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id', 'title', 'desc', 'is_complete']
    search_fields = ['id', 'title', 'desc', 'is_complete']
    ordering_fields = ['id', 'title', 'desc', 'is_complete']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = TodoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

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
from django.shortcuts import render, HttpResponse
from rest_framework import generics, permissions
from .serializers import *
from mainapp.models import ToDoList
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# import re
from rest_framework_extensions.mixins import NestedViewSetMixin

# list all tasks
class ListToDo(generics.ListAPIView):
    queryset = ToDoList.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

# PUT
class Detailview(generics.RetrieveUpdateAPIView):
    queryset = ToDoList.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

# Create Task
class Createview(generics.CreateAPIView):
    queryset = ToDoList.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
     

# Delete task
class Deleteview(generics.DestroyAPIView):
    queryset = ToDoList.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

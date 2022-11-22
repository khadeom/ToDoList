from django.shortcuts import render, HttpResponse
from rest_framework import generics, permissions
from .serializers import *
from mainapp.models import ToDoList
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# import re

class ListToDo(generics.ListAPIView):
    queryset = ToDoList.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = ToDoListSerializers
   
class Detailview(generics.RetrieveUpdateAPIView):
    queryset = ToDoList.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = ToDoListSerializers


class Createview(generics.CreateAPIView):
    queryset = ToDoList.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = ToDoListSerializers
     

    # def get(self, request, *args, **kwargs):
    #     return Response("he ha")


class Deleteview(generics.DestroyAPIView):
    queryset = ToDoList.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = ToDoListSerializers

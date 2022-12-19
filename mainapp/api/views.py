from rest_framework import generics, permissions
from .serializers import *
from mainapp.models import ToDoList
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# list all tasks
class ListToDo(generics.ListAPIView):
    queryset = ToDoList.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

# PUT
class Detailview(generics.RetrieveUpdateAPIView):
    queryset = ToDoList.objects.all()
    # authentication_classes = [SessionAuthentication,BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # def update(self, request, *args, **kwargs):
    #     request.data.update({'voucherrows': json.loads(request.data.pop('voucherrows', None))})
    #     return super().update(request, *args, **kwargs)

# Create Task
class Createview(generics.CreateAPIView):
    queryset = ToDoList.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer


# Delete task
class Deleteview(generics.DestroyAPIView):
    queryset = ToDoList.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

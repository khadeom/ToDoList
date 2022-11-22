from rest_framework import serializers
from taggit_serializer.serializers import TaggitSerializer,TagListSerializerField
from mainapp.models import *
import six
import json

# class TagsSerializerField(serializers.CharField):
#     child = serializers.CharField()

#     def to_representation(self, data):
#         return data.replace(","," ").split(" ")

class ToDoListSerializers(serializers.ModelSerializer):
    tags = TagListSerializerField()
    
    class Meta:
        model = ToDoList
        fields = ("id", "title", "description", "due_date", "tags", "status")

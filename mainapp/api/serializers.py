from rest_framework import serializers
from taggit_serializer.serializers import TaggitSerializer
from mainapp.models import *
import six
import json

class TagsSerializerField(serializers.CharField):
    child = serializers.CharField()

    def to_representation(self, data):
        return data.replace(","," ").split(" ")

class ToDoListSerializers(TaggitSerializer, serializers.ModelSerializer):
    tags = TagsSerializerField(required=False)
    
    class Meta:
        model = ToDoList
        fields = ("id", "title", "description", "due_date", "tags", "status")

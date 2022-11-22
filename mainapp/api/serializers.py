from rest_framework import serializers
from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField
from mainapp.models import *
import six
import json



class TagsSerializerField(serializers.ListField):
    child = serializers.CharField()

    def to_representation(self, data):
        return data.values_list("name", flat=True)


class ToDoListSerializers(TaggitSerializer, serializers.ModelSerializer):
    tags = TagsSerializerField(required=False)

    class Meta:
        model = ToDoList
        fields = ("id", "title", "description", "due_date", "tags", "status")

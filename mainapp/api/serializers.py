from rest_framework import serializers
from taggit_serializer.serializers import TaggitSerializer,TagListSerializerField
from mainapp.models import *
from django.utils import timezone


class TaskSerializer(serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        lookup_field = 'id'
        model = ToDoList
        fields =("id", "title", "description", "due_date",
                     "tags", "status","timestamp") 
        read_only_fields = ('id', 'timestamp')
    
    def validate_due_date(self, value):
        if (timezone.now().date() > value):
            raise serializers.ValidationError('deadline must be in the future.')
        return value


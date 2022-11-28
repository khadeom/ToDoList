from rest_framework import serializers
# from taggit_serializer.serializers import TaggitSerializer,TagListSerializerField
from mainapp.models import *
from django.utils import timezone
import json

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        lookup_field = 'id'
        model = ToDoList
        fields =("id", "title", "description", "due_date",
                    "tags", "status","timestamp")
        read_only_fields = ('id', 'timestamp')


    def create(self, validated_data):
        tags = validated_data.pop('tags')
        print(tags)
        task = ToDoList.objects.create(**validated_data)

        for tag in tags:
            print(tag)
            if Tag.objects.filter(name = tag):
                pass
            else:
                Tag.objects.create(todolist=task, **tag)

        return task

    def validate_due_date(self, value):
        if (timezone.now().date() > value):
            raise serializers.ValidationError('deadline must be in the future.')
        return value


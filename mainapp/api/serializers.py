from rest_framework import serializers
# from taggit_serializer.serializers import TaggitSerializer,TagListSerializerField
from mainapp.models import *
from django.utils import timezone
import json

# 



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'id'
        model = ToDoList
        fields =("id", "title", "description", "due_date",
                    "tags", "status","timestamp") 
        read_only_fields = ('id', 'timestamp')

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        print("tah",tags_data)
        instance = ToDoList.objects.create(**validated_data)
        instance.tags = json.dumps(list(set((map(lambda a:a.strip(), tags_data.split(","))))))
        instance.save()
    
        return instance 

    def update(self, instance, validated_data):
        tag_names = validated_data.pop('tags')
        instance = super().update(instance, validated_data)
        
        instance.tags = json.dumps(list(set(json.loads(tag_names))))
        instance.save()    
        return instance

    def validate_due_date(self, value):
        if (timezone.now().date() > value):
            raise serializers.ValidationError('deadline must be in the future.')
        return value


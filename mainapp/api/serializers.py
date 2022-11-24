from rest_framework import serializers
# from taggit_serializer.serializers import TaggitSerializer,TagListSerializerField
from mainapp.models import *
from django.utils import timezone


class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = "__all__"

    def create(self, validated_data):
        tag = Tags.objects.get_or_create(**validated_data)
        return tag

    def to_representation(self, instance):
        ret = super(TagsSerializer, self).to_representation(instance)
        data = dict()
        data['name'] = ret['name']
        return data 



class TaskSerializer(serializers.ModelSerializer):
    tags = TagsSerializer()
    class Meta:
        lookup_field = 'id'
        model = ToDoList
        fields =("id", "title", "description", "due_date",
                    "tags", "status","timestamp") 
        read_only_fields = ('id', 'timestamp')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'] = TagsSerializer(many=True, required=False, context=self.context)

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        print("tah",tags_data)
        todo = ToDoList.objects.create(**validated_data)
        for tag in tags_data:
            t,_= Tags.objects.get_or_create(name=tag["name"])
            print("Ye ky",t)
            todo.tag_list.add(t)    #set than add
        return todo 



    def validate_due_date(self, value):
        if (timezone.now().date() > value):
            raise serializers.ValidationError('deadline must be in the future.')
        return value


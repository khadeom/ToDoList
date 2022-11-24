from django.db import models
from taggit.managers import TaggableManager
import uuid

class Tags(models.Model):
    # id = models.CharField(_(u'id'), max_length=128, primary_key=True)
    name = models.CharField(max_length=50)



class ToDoList(models.Model):

    status_choices = [
            ("O", "OPEN"), 
            ("W", "WORKING"), 
            ("D", "DONE"), 
            ("v", "OVERDUE")
    ]

    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    due_date = models.DateField(blank=True)
    # tags = TaggableManager(blank=True)
    tag_list = models.ManyToManyField('Tags',related_name="tag")
    status = models.CharField(max_length=2, default="O", choices=status_choices)
    
    def __str__(self):
        return self.title



# {
#     "title": "Om Khade2",
#     "description": "tags Test",
#     "due_date": "2023-11-11",
#     "tags": [{"name":"testtag1"},{"name":"testtag2"},{"name":"testtag3"}],
#     "status": "O"
# }


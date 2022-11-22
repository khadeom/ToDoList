from django.db import models
from taggit.managers import TaggableManager
import uuid


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
    tags = TaggableManager(blank=True)
    status = models.CharField(max_length=2, default="O", choices=status_choices)
    
    def __str__(self):
        return self.title



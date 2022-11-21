from django.db import models
from taggit.managers import TaggableManager
import uuid


class ToDoList(models.Model):

    status_choices = [("O", "OPEN"), ("W", "WORKING"), ("D", "DONE"), ("v", "OVERDUE")]
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    due_date = models.DateField(blank=True)
    tags = TaggableManager(blank=True)

    status = models.CharField(max_length=2, default="O", choices=status_choices)
    # status2 = models.CharField(max_length=2, default="O", choices=status_choices)

    def is_status(self):
        return self.Status in {self.JUNIOR, self.SENIOR}

    def __str__(self):
        return self.title


# # Create your models here.
# class ToDoList(models.Model):

#     status_choices = [("O", "OPEN"), ("W", "WORKING"), ("D", "DONE"), ("v", "OVERDUE")]

#     timestamp = models.DateTimeField(auto_now_add=True, editable=False)
#     title = models.CharField(max_length=100, blank=False)
#     description = models.TextField(max_length=1000, blank=False)
#     due_date = models.DateField(blank=True)
#     # tags = TaggableManager(blank=True)
#     tags = models.ManyToManyField("Tag", related_name="TaggedModel")
#     status = models.CharField(max_length=2, default="O", choices=status_choices)

#     def is_status(self):
#         return self.Status in {self.JUNIOR, self.SENIOR}

#     def __str__(self):
#         return self.Title

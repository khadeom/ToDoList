from django.contrib import admin
from .models import ToDoList

# @admin.action(description='Mark selected task as done')
# def mark_done(modeladmin, request, queryset):
#     queryset.update(status='D')

# class ToDoListAdmin(admin.ModelAdmin):
#     list_display = [
#         "id", 
#         "timestamp", 
#         "title",
#         "description",
#         "due_date",
#         "tag_list",
#         "status"
#     ]
    
#     ordering = ['timestamp']
#     actions = [mark_done]


#     def get_queryset(self, request):
#         return super().get_queryset(request).prefetch_related('tag_list')

#     def tag_list_list(self, obj):
#         return u", ".join(o.name for o in obj.tags.all())
#     search_fields = ('title',)

# admin.site.register(ToDoList, ToDoListAdmin)
admin.site.register(ToDoList)


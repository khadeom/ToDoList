from django.contrib import admin
from .models import ToDoList

@admin.action(description='Mark selected task as done')
def mark_done(modeladmin, request, queryset):
    queryset.update(status='D')

class ToDoListAdmin(admin.ModelAdmin):
    list_display = ["id", "timestamp", "title", "description", "due_date", "tag_list", "status"]
    # list_display = ["tags_list"]
    ordering = ['timestamp']
    actions = [mark_done]


    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
    # fieldsets = (

    #     (None, {'fields': ("timestamp", "title", "description", "due_date", "tags", "status")}),
    #     ('Personal info', {'fields': ('username')}),
    #     ('Permissions', {'fields': ('is_admin','is_staff')}),
    # )

    search_fields = ('title',)

admin.site.register(ToDoList, ToDoListAdmin)

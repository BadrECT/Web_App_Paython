from django.contrib import admin
from .models import Project, Task, Comment, TimeLog

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'manager', 'priority', 'status', 'start_date', 'end_date']
    list_filter = ['priority', 'status', 'start_date']
    search_fields = ['name', 'description']
    filter_horizontal = ['team_members']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'assigned_to', 'priority', 'status', 'due_date']
    list_filter = ['priority', 'status', 'due_date']
    search_fields = ['title', 'description']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['task', 'author', 'created_at']
    list_filter = ['created_at']

@admin.register(TimeLog)
class TimeLogAdmin(admin.ModelAdmin):
    list_display = ['task', 'user', 'date', 'hours']
    list_filter = ['date']
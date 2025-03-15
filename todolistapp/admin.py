from django.contrib import admin
from .models import Taskers , Task
# Register your models here.

@admin.register(Taskers)
class TaskerAdmin(admin.ModelAdmin):
    list_display = ('username','email','created_at')
    search_fields = ('username','email') #enables search function

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','completed','created_at','tasker')
    search_fields = ('title','completed','tasker__username')
    list_filter = ('completed','tasker__username')
    autocomplete_fields = ('tasker',) # dropdown showing taskers


























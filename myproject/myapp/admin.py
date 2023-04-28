from django.contrib import admin

# Register your models here.
from myapp.models import *
class MyModelAdmin(admin.ModelAdmin):
    # Customize the admin interface for this model
    list_display = ['name']

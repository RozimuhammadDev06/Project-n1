from django.contrib import admin
from .models import Oquvchi,new

# Register your models here.

@admin.register(new)
class OquvchiAdmin(admin.ModelAdmin):
    pass



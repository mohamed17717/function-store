from django.contrib import admin

# Register your models here.
from .models import Function, Tag

admin.site.register(Function)
admin.site.register(Tag)

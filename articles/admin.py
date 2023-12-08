# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Articles)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
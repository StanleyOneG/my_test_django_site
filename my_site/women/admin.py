from django.contrib import admin
from . models import *

# Register your models here.

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_created', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)  # Обязательно ставить запятую, т.к. это кортеж
    list_filter = ('is_published', 'time_created')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)  # обязательно ставить запятую, т.к. это должен быть кортеж
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)

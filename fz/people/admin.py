from django.contrib import admin
from .models import People

class PeopleAdmin(admin.ModelAdmin):
    list_display = ("name","title","interest","rsdirection")
    ordering = ('rsdirection',)
    list_filter =('rsdirection',) #过滤器
    search_fields =('name', 'title', 'rsdirection') #搜索字段
admin.site.register(People,PeopleAdmin)
# Register your models here.

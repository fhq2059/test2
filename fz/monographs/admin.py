from django.contrib import admin
from .models import Monographs

class MonographsAdmin(admin.ModelAdmin):
    list_display = ("name","subject","publishing","time")
    list_filter =( 'publishing', 'time',) #过滤器
    search_fields =('name', 'subject', 'publishing') #搜索字段
admin.site.register(Monographs,MonographsAdmin)
# Register your models here.

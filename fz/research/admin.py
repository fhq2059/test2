from django.contrib import admin
from .models import Research

class ResearchAdmin(admin.ModelAdmin):
    list_display = ("name","orientation","time","rank")
    list_filter =('orientation', 'rank', ) #过滤器
    search_fields =('name', 'orientation', 'time','rank') #搜索字段
admin.site.register(Research,ResearchAdmin)
# Register your models here.

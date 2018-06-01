from django.contrib import admin
from .models import Awards

class AwardAdmin(admin.ModelAdmin):
    list_display = ("time","awardname","projectname","company","role")

    list_filter =('time', 'company', ) #过滤器
    search_fields =('awardname', 'projectname', 'company') #搜索字段
admin.site.register(Awards,AwardAdmin)
# Register your models here.

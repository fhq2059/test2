from django.contrib import admin
from .models import Adactivaty

class AdcativatyAdmin(admin.ModelAdmin):
    list_display = ("title","image","year")

    list_filter =('year',) #过滤器
    search_fields =('title',) #搜索字段

admin.site.register(Adactivaty,AdcativatyAdmin)
# Register your models here.

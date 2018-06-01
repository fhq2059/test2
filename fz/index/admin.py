from django.contrib import admin
from .models import Paper,Rsdirection,Active

class PaperAdmin(admin.ModelAdmin):
    list_display =("title","body","publish")

    search_fields = ('body', 'title',)  # 搜索字段
    date_hierarchy = 'publish'  # 详细时间分层筛选　
    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all.js',
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js'
        )
admin.site.register(Paper,PaperAdmin)

class RsdirectionAdmin(admin.ModelAdmin):
    list_display = ("title","body")
    search_fields = ('title',)  # 搜索字段

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all.js',
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js'
        )
admin.site.register(Rsdirection,RsdirectionAdmin)

class ActiveForm(admin.ModelAdmin):
    list_display = ("title","body","publish")
    search_fields = ('title', )  # 搜索字段
    date_hierarchy = 'publish'  # 详细时间分层筛选　

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all.js',
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js'
        )
admin.site.register(Active,ActiveForm)
# Register your models here.
admin.site.site_header = '纺织企业管理信息中心后台管理'

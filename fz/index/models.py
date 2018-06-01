from django.db import models
from django.utils import timezone
from filer.fields.image import FilerImageField

class Paper(models.Model):
    title = models.CharField('题目',max_length=300)
    body = models.TextField('内容')
    publish = models.DateTimeField('出版时间',default=timezone.now)
    class Meta:
        ordering = ("-publish",)
        verbose_name = '论文'
        verbose_name_plural = '论文'
    def __str__(self):
        return self.title

class Rsdirection(models.Model):
    title = models.CharField('名字',max_length=300)
    body = models.TextField('描述')
    image = FilerImageField(verbose_name = '图片',related_name='rsdirection_image', null=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '研究方向'
        verbose_name_plural = '研究方向'

class Active(models.Model):
    title = models.CharField('标题',max_length=300)
    body = models.TextField('内容')
    publish = models.DateTimeField('时间',default=timezone.now)
    image = FilerImageField(verbose_name = '图片',related_name='active_image', null=True)
    class Meta:
        ordering = ("-publish",)
        verbose_name = '活动'
        verbose_name_plural = '活动'
    def __str__(self):
        return self.title
# Create your models here.

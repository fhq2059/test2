from django.db import models
from django.utils import timezone


class Research(models.Model):
    name = models.CharField('项目名称',max_length=200)
    orientation = models.CharField('研究方向',max_length=200,blank=True)
    time = models.CharField('起止时间',max_length=200,blank=True)
    projectorigin = models.CharField('项目来源',max_length=200,blank=True)
    rank = models.CharField('级别',max_length=200,blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '科研项目'
        verbose_name_plural = '科研项目'


# Create your models here.

from django.db import models

class Monographs(models.Model):
    name = models.CharField('姓名',max_length=300)
    subject =  models.CharField('题目',max_length=300)
    publishing = models.CharField('出版社',max_length=300,blank=True)
    time = models.CharField('时间',max_length=300,blank=True)

    class Meta:
        verbose_name = '论文及专著'
        verbose_name_plural = '论文及专著'

    def __str__(self):
        return self.name
# Create your models here.

from django.db import models


class Awards(models.Model):
    time = models.CharField('获奖时间',max_length=300)
    awardname = models.CharField('获奖名称',max_length=300,blank=True)
    projectname = models.CharField('项目名称',max_length=300,blank=True)
    company = models.CharField('颁奖单位',max_length=300,blank=True)
    role = models.CharField('角色',max_length=300,blank=True)

    class Meta:
        verbose_name = '成果获奖'
        verbose_name_plural = '成果获奖'

    def __str__(self):
        return self.projectname
# Create your models here.

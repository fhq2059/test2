from django.db import models
from index.models import Rsdirection
from filer.fields.image import FilerImageField

class People(models.Model):
    name = models.CharField('姓名',max_length=300)
    title = models.CharField('职称',max_length=300,blank=True)
    interest = models.CharField('研究兴趣',max_length=300,blank=True)
    rsdirection = models.ForeignKey(Rsdirection,verbose_name = '方向',on_delete=models.CASCADE)
    image = FilerImageField(verbose_name ='照片',related_name='people_image',null=True)

    class Meta:
        verbose_name = '人员'
        verbose_name_plural = '人员'

    def __str__(self):
        return self.name
# Create your models here.

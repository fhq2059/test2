from django.db import models
from filer.fields.image import FilerImageField

class Adactivaty(models.Model):
    title = models.CharField('标题',max_length=300)
    image = FilerImageField(verbose_name = '图片',related_name='adactivaty_image',null=True)
    year = models.CharField('年份',max_length=300,blank=True)

    class Meta:
        verbose_name = '学术活动'
        verbose_name_plural = '学术活动'

    def __str__(self):
        return self.title
# Create your models here.

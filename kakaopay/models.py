from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.

class Goods(models.Model):
    goods_name = models.CharField(max_length=1000,null=False,blank=False)
    goods_introduction = RichTextUploadingField(blank=True,null=True)
    goods_code = models.PositiveIntegerField(primary_key=True,auto_created=True)
    stock = models.IntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.goods_name



from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models

# Create your models here.

class Goods(models.Model):
    goods_name = models.CharField(max_length=1000,null=False,blank=False)
    goods_introduction = RichTextUploadingField(blank=True,null=True)
    stock = models.IntegerField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey(settings.CATEGORY_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.goods_name

    class Meta:
        verbose_name_plural = 'Goods'

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods,on_delete=models.PROTECT)
    order_time = models.DateTimeField(auto_now_add=True)




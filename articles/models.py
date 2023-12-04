from django.conf import settings
from django.db import models

# Create your models here.

class Articles(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='articles')
    upload_time = models.DateTimeField(auto_now_add=True)
    revise_time = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=50000)
    image = models.ImageField(upload_to='articles/images/%Y/%m/%d',blank=True,null=True)

class Comment(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='comment')
    upload_time = models.DateTimeField(auto_now_add=True)
    revise_time = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=1000)
    Articles = models.ForeignKey(Articles,on_delete=models.CASCADE,related_name='articles')


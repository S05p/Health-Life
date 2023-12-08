from django.conf import settings
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True,default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Articles(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='articles')
    upload_time = models.DateTimeField(auto_now_add=True)
    revise_time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50,default=None)
    content = RichTextUploadingField(blank=True,null=True)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_articles')
    unlike_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='unlike_articles')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')

class Comment(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='comment')
    upload_time = models.DateTimeField(auto_now_add=True)
    revise_time = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=1000)
    Articles = models.ForeignKey(Articles,on_delete=models.CASCADE,related_name='articles')
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_comments')




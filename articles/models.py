from django.conf import settings
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Articles(models.Model):
    Category_Choices = [
        ('big three exercises ', '3대운동'),
        ('Lean Mass Up', '린매스업'),
        ('cardio', '유산'),
        ('bodybilding', '보디빌딩'),
        ('diet', '식단'),
        ('freedom', '자유'),
    ]
    User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='articles')
    upload_time = models.DateTimeField(auto_now_add=True)
    revise_time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50,default=None)
    content = RichTextUploadingField(blank=True,null=True)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_articles')
    category = models.CharField(choices=Category_Choices,blank=False,null=False,max_length=20,default='')

class Comment(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='comment')
    upload_time = models.DateTimeField(auto_now_add=True)
    revise_time = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=1000)
    Articles = models.ForeignKey(Articles,on_delete=models.CASCADE,related_name='articles')
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_comments')

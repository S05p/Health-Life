from django.conf import settings
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


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
    comment_count = models.IntegerField(default=0)

class Comment(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='comment')
    upload_time = models.DateTimeField(auto_now_add=True)
    revise_time = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=1000)
    articles = models.ForeignKey(Articles,on_delete=models.CASCADE,related_name='articles')
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_comments')


# 댓글 카운트를 위한 함수
@receiver(post_save, sender=Comment)
@receiver(post_delete, sender=Comment)
def update_comment_count(sender, instance, **kwargs):
    article = instance.articles
    article.comment_count = Comment.objects.filter(articles=article).count()
    article.save()


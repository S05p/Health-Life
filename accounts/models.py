from django.contrib.auth.models import AbstractUser
from django.db import models
import json
# Create your models here.

class Hobby(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Hobbies'
class User(AbstractUser):
    username = models.CharField(max_length=20,blank=False,null=False,unique=True)
    nickname = models.CharField(max_length=15,blank=False,null=False,unique=True)
    level = models.IntegerField(default=0)
    # 이름,닉네임,레벨... 말고 또 뭐가 있지
    invited_Day = models.DateField(auto_now_add=True)
    profile_image = models.ImageField(upload_to='user/images/%Y/%m/%d',blank=True,null=True)
    email = models.EmailField(blank=False,null=False,unique=True)
    hobbies = models.ManyToManyField(Hobby,related_name='hobbies')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','nickname',]
    def __str__(self):
        return self.nickname


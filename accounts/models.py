from django.contrib.auth.models import AbstractUser
from django.db import models
import json
# Create your models here.

class User(AbstractUser):
    username = models.TextField(blank=False,null=False,unique=False)
    nickname = models.TextField(blank=False,null=False,unique=True)
    level = models.IntegerField(default=0)
    # 이름,닉네임,레벨... 말고 또 뭐가 있지
    invited_Day = models.DateField(auto_now_add=True)
    profile_image = models.ImageField(upload_to='user/images/%Y/%m/%d',blank=True,null=True)
    email = models.EmailField(blank=False,null=False,unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','nickname',]
    def __str__(self):
        return self.nickname
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    Hobbiy_Choices = [
        ('big three exercises ', '3대운동'),
        ('cycling', '싸이클'),
        ('bodyWeight_training', '맨몸운동'),
        ('bodybilding', '보디빌딩'),
        ('jogging', '조깅'),
        ('running', '러닝'),
        ('swimming', '수영'),
        ('WeightTraining', '웨이트트레이닝'),
        ('Yoga', '요가'),
        ('Pilates', '필라테스'),
        ('climbing', '클라이밍'),
        ('tennis', '테니스'),
    ]
    username = models.TextField(blank=False,null=False,unique=False)
    nickname = models.TextField(blank=False,null=False,unique=True)
    level = models.IntegerField(default=0)
    # 이름,닉네임,레벨... 말고 또 뭐가 있지
    invited_Day = models.DateField(auto_now_add=True)
    profile_image = models.ImageField(upload_to='user/images/%Y/%m/%d',blank=True,null=True)
    hobbies = models.CharField(max_length=20,choices=Hobbiy_Choices,blank=True,null=True,verbose_name='취미')
    email = models.EmailField(blank=False,null=False,unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','nickname',]
    def __str__(self):
        return self.nickname
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    region = models.CharField(max_length=200)
    phone_number = models.IntegerField(null=True)

    def __str__(self):
        return self.username

    class Meta: # 권한 명, 사용자에게 보여질 권한 이름
        permissions = [('gold_member', 'Gold member'),
                       ('silver_member', 'Silver member')]

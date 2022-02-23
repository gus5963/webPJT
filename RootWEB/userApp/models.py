from django.db import models

# Create your models here.

class WebUser(models.Model):
    user_id = models.CharField(max_length=10)
    user_pwd = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    user_point = models.IntegerField(default=0)
    user_regdate = models.DateTimeField(auto_now=True)

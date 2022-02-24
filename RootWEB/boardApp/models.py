from django.db import models

# Create your models here.
class WebBoard(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=50)
    content = models.TextField()
    regdate = models.DateField(auto_now=True)
    viewcnt = models.IntegerField(default=0)
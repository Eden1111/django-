from django.db import models

# Create your models here.

class messages(models.Model):
    user = models.CharField('姓名',max_length=10000000)
    subject = models.CharField('主題',max_length=10000000)
    content = models.TextField('內容')
    cterted = models.DateTimeField('留言時間',auto_now_add=True)

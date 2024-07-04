from django.db import models

# Create your models here.

class Message(models.Model):
    user = models.CharField('姓名',max_length=10000000)
    subject = models.CharField('主題',max_length=10000000)
    content = models.TextField('內容')
    created = models.DateTimeField('留言時間',auto_now_add=True)
#建立資料模型 user=名字 subject=主題 context=內容 created=留言時間
    
    def __str__(self):
        return self.subject #定義__str__
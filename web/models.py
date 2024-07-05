from django.db import models

# Create your models here.

#class 資料庫名稱(models.Model) 創建django內建的資料庫類型
class Message(models.Model): 
    user = models.CharField('姓名',max_length=10000000000000000000000000000000)
    subject = models.CharField('主題',max_length=100000000000000000000000000000)
    content = models.TextField('內容')
    created = models.DateTimeField('留言時間',auto_now_add=True)
#建立資料模型 user=名字 subject=主題 context=內容 created=留言時間 此資料庫有四個欄位
    
    def __str__(self):
        return self.subject,self.content,self.user,self.created #定義__str__ (會在object裡面，可以.user等) 
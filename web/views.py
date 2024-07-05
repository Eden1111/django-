from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin #檢測用戶是否登入

# Create your views here.

#ListView、DetailView、CreateView、DeleteView會開啟在app名/template/app名/對應的.html

#留言列表
class MessageList(ListView):
    model = Message
    ordering = ['-id'] #以id值反向排序
#留言內容
class MessageView(DetailView):
    model = Message
#創建留言
class MessageCreate(CreateView):
    model = Message
    fields = ['user', 'subject', 'content'] #顯示'user','subject','content'
    success_url = reverse_lazy('msg_list') #新增後導向留言列表(/message)
# 刪除留言
class MessageDelete(LoginRequiredMixin,DeleteView): #LoginRequiredMixin需要登入
    model = Message
    success_url = reverse_lazy('msg_list') #刪除後導向留言列表(/message)
#修改留言
class MessageUpdate(LoginRequiredMixin,UpdateView): #修改留言
    model = Message
    fields=['subject', 'content'] #顯示'content'
    success_url = reverse_lazy('msg_list') #修改後導向留言列表(/message)
    template_name = 'message_update.html' #修改要被展示的html檔案
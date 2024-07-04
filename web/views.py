from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin #檢測用戶是否登入

# Create your views here.

class MessageList(ListView):
    model = Message
    ordering = ['-id'] #以id值反向排序
class MessageView(DetailView):
    model = Message
class MessageCreate(CreateView):
    model = Message
    fields = ['user', 'subject', 'content'] #顯示'user','subject','content'
    success_url = reverse_lazy('msg_list')#新增後導向留言列表(/message)
# 刪除留言
class MessageDelete(LoginRequiredMixin,DeleteView):#LoginRequiredMixin需要登入
    model = Message
    success_url = reverse_lazy('msg_list')#刪除後導向留言列表(/message)
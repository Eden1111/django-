from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *

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

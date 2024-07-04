from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *

# Create your views here.

def MessageList(ListView):
    models = messages
    ordering = ['-id']
def MessageViews(DetailView):
    models=messages
def MessageCreat(CreateView):
    CreateView
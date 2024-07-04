from django.urls import path
from .views import *

urlpatterns=[
    path('',MessageList.as_view(),name='msg_list'),
    path('<ink:pk>/',MessageViews.as_view(),name='msg_view'),
    path('creat/',MessageCreat.as_view(),name='msg_creat'),

]
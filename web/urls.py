from django.urls import path
from .views import *

urlpatterns=[
    path('', MessageList.as_view(), name='msg_list'),#空路徑(/message) 留言列表
    path('<int:pk>/', MessageView.as_view(), name='msg_view'),#
    path('create/', MessageCreate.as_view(), name='msg_create'),#建立留言
]
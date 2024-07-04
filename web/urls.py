from django.urls import path
from .views import *

urlpatterns=[
    path('', MessageList.as_view(), name='msg_list'),#空路徑(/message) 留言列表
    path('<int:pk>/', MessageView.as_view(), name='msg_view'),#留言內容
    path('create/', MessageCreate.as_view(), name='msg_create'),#建立留言
    path('<int:pk>/delete/', MessageDelete.as_view(), name='msg_delete'),#刪除留言
]
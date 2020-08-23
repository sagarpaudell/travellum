from django.urls import path
from . import views as chatView

urlpatterns=[
    path('',chatView.chatRedirect, name='chat1'),
    path('<str:email>',chatView.chat, name='chat')
]
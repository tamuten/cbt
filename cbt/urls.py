from re import U
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('name', views.get_name, name='get_name'),
    path('work', views.work, name='work'),
    path('user', views.user, name='user'),
    path('getUserList', views.get_user, name='get_user'),
]

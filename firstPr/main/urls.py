from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('user', views.user),
    path('login', views.login),
    path('regist', views.regist),
    path('graph', views.graph)
]
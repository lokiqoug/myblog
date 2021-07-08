# -*- coding: utf-8 -*-
# @Author : guoq
# @Time : 2021/7/7 10:39

from . import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('category/<int:id>/', views.category, name='category'),
    path('tag/<int:id>/', views.tag, name='tag'),
]

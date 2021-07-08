# -*- coding: utf-8 -*-
# @Author : guoq
# @Time : 2021/7/8 16:32

from . import views
from django.urls import path

app_name = 'comments'
urlpatterns = [
    path('comment/<int:post_id>', views.comment, name='comment')
]

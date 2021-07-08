# -*- coding: utf-8 -*-
# @Author : guoq
# @Time : 2021/7/8 16:16

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']

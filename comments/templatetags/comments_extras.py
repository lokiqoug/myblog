# -*- coding: utf-8 -*-
# @Author : guoq
# @Time : 2021/7/8 16:22
from django import template
from ..forms import CommentForm

register = template.Library()


@register.inclusion_tag('comments/inclusions/_form.html', takes_context=True)
def show_comment_form(context, post, form=None):
    if form is None:
        form = CommentForm()
    return {
        'form': form,
        'post': post
    }

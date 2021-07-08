# -*- coding: utf-8 -*-
# @Author : guoq
# @Time : 2021/7/7 17:15

from django import template
from ..models import Post, Categroy, Tag

register = template.Library()


@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {
        'recent_post_list': Post.objects.all().order_by('-create_time')[:num]
    }


@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {
        'category_list': Categroy.objects.all(),
        'post_all': Post.objects.all()
    }


@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.all()
    }


@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Post.objects.dates('create_time', 'month', order='DESC')
    }


@register.filter
def get_post_num_by_category(post, cate):
    post_list = post.filter(category=cate)
    return len(post_list)

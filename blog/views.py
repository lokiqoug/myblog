import re
import markdown
from blog.models import Post, Categroy, Tag
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.shortcuts import render, get_object_or_404


# Create your views here.

def index(request):
    post_list = Post.objects.all()
    context = {
        'post_list': post_list
    }
    return render(request, 'blog/index.html', context=context)


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify)
    ])
    post.body = md.convert(post.body)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    return render(request, 'blog/detail.html', context={'post': post})


def archive(request, year, month):
    post_list = Post.objects.filter(create_time__year=year,
                                    create_time__month=month
                                    ).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, id):
    cate = get_object_or_404(Categroy, id=id)
    post_list = Post.objects.filter(category=cate).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def tag(request, id):
    t = get_object_or_404(Tag, id=id)
    post_list = Post.objects.filter(tags=t).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

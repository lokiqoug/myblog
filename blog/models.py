import markdown
from django.db import models
from django.urls import reverse
from django.utils import timezone, html
from django.contrib.auth.models import User


# Create your models here.

class Categroy(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    # 标题
    title = models.CharField('标题', max_length=70)
    # 正文
    body = models.TextField('正文')
    # 创建时间
    create_time = models.DateTimeField('创建时间', default=timezone.now)
    # 修改时间
    modified_time = models.DateTimeField('修改时间')
    # 摘要
    excerpt = models.CharField('摘要', max_length=200, blank=True)
    # 类别，级联删除，某个类别删除后相关文章也同时删除
    category = models.ForeignKey(Categroy, verbose_name='类别', on_delete=models.CASCADE)
    # 标签
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    # 作者
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'id': self.id})

    def save(self, *args, **kwargs):
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        if not self.excerpt:
            self.excerpt = html.strip_tags(md.convert(self.body))[:54]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

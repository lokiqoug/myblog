from blog.models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST


# Create your views here.
@require_POST
def comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect(post)

    context = {
        'post': post,
        'form': form
    }

    return render(request, 'comments/preview.html', context=context)

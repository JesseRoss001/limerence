from django.shortcuts import render, get_object_or_404
from .models import BlogPage

def blog_list(request):
    posts = BlogPage.objects.live().order_by('-date')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPage, slug=slug)
    return render(request, 'blog/blog_detail.html', {'post': post})

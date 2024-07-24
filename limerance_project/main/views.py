from django.shortcuts import render
from .models import BlogIndexPage

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    try:
        blog_index_page = BlogIndexPage.objects.live().first()
        if blog_index_page:
            context = blog_index_page.get_context(request)
            return render(request, 'blog_index_page.html', context)
        else:
            return render(request, '404.html', status=404)
    except BlogIndexPage.DoesNotExist:
        return render(request, '404.html', status=404)

def services(request):
    return render(request, 'service.html')

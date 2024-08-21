
from django.shortcuts import render
from django.http import HttpResponse
def sitemap(request):
    sitemap_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://www.bornfreelimerencecoaching.com/</loc>
        <lastmod>2024-08-21T15:47:23+00:00</lastmod>
        <priority>1.00</priority>
    </url>
    <url>
        <loc>https://www.bornfreelimerencecoaching.com/about/</loc>
        <lastmod>2024-08-21T15:47:23+00:00</lastmod>
        <priority>0.80</priority>
    </url>
    <url>
        <loc>https://www.bornfreelimerencecoaching.com/contact/</loc>
        <lastmod>2024-08-21T15:47:23+00:00</lastmod>
        <priority>0.80</priority>
    </url>
    <url>
        <loc>https://www.bornfreelimerencecoaching.com/blog/</loc>
        <lastmod>2024-08-21T15:47:23+00:00</lastmod>
        <priority>0.80</priority>
    </url>
    <url>
        <loc>https://www.bornfreelimerencecoaching.com/services/</loc>
        <lastmod>2024-08-21T15:47:23+00:00</lastmod>
        <priority>0.80</priority>
    </url>
    <url>
        <loc>https://www.bornfreelimerencecoaching.com/other-services/</loc>
        <lastmod>2024-08-21T15:47:23+00:00</lastmod>
        <priority>0.80</priority>
    </url>
</urlset>'''
    return HttpResponse(sitemap_content, content_type="application/xml") 
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')



def services(request):
    return render(request, 'service.html')

def other_services(request):
    return render(request, 'other_services.html')
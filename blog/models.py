from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    meta_title = models.CharField(max_length=100, blank=True, help_text="SEO meta title for this blog post")
    meta_description = models.CharField(max_length=160, blank=True, help_text="SEO meta description for this blog post")

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('meta_title'),
        FieldPanel('meta_description'),
    ]

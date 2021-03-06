# Django Imports
from django.db import models
from django.contrib.sitemaps import ping_google

# Python Imports
import datetime

# Project Imports
from Django_Blog.blog.managers import EntryManager

class Entry(models.Model):
    """
    An Entry is one item to be listed in the blog page.
    """
    name = models.CharField(max_length=75, help_text='Name of blog entry')
    slug = models.SlugField()
    data = models.TextField()
    published = models.BooleanField(default=False)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)

    objects = EntryManager()

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()
        super(Entry, self).save(*args, **kwargs)
        try:
            ping_google()
        except Exception:
            pass

    @models.permalink
    def get_absolute_url(self):
        return ('blog_view', [str(self.slug)])

    def is_published(self):
        if self.published:
            return True
        else:
            return False
        


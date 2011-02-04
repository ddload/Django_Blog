# Django Imports
from django.db import models

# Python Imports
import datetime

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

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.datetime.now()
            self.modified = datetime.datetime.now()
            super(Entry, self).save(*args, **kwargs)

    def is_published(self):
        if self.published:
            return True
        else:
            return False

    def __unicode__(self):
        return self.name

    

from django.db import models

class Entry(models.Model):
    """
    An Entry is one item to be listed in the blog page.
    """
    name = models.CharField(max_length=75, help_text='Name of blog entry')
    slug = models.SlugField()
    data = models.TextField()
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)

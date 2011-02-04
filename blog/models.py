from django.db import models

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

    def save(self, force_insert=False, force_update=False):
        if not seld.id:
            self.created = datetime.datetime.now()
            self.modified = datetime.datetime.now()
            super(Entry, self).save(force_insert, force_update)

    def is_published(self):
        """
        Returns the entries published status
        """
        if self.published:
            return True
        else:
            return False

    def __unicode__(self):
        return self.name

    

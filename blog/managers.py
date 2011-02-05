from django.db import models

class EntryManager(models.Manager):
    def published(self):
        """
        Returns only published Entries.
        """
        return self.filter(published=True)

    def private(self):
        """
        Returns only private (non-published)
        Entries.
        """
        return self.filter(published=False)
        
        

        

from django.contrib.sitemaps import Sitemap
from Django_Blog.blog.models import Entry

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Entry.objects.published()

    def lastmod(self, obj):
        return obj.created

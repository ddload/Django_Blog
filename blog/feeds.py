from django.contrib.syndication.views import Feed
from Django_Blog.blog.models import Entry

class LatestEntriesFeed(Feed):
    title = "DjangoBlog.net site feed"
    link = "/sitefeed/"
    description = "Updates on changes and additions to djangoblog.net."

    def items(self):
        return Entry.objects.order_by('-modified')[:5]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return ''

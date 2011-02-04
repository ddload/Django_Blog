from django.conf.urls.defaults import *

from Django_Blog.blog.views import blog_index

urlpatterns = patterns('',
    url(r'^$/', blog_index, name='blog_index'),
)

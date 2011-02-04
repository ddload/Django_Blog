from django.conf.urls.defaults import *

from Django_Blog.blog.views import blog_index, BlogView, \
                                   blog_editor, blog_delete

urlpatterns = patterns('',
    url(r'^$', blog_index, name='blog_index'),
    url(r'^add/$', blog_editor, name='blog_add'),
    url(r'^view/(?P<id>\d+)/$', BlogView.as_view(), name='blog_view'),
    url(r'^edit/(?P<id>)\d+/$', blog_editor, name='blog_edit'),
    url(r'^delete/(?P<id>\d+)/$', blog_delete, name='blog_delete'),
)

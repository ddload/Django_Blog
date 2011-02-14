# Django Imports
from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, DeleteView
from django.contrib.auth.decorators import login_required

# Project Imports
from Django_Blog.blog.utils import reverse
from Django_Blog.blog.views import blog_editor, blog_delete, BlogIndex
from Django_Blog.blog.models import Entry

urlpatterns = patterns('',
    url(r'^$',BlogIndex.as_view(), name='blog_index'),
    url(r'^add/$', blog_editor, name='blog_add'),
    url(r'^view/(?P<slug>[-\w]+)/$', DetailView.as_view(
                                       model=Entry,
                                       template_name='blog/view.html'
                                ), name='blog_view'),
    url(r'^edit/(?P<slug>[-\w]+)/$', blog_editor, name='blog_edit'),
    url(r'^delete/(?P<slug>[-\w]+)/$', login_required(DeleteView.as_view(
                                         model=Entry,
                                         success_url=reverse('blog_index'))),
                                  name='blog_delete'),
)

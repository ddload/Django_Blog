from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, DeleteView
from utils import reverse

from Django_Blog.blog.views import blog_editor, blog_delete
from Django_Blog.blog.models import Entry

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(
                           queryset=Entry.objects.published(),
                           context_object_name='blog_index',
                           template_name='blog/index.html'
                           ), name='blog_index'),
    url(r'^add/$', blog_editor, name='blog_add'),
    url(r'^view/(?P<pk>\d+)/$', DetailView.as_view(
                                       model=Entry,
                                       template_name='blog/view.html'
                                ), name='blog_view'),
    url(r'^edit/(?P<id>\d+)/$', blog_editor, name='blog_edit'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteView.as_view(
                                         model=Entry,
                                         success_url=reverse('blog_index')),
                                  name='blog_delete'),
)

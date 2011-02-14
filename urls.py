from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from Django_Blog.sitemaps import BlogSitemap
from django.contrib import admin
admin.autodiscover()

sitemaps = {
    'blog': BlogSitemap,
}

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/', include('Django_Blog.blog.urls')),
    (r'^accounts/', include('registration.urls')),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)
urlpatterns += staticfiles_urlpatterns()

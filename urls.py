from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple  import direct_to_template

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
    (r'^comments/', include('django.contrib.comments.urls')),
    # Utilizing the contrib sitemaps app.
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    # Utilizing django-robots app. 
    (r'^robots.txt$', include('robots.urls')),
)
urlpatterns += patterns('',
    (r'^accounts/profile/$', direct_to_template, {'template': 'registration/profile.html'}),
    (r'^accounts/profile/edit/$', direct_to_template, {'template': 'registration/profile_form.html'}),
)
                     
urlpatterns += staticfiles_urlpatterns()

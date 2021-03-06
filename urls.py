from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple  import direct_to_template
from django.views.generic.simple import redirect_to
from django.contrib import admin
admin.autodiscover()

from Django_Blog.sitemaps import BlogSitemap
from Django_Blog.blog.views import contact

sitemaps = {
    'blog': BlogSitemap,
}

urlpatterns = patterns('',
    (r'^$', redirect_to, {'url':'/blog/'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/', include('Django_Blog.blog.urls')),
    (r'^accounts/', include('registration.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    url(r'^links/', direct_to_template, {'template':'links.html'}, name='links'),
    url(r'^contact/', contact, name='contact'),
    # Utilizing the contrib sitemaps app.
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    # Utilizing django-robots app. 
    (r'^robots.txt$', include('robots.urls')),
)

urlpatterns += patterns('',
    (r'^accounts/profile/$', direct_to_template, {'template': 'registration/profile.html'}),
    (r'^accounts/profile/edit/$', direct_to_template, {'template': 'registration/profile_form.html'}),
)
                     
#urlpatterns += staticfiles_urlpatterns()

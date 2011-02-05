from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/', include('Django_Blog.blog.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login_view'),
)
urlpatterns += staticfiles_urlpatterns()

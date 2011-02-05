from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/', include('Django_Blog.blog.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
)

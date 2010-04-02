from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
             { 'document_root': 'tiny_mce' }),
    (r'^search/$', 'cms.search.views.search'),
    (r'^weblog/', include('coltrane.urls')),
    (r'', include('django.contrib.flatpages.urls')),
)

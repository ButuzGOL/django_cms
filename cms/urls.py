from django.conf.urls.defaults import *
from coltrane.feeds import CategoryFeed, LatestEntriesFeed

from django.contrib import admin
admin.autodiscover()

feeds = { 'entries': LatestEntriesFeed,
          'categories': CategoryFeed }

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
             { 'document_root': 'tiny_mce' }),
    (r'^search/$', 'cms.search.views.search'),

    (r'^weblog/categories/', include('coltrane.urls.categories')),
    (r'^weblog/links/', include('coltrane.urls.links')),
    (r'^weblog/tags/', include('coltrane.urls.tags')),
    (r'^weblog/', include('coltrane.urls.entries')),

    (r'^comments/', include('django.contrib.comments.urls')),
    
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
     { 'feed_dict': feeds }),

    (r'^snippets/', include('cab.urls.snippets')),
    (r'^languages/', include('cab.urls.languages')),
    (r'^bookmarks/', include('cab.urls.bookmarks')),
    (r'^popular/', include('cab.urls.popular')),

    (r'', include('django.contrib.flatpages.urls')),
)

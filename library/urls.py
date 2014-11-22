from django.conf.urls import patterns, include, url
from library import views
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^artist/(?P<artist_name_url>\w+)$', views.artist, name='artist'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}),
        )
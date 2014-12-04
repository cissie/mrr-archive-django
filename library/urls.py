from django.conf.urls import patterns, include, url
from library import views
# from django.conf import settings


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_artist/$', views.add_artist, name='add_artist'),
        url(r'^artist/(?P<artist_name_url>\w+)$', views.artist, name='artist'),
        url(r'^ajax$', views.ajax, name='ajax'),

)


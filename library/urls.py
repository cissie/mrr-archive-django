from django.conf.urls import patterns, include, url
from library import views
# from django.conf import settings


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^artist/(?P<artist_name_url>\w+)$', views.artist, name='artist'),

)


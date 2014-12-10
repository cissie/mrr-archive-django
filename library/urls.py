from django.conf.urls import patterns, include, url
from library import views
# from django.conf import settings


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_artist/$', views.add_artist, name='add_artist'),
        url(r'^artist/(?P<artist_name_url>\w+)$', views.artist, name='artist'),
        url(r'^ajax?$', views.ajax, name='ajax'),
        url(r'^dom?$', views.dom, name='dom'),
        url(r'^title?$', views.record_title, name="title"),
        url(r'^label?$', views.record_label, name="label"),
        url(r'^review?$', views.record_review, name="review")
)


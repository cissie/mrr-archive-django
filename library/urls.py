from django.conf.urls import patterns, include, url
from library import views
# from django.conf import settings


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_artist/$', views.add_artist, name='add_artist'),
        url(r'^artist/(?P<artist_id>\w*)$', views.artist, name='artist'),
        url(r'^ajax?$', views.ajax, name='ajax'),
        url(r'^dom?$', views.dom, name='dom'),
        url(r'^titles?$', views.record_title, name="titles"),
        url(r'^record_title/(?P<record_title_id>\w*)$', views.record_title_detail, name='title'),
        url(r'^label?$', views.record_label, name="label"),
        url(r'^review?$', views.record_review, name="review"),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.login, name='login'),
        url(r'^restricted/', views.restricted, name='restricted'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^load_data?$', views.load_data, name='load_data')
)

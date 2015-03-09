from django.conf import settings
from django.conf.urls import patterns, include, url
from library import views
# from django.conf import settings


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        # url(r'^add_review/$', views.add_review, name='add_review'),
        url(r'^artist/(?P<artist_id>\w*)$', views.artist, name='artist'),
        # url(r'^ajax?$', views.ajax, name='ajax'),
        # url(r'^dom?$', views.dom, name='dom'),
        url(r'^titles$', views.record_title, name='titles'),
        url(r'^record_title_detail/(?P<record_title_id>\w*)$', views.record_title_detail, name='title'),
        url(r'^labels?$', views.record_label, name='labels'),
        url(r'^record_label_detail/(?P<record_label_id>\w*)$', views.record_label_detail, name='label'),
        url(r'^countries?$', views.country, name='countries'),
        url(r'^country_detail/(?P<country_id>\w*)$', views.country_detail, name='country'),
        url(r'^reviewers?$', views.reviewer, name='reviewers'),
        url(r'record_reviewer_detail/(?P<reviewer_name_id>\w*)$', views.record_reviewer_detail, name='record_reviewer'),
        url(r'^issues?$', views.issue_number, name='issue_numbers'),
        url(r'issue_number_detail/(?P<issue_number_id>\w*)$', views.issue_number_detail, name='issue_number'),
        url(r'^years?$', views.years, name='years'),
        url(r'year_detail/(?P<release_year_id>\w*)$', views.year_detail, name='year'),
        url(r'^formats?$', views.formats, name='formats'),
        url(r'format_detail/(?P<format_type_id>\w*)$', views.format_detail, name='format'),
        url(r'band_member_detail/(?P<band_member_id>\w*)$', views.band_member_detail, name='band_member'),
        url(r'^review?$', views.record_review, name='review'),
        # url(r'^register/$', views.register, name='register'),
        # url(r'^login/$', views.login, name='login'),
        # url(r'^restricted/', views.restricted, name='restricted'),
        # url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^search/$', include('haystack.urls')),
        # url(r'^edit_form/(?P<record_title_id>\w*)$', views.edit_form, name='edit_form'),
        # url(r'^cover_art_form/(?P<record_title_id>\w*)$', views.upload_art, name='cover_art_form'),
        # url(r'^record_review_form/(?P<record_title_id>\w*)$', views.add_review, name='record_review_form'),
        # url(r'^load_data?$', views.load_data, name='load_data'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
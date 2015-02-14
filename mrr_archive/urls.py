from django.conf import settings
from django.conf.urls import *
from django.conf.urls.static import static
from django.contrib import admin
from library import views
from tastypie.api import Api
from library.api.resources import RecordTitle
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(RecordTitle())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mrr_archive.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^library/', include('library.urls')),
    (r'^api/', include(v1_api.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )

from tastypie.resources import ModelResource
from library.models import RecordTitle

class RecordTitle(ModelResource):
    class Meta:
        queryset = RecordTitle.objects.all()
        allowed_methods = ['get']



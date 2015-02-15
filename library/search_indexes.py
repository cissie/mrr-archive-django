from haystack import indexes

from django.utils import timezone

from library.models import Artist, RecordTitle, RecordLabel


class ArtistIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    artist = indexes.CharField(model_attr='name')

    def get_model(self):
        return Artist

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter()


class TitleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='record_title')

    def get_model(self):
        return RecordTitle

    def index_queryset(self, using=None):
        return self.get_model().objects.filter()


class LabelIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    label = indexes.CharField(model_attr='record_label')

    def get_model(self):
        return RecordLabel

    def index_queryset(self, using=None):
        return self.get_model().objects.filter()



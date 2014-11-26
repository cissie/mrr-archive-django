from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)


class RecordTitle(models.Model):
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=200)
    format = models.CharField(max_length=200)
    year = models.IntegerField(default=0)


# class CoverArt(models.Model):
#     record_title = models.ForeignKey(RecordTitle)
#     cover_art = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=200)
#     url = models.URLField()

class Country(models.Model):
    name = models.ForeignKey(Artist)
    country = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "countries"


class RecordLabel(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    record_label = models.CharField(max_length=200)


class CatalogNumber(models.Model):
    record_label = models.ForeignKey(RecordLabel)
    catalog_number = models.CharField(max_length=200)


class Discography(models.Model):
    artist = models.ForeignKey(Artist)
    discography = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "discographies"


class BandMember(models.Model):
    artist = models.ForeignKey(Artist)
    band_member = models.CharField(max_length=200)


class RecordReview(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    record_review = models.TextField()


class IssueNumber(models.Model):
    review = models.ForeignKey(RecordReview)
    issue_number = models.IntegerField(default=0)


class ReviewerName(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    reviewer_name = models.CharField(max_length=200)



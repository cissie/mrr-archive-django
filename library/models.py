from django.db import models


class Artist(models.Model):
    artist = models.CharField(max_length=200)
    url = models.URLField()


class RecordTitle(models.Model):
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=200)
    url = models.URLField()


class Format(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    format = models.CharField(max_length=200)


class Country(models.Model):
    artist = models.ForeignKey(Artist)
    country = models.CharField(max_length=200)
    url = models.URLField()

    class Meta:
        verbose_name_plural = "countries"


class Year(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    year = models.IntegerField(default=0)
    url = models.URLField()


# class CoverArt(models.Model):
#     record_title = models.ForeignKey(RecordTitle)
#     cover_art = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=200)
#     url = models.URLField()


class Label(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    label = models.CharField(max_length=200)
    url = models.URLField()


class CatalogNumber(models.Model):
    label = models.ForeignKey(Label)
    catalog_number = models.CharField(max_length=200)


class Discography(models.Model):
    artist = models.ForeignKey(Artist)
    releases = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "discographies"


class Member(models.Model):
    artist = models.ForeignKey(Artist)
    member = models.CharField(max_length=200)
    url = models.URLField()


class Review(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    review = models.TextField()
    url = models.URLField()


class IssueNumber(models.Model):
    review = models.ForeignKey(Review)
    issue = models.IntegerField(default=0)


class Reviewer(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    reviewer = models.CharField(max_length=200)
    url = models.URLField()



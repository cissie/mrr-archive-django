from django.contrib.auth.models import User
from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class RecordTitle(models.Model):
    artist = models.ForeignKey(Artist)
    record_title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.record_title


class Country(models.Model):
    artist = models.ForeignKey(Artist)
    country = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "countries"

    def __unicode__(self):
        return self.country


class FormatType(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    format_type = models.CharField(max_length=200)

    def __unicode__(self):
        return self.format_type


class ReleaseYear(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    release_year = models.IntegerField(default=0)

    def __unicode__(self):
        return self.release_year


class CoverArt(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    cover_art = models.ImageField(upload_to='cover_images', blank=True)

    class Meta:
        verbose_name_plural = "cover art"

    def __unicode__(self):
        return self.cover_art


class RecordLabel(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    record_label = models.CharField(max_length=200)

    def __unicode__(self):
        return self.record_label


class CatalogNumber(models.Model):
    record_label = models.ForeignKey(RecordLabel)
    catalog_number = models.CharField(max_length=200)

    def __unicode__(self):
        return self.catalog_number


class RecordReview(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    record_review = models.TextField()

    def __unicode__(self):
        return self.record_review


class IssueNumber(models.Model):
    record_review = models.ForeignKey(RecordReview)
    issue_number = models.IntegerField(default=0)

    def __unicode__(self):
        return self.issue_number


class Discography(models.Model):
    artist = models.ForeignKey(Artist)
    discography = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "discographies"

    def __unicode__(self):
        return self.discography


class ReviewerName(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    reviewer_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.reviewer_name


class FileUnder(models.Model):
    artist = models.ForeignKey(Artist)
    file_under = models.CharField(max_length=200)

    def __unicode__(self):
        return self.file_under


class Notes(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    notes = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "notes"

    def __unicode__(self):
        return self.notes


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username



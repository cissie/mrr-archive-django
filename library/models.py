from django.contrib.auth.models import User
from django.db import models


class Country(models.Model):
    country = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "countries"

    def __unicode__(self):
        return self.country


class FileUnder(models.Model):
    file_under = models.TextField()

    def __unicode__(self):
        return self.file_under


class Artist(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, blank=True, null=True)
    file_under = models.ForeignKey(FileUnder, blank=True, null=True)

    def __unicode__(self):
        return self.name


class FormatType(models.Model):
    format_type = models.CharField(max_length=200)

    def __unicode__(self):
        return self.format_type


class ReleaseYear(models.Model):
    release_year = models.IntegerField(default=0)

    def __unicode__(self):
        return self.release_year


class RecordLabel(models.Model):
    record_label = models.TextField(null=True)

    def __unicode__(self):
        return self.record_label


class CatalogNumber(models.Model):
    catalog_number = models.TextField(null=True)

    def __unicode__(self):
        return self.catalog_number


class IssueNumber(models.Model):
    issue_number = models.IntegerField(default=0)

    def __unicode__(self):
        return self.issue_number


class Notes(models.Model):
    notes = models.TextField()

    class Meta:
        verbose_name_plural = "notes"

    def __unicode__(self):
        return self.notes

class CoverArt(models.Model):
    cover_art = models.ImageField(upload_to='media/img/cover_images', blank=True, null=True, default='static/img/cover_images/vinyl.tif')

    class Meta:
        verbose_name_plural = "cover art"

    def __unicode__(self):
        return self.cover_art


class RecordReview(models.Model):
    record_review = models.TextField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.record_review


class ReviewerName(models.Model):
    reviewer_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.reviewer_name


class RecordTitle(models.Model):
    artist = models.ForeignKey(Artist, blank=True, null=True)
    format_type = models.ForeignKey(FormatType, null=True)
    record_title = models.TextField()
    release_year = models.ForeignKey(ReleaseYear, null=True)
    record_label = models.ForeignKey(RecordLabel, null=True)
    catalog_number = models.ForeignKey(CatalogNumber, null=True, blank=True)
    issue_number = models.ForeignKey(IssueNumber, null=True, blank=True)
    notes = models.ForeignKey(Notes, null=True, blank=True)
    # last_edited_by = models.ForeignKey(User)
    # covers = models.ForeignKey(CoverArt, default='static/img/cover_images/vinyl.tif',
    #                               blank=True, null=True)
    record_review = models.ForeignKey(RecordReview, null=True, blank=True)
    reviewer_name = models.ForeignKey(ReviewerName, null=True, blank=True)

    def __unicode__(self):
        return self.record_title



class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username



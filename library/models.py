from django.contrib.auth.models import User
from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)


class RecordTitle(models.Model):
    artist = models.ForeignKey(Artist)
    record_title = models.CharField(max_length=200)


class Country(models.Model):
    artist = models.ForeignKey(Artist)
    country = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "countries"


class FormatType(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    format_type = models.CharField(max_length=200)


class ReleaseYear(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    release_year = models.IntegerField(default=0)


class CoverArt(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    cover_art = models.ImageField(upload_to='cover_images', blank=True)



class RecordLabel(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    record_label = models.CharField(max_length=200)


class CatalogNumber(models.Model):
    record_label = models.ForeignKey(RecordLabel)
    catalog_number = models.CharField(max_length=200)


class RecordReview(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    record_review = models.TextField()


class IssueNumber(models.Model):
    record_review = models.ForeignKey(RecordReview)
    issue_number = models.IntegerField(default=0)


class Discography(models.Model):
    artist = models.ForeignKey(Artist)
    discography = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "discographies"


class ReviewerName(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    reviewer_name = models.CharField(max_length=200)


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username



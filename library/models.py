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


class BandMember(models.Model):
    band_member = models.CharField(max_length=1000, blank=True, null=True)


    def __unicode__(self):
        return self.band_member


class Artist(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    country = models.ForeignKey(Country, blank=True, null=True)
    file_under = models.ForeignKey(FileUnder, blank=True, null=True)
    band_members = models.ManyToManyField(BandMember, blank=True, null=True)

    def __unicode__(self):
        return self.name


class FormatType(models.Model):
    format_type = models.CharField(max_length=200)

    def __unicode__(self):
        return self.format_type


class ReleaseYear(models.Model):
    release_year = models.CharField(default=0, max_length=4)

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
    issue_number = models.CharField(default=0, max_length=7)

    def __unicode__(self):
        return self.issue_number


class Notes(models.Model):
    notes = models.TextField()

    class Meta:
        verbose_name_plural = "notes"

    def __unicode__(self):
        return self.notes


class ReviewerName(models.Model):
    reviewer_name = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.reviewer_name

class RecordReview(models.Model):
    record_review = models.TextField()


class TrackName(models.Model):
    track_name = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.track_name


class RecordTitle(models.Model):
    artists = models.ManyToManyField(Artist)
    format_type = models.ForeignKey(FormatType, null=True)
    record_title = models.TextField()
    release_year = models.ForeignKey(ReleaseYear, null=True)
    record_labels = models.ManyToManyField(RecordLabel, null=True)
    catalog_numbers = models.ManyToManyField(CatalogNumber, null=True, blank=True)
    countries = models.ManyToManyField(Country, null=True, blank=True)
    issue_number = models.ForeignKey(IssueNumber, null=True, blank=True)
    notes = models.ForeignKey(Notes, null=True, blank=True)
    cover_art = models.ImageField(upload_to='media/img/cover_images/', default='static/img/vinyl.png', blank=True, null=True)
    record_review = models.ForeignKey(RecordReview, blank=True, null=True)
    reviewer_names = models.ManyToManyField(ReviewerName, blank=True, null=True)
    track_names = models.ManyToManyField(TrackName, blank=True, null=True)
    band_members = models.ManyToManyField(BandMember, blank=True, null=True)
    in_collection = models.BooleanField(default=True)
    stolen = models.BooleanField(default=False)
    wanted = models.BooleanField(default=False)

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



from django.db import models


class Artist(models.Model):
    artist = models.CharField(max_length=200)
    column1 = models.Field.db_column


class RecordTitle(models.Model):
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=200)
    column2 = models.Field.db_column
    

class Format(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    format = models.CharField(max_length=200)
    column3 = models.Field.db_column


class Country(models.Model):
    artist = models.ForeignKey(Artist)
    country = models.CharField(max_length=200)
    column7 = models.Field.db_column


class Year(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    year = models.CharField(max_length=200)
    column6 = models.Field.db_column


class CoverArt(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    cover_art = models.ImageField(height_field=None, width_field=None, max_length=200)


class Label(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    label = models.CharField(max_length=200)
    column4 = models.Field.db_column


class CatalogNumber(models.Model):
    label = models.ForeignKey(Label)
    catalog_number = models.CharField(max_length=200)
    column5 = models.Field.db_column


class Discography(models.Model):
    artist = models.ForeignKey(Artist)
    releases = models.CharField(max_length=200)


class Members(models.Model):
    artist = models.ForeignKey(Artist)
    members = models.CharField(max_length=200)


class Review(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    review = models.TextField


class IssueNumber(models.Model):
    review = models.ForeignKey(Review)
    issue = models.IntegerField(default=0)


class Reviewer(models.Model):
    record_title = models.ForeignKey(RecordTitle)
    reviewer = models.CharField(max_length=200)



# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'library_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'library', ['Country'])

        # Adding model 'FileUnder'
        db.create_table(u'library_fileunder', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file_under', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'library', ['FileUnder'])

        # Adding model 'Artist'
        db.create_table(u'library_artist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.Country'], null=True, blank=True)),
            ('file_under', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.FileUnder'], null=True, blank=True)),
        ))
        db.send_create_signal(u'library', ['Artist'])

        # Adding model 'FormatType'
        db.create_table(u'library_formattype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('format_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'library', ['FormatType'])

        # Adding model 'ReleaseYear'
        db.create_table(u'library_releaseyear', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('release_year', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'library', ['ReleaseYear'])

        # Adding model 'RecordLabel'
        db.create_table(u'library_recordlabel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record_label', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'library', ['RecordLabel'])

        # Adding model 'CatalogNumber'
        db.create_table(u'library_catalognumber', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('catalog_number', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'library', ['CatalogNumber'])

        # Adding model 'IssueNumber'
        db.create_table(u'library_issuenumber', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('issue_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'library', ['IssueNumber'])

        # Adding model 'Notes'
        db.create_table(u'library_notes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'library', ['Notes'])

        # Adding model 'CoverArt'
        db.create_table(u'library_coverart', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cover_art', self.gf('django.db.models.fields.files.ImageField')(default='static/img/cover_images/vinyl.tif', max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'library', ['CoverArt'])

        # Adding model 'RecordReview'
        db.create_table(u'library_recordreview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record_review', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'library', ['RecordReview'])

        # Adding model 'ReviewerName'
        db.create_table(u'library_reviewername', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reviewer_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'library', ['ReviewerName'])

        # Adding model 'RecordTitle'
        db.create_table(u'library_recordtitle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.Artist'], null=True)),
            ('format_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.FormatType'], null=True)),
            ('record_title', self.gf('django.db.models.fields.TextField')()),
            ('release_year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.ReleaseYear'], null=True)),
            ('record_label', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.RecordLabel'], null=True)),
            ('catalog_number', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.CatalogNumber'], null=True, blank=True)),
            ('issue_number', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.IssueNumber'], null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.Notes'], null=True, blank=True)),
            ('record_review', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.RecordReview'], null=True, blank=True)),
            ('reviewer_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.ReviewerName'], null=True, blank=True)),
        ))
        db.send_create_signal(u'library', ['RecordTitle'])

        # Adding model 'UserProfile'
        db.create_table(u'library_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'library', ['UserProfile'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table(u'library_country')

        # Deleting model 'FileUnder'
        db.delete_table(u'library_fileunder')

        # Deleting model 'Artist'
        db.delete_table(u'library_artist')

        # Deleting model 'FormatType'
        db.delete_table(u'library_formattype')

        # Deleting model 'ReleaseYear'
        db.delete_table(u'library_releaseyear')

        # Deleting model 'RecordLabel'
        db.delete_table(u'library_recordlabel')

        # Deleting model 'CatalogNumber'
        db.delete_table(u'library_catalognumber')

        # Deleting model 'IssueNumber'
        db.delete_table(u'library_issuenumber')

        # Deleting model 'Notes'
        db.delete_table(u'library_notes')

        # Deleting model 'CoverArt'
        db.delete_table(u'library_coverart')

        # Deleting model 'RecordReview'
        db.delete_table(u'library_recordreview')

        # Deleting model 'ReviewerName'
        db.delete_table(u'library_reviewername')

        # Deleting model 'RecordTitle'
        db.delete_table(u'library_recordtitle')

        # Deleting model 'UserProfile'
        db.delete_table(u'library_userprofile')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'library.artist': {
            'Meta': {'object_name': 'Artist'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Country']", 'null': 'True', 'blank': 'True'}),
            'file_under': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.FileUnder']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'library.catalognumber': {
            'Meta': {'object_name': 'CatalogNumber'},
            'catalog_number': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'library.country': {
            'Meta': {'object_name': 'Country'},
            'country': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'library.coverart': {
            'Meta': {'object_name': 'CoverArt'},
            'cover_art': ('django.db.models.fields.files.ImageField', [], {'default': "'static/img/cover_images/vinyl.tif'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'library.fileunder': {
            'Meta': {'object_name': 'FileUnder'},
            'file_under': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'library.formattype': {
            'Meta': {'object_name': 'FormatType'},
            'format_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'library.issuenumber': {
            'Meta': {'object_name': 'IssueNumber'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_number': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'library.notes': {
            'Meta': {'object_name': 'Notes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {})
        },
        u'library.recordlabel': {
            'Meta': {'object_name': 'RecordLabel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record_label': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        u'library.recordreview': {
            'Meta': {'object_name': 'RecordReview'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record_review': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'library.recordtitle': {
            'Meta': {'object_name': 'RecordTitle'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Artist']", 'null': 'True'}),
            'catalog_number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.CatalogNumber']", 'null': 'True', 'blank': 'True'}),
            'format_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.FormatType']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.IssueNumber']", 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Notes']", 'null': 'True', 'blank': 'True'}),
            'record_label': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.RecordLabel']", 'null': 'True'}),
            'record_review': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.RecordReview']", 'null': 'True', 'blank': 'True'}),
            'record_title': ('django.db.models.fields.TextField', [], {}),
            'release_year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.ReleaseYear']", 'null': 'True'}),
            'reviewer_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.ReviewerName']", 'null': 'True', 'blank': 'True'})
        },
        u'library.releaseyear': {
            'Meta': {'object_name': 'ReleaseYear'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'release_year': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'library.reviewername': {
            'Meta': {'object_name': 'ReviewerName'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reviewer_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'library.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['library']
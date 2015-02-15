# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CatalogNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('catalog_number', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'countries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FileUnder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_under', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FormatType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('format_type', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IssueNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issue_number', models.CharField(default=0, max_length=7)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notes', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'notes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecordLabel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('record_label', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecordReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('record_review', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecordTitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('record_title', models.TextField()),
                ('cover_art', models.ImageField(default=b'static/img/cover_images/vinyl.tif', null=True, upload_to=b'media/img/cover_images/', blank=True)),
                ('in_collection', models.BooleanField(default=True)),
                ('stolen', models.BooleanField(default=False)),
                ('wanted', models.BooleanField(default=False)),
                ('artist', models.ManyToManyField(to='library.Artist')),
                ('catalog_number', models.ForeignKey(blank=True, to='library.CatalogNumber', null=True)),
                ('country', models.ManyToManyField(to='library.Country', null=True, blank=True)),
                ('format_type', models.ForeignKey(to='library.FormatType', null=True)),
                ('issue_number', models.ForeignKey(blank=True, to='library.IssueNumber', null=True)),
                ('notes', models.ForeignKey(blank=True, to='library.Notes', null=True)),
                ('record_label', models.ManyToManyField(to='library.RecordLabel', null=True)),
                ('record_review', models.ManyToManyField(to='library.RecordReview', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReleaseYear',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('release_year', models.CharField(default=0, max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReviewerName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reviewer_name', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='recordtitle',
            name='release_year',
            field=models.ForeignKey(to='library.ReleaseYear', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recordtitle',
            name='reviewer_name',
            field=models.ManyToManyField(to='library.ReviewerName', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='country',
            field=models.ForeignKey(blank=True, to='library.Country', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='file_under',
            field=models.ForeignKey(blank=True, to='library.FileUnder', null=True),
            preserve_default=True,
        ),
    ]

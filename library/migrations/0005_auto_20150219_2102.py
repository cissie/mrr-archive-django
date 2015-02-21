# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20150219_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordtitle',
            name='band_members',
            field=models.ManyToManyField(to='library.BandMember', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recordtitle',
            name='cover_art',
            field=models.ImageField(default=b'static/img/vinyl.png', null=True, upload_to=b'media/img/cover_images/', blank=True),
        ),
    ]

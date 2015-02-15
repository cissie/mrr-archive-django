# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recordtitle',
            name='country',
        ),
        migrations.AlterField(
            model_name='recordtitle',
            name='artist',
            field=models.ForeignKey(to='library.Artist'),
        ),
        migrations.AlterField(
            model_name='recordtitle',
            name='record_label',
            field=models.ForeignKey(to='library.RecordLabel', null=True),
        ),
        migrations.AlterField(
            model_name='recordtitle',
            name='record_review',
            field=models.ForeignKey(blank=True, to='library.RecordReview', null=True),
        ),
        migrations.AlterField(
            model_name='recordtitle',
            name='reviewer_name',
            field=models.ForeignKey(blank=True, to='library.ReviewerName', null=True),
        ),
    ]

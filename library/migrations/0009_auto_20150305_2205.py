# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20150305_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordtitle',
            name='reviewed',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recordtitle',
            name='wanted',
            field=models.BooleanField(default=False),
        ),
    ]

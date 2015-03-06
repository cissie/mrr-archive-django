# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_recordtitle_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordtitle',
            name='wanted',
            field=models.BooleanField(default=True),
        ),
    ]

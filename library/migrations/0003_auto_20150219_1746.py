# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20150219_1742'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ['name']},
        ),
    ]

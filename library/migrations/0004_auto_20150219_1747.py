# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20150219_1746'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ['file_under']},
        ),
    ]

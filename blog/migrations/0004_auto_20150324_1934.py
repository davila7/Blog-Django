# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150324_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime.now, auto_now=True, null=True),
            preserve_default=True,
        ),
    ]

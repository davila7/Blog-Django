# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime.now, auto_now_add=True, null=True),
            preserve_default=True,
        ),
    ]

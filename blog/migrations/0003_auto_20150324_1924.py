# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_entrada_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='slug',
            field=models.SlugField(max_length=200, editable=False),
            preserve_default=True,
        ),
    ]

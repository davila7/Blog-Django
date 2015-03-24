# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('slug', models.SlugField(max_length=200)),
                ('publish', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
            },
            bases=(models.Model,),
        ),
    ]

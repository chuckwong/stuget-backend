# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='android_sync_amount',
            field=models.IntegerField(default=0, verbose_name='Android'),
        ),
        migrations.AddField(
            model_name='phone',
            name='ios_sync_amount',
            field=models.IntegerField(default=0, verbose_name='iOS'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='sync_amount',
            field=models.IntegerField(default=0, verbose_name='\u603b\u540c\u6b65\u6b21\u6570'),
        ),
    ]

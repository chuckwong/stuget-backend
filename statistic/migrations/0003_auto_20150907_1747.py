# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0002_auto_20150729_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='android_sync_amount',
            field=models.IntegerField(default=0, verbose_name='Android\u540c\u6b65\u6b21\u6570'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='ios_sync_amount',
            field=models.IntegerField(default=0, verbose_name='iOS\u540c\u6b65\u6b21\u6570'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='sync_amount',
            field=models.IntegerField(default=0, verbose_name='\u603b\u5171\u540c\u6b65\u6b21\u6570'),
        ),
    ]

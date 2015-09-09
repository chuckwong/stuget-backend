# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(default=b'', max_length=200, verbose_name='\u7c7b\u540d'),
        ),
        migrations.AlterField(
            model_name='phonelist',
            name='phone_name',
            field=models.CharField(default=b'', max_length=200, verbose_name='\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='phonelist',
            name='phone_num1',
            field=models.CharField(default=b'', max_length=200, verbose_name='\u7535\u8bdd1'),
        ),
        migrations.AlterField(
            model_name='phonelist',
            name='phone_num2',
            field=models.CharField(default=b'', max_length=200, verbose_name='\u7535\u8bdd2', blank=True),
        ),
        migrations.AlterField(
            model_name='version',
            name='version_num',
            field=models.CharField(default=b'20150729042210', max_length=200, verbose_name='\u7248\u672c\u53f7'),
        ),
    ]

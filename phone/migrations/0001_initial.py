# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(default=b'', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_name', models.CharField(default=b'', max_length=200)),
                ('phone_num1', models.CharField(default=b'', max_length=200)),
                ('phone_num2', models.CharField(default=b'', max_length=200, blank=True)),
                ('phone_category', models.ForeignKey(to='phone.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version_num', models.CharField(default=b'20150729042210', max_length=200)),
            ],
        ),
    ]

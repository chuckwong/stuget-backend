# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(default=b'', max_length=200, verbose_name='\u7528\u6237\u540d')),
                ('auth_key', models.CharField(default=b'', max_length=200, verbose_name='\u8ba4\u8bc1\u5bc6\u94a5')),
            ],
        ),
    ]

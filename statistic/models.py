# -*- coding: utf-8 -*- 

from django.db import models

# phone
class Phone(models.Model):
    ios_sync_amount = models.IntegerField(u'iOS同步次数', default=0)
    android_sync_amount = models.IntegerField(u'Android同步次数', default=0)
    sync_amount = models.IntegerField(u'总共同步次数', default=0)

    def __unicode__(self):
        return 'Phone Statistics'

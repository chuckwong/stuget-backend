# -*- coding: utf-8 -*-

from django.db import models


# userList
class UserList(models.Model):
    username = models.CharField(u'用户名', max_length=200, default='')
    auth_key = models.CharField(u'认证密钥', max_length=200, default='')
    def __unicode__(self):
        return self.username









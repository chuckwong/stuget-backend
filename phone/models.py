# -*- coding: utf-8 -*- 

from django.db import models
import datetime
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# category
class Category(models.Model):
    category_name = models.CharField(u'类名', max_length=200, default='')
    def __unicode__(self):
        return self.category_name
    # rewrite save() for updating version
    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)
        v = Version.objects.get()
        v.version_num = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        v.save()

# phonelist
class PhoneList(models.Model):
    phone_category = models.ForeignKey(Category)
    phone_name = models.CharField(u'名称', max_length=200, default='')
    phone_num1 = models.CharField(u'电话1', max_length=200, default='')
    phone_num2 = models.CharField(u'电话2', max_length=200, default='', blank=True)
    def __unicode__(self):
        return self.phone_name
    # rewrite save() for updating version
    def save(self, *args, **kwargs):
        super(PhoneList, self).save(*args, **kwargs)
        v = Version.objects.get()
        v.version_num = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        v.save()

# version
class Version(models.Model):
    version_num = models.CharField(u'版本号', max_length=200, default='20150729042210')
    def __unicode__(self):
        return self.version_num



# rewrite delete() for updating version
@receiver(pre_delete, sender=PhoneList)
def _phonelist_delete(sender, instance, **kwargs):
    print "deleting-phonelist"
    v = Version.objects.get()
    v.version_num = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    v.save()
# rewrite delete() for updating version
@receiver(pre_delete, sender=Category)
def _category_delete(sender, instance, **kwargs):
    print "deleting-category"
    v = Version.objects.get()
    v.version_num = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    v.save()











# -*- coding: utf-8 -*- 

from django.contrib import admin

from .models import Phone
from phone.models import Category, PhoneList

# phone statistics
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['category_amount', 'phone_amount', 'ios_sync_amount', 'android_sync_amount', 'sync_amount']
    readonly_fields = ['category_amount', 'phone_amount', 'ios_sync_amount', 'android_sync_amount', 'sync_amount']

    def category_amount(self, obj):
        return Category.objects.all().count()

    def phone_amount(self, obj):
        return PhoneList.objects.all().count()

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_save_permission(self, request, obj=None):
        return False

    category_amount.short_description = u'类别数'
    phone_amount.short_description = u'电话数'

admin.site.register(Phone, PhoneAdmin)

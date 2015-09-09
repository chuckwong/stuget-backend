# -*- coding: utf-8 -*- 

from django.contrib import admin
from .models import Category, PhoneList, Version

class PhoneListInline(admin.TabularInline):
    model = PhoneList
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'number_of_phone']
    inlines = [PhoneListInline, ]
    # return numberOfPhone
    def number_of_phone(self, obj):
        return PhoneList.objects.filter(phone_category=obj).count()
    number_of_phone.short_description = u'电话数'


class PhoneListAdmin(admin.ModelAdmin):
    list_display = ['phone_name', 'phone_num1', 'phone_num2', 'category']
    search_fields = ['phone_name', 'phone_num1', 'phone_num2']
    def category(self, obj):
        return obj.phone_category
    category.short_description = u'所属类别'

class VersionAdmin(admin.ModelAdmin):
    readonly_fields = ['version_num']
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_save_permission(self, request, obj=None):
        return False


admin.site.register(Category, CategoryAdmin)
admin.site.register(PhoneList, PhoneListAdmin)
admin.site.register(Version, VersionAdmin)

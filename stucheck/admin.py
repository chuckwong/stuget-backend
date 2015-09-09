# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import UserList

class UserListAdmin(admin.ModelAdmin):
    list_display = ['username', 'auth_key']
    search_fields = ['username']
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_save_permission(self, request, obj=None):
        return False

admin.site.register(UserList, UserListAdmin)
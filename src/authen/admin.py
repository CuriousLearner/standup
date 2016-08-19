from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from .models import User, Address
# -*- coding: utf-8 -*-

# Third Party Stuff
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

# Register your models here.


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    add_form_template = 'admin/auth/user/add_form.html'
    model = User
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('date_joined', 'last_login')
    list_display = ('email', 'first_name', 'last_name', 'is_active')
    list_filter = ('is_superuser', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('email',)


admin.site.register(Address)

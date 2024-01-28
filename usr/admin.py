
# # Register your models here.
# from django.contrib import admin
# from .models import *


# class UsrAdmin(admin.ModelAdmin):
#     list_display = ('id_usr', 'no_telpn')
#     search_fields = ('id_usr', 'no_telpn')


# class UsrOutlet(admin.ModelAdmin):
#     list_display = ('outlet', 'usr')
#     search_fields = ('outlet', 'usr')


# admin.site.register(Usr, UsrAdmin)
# admin.site.register(UsrOutletProfile, UsrOutlet)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser ,UserOutlet

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'is_block', 'is_active', 'is_staff', 'date_joined')
    search_fields = ('username',)
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )


class UserOutletAdmin(admin.ModelAdmin):
    list_display = ('usr', 'outlet')
    # search_fields = ('usr__username', 'outlet__name')
    # list_filter = ('usr__is_active', 'outlet__is_active')

    # Customize other settings as needed

admin.site.register(UserOutlet, UserOutletAdmin)

admin.site.register(CustomUser, CustomUserAdmin)


# Register your models here.
from django.contrib import admin
from .models import *


class UsrAdmin(admin.ModelAdmin):
    list_display = ('id_usr', 'no_telpn')
    search_fields = ('id_usr', 'no_telpn')


class UsrOutlet(admin.ModelAdmin):
    list_display = ('outlet', 'usr')
    search_fields = ('outlet', 'usr')


admin.site.register(Usr, UsrAdmin)
admin.site.register(UsrOutletProfile, UsrOutlet)

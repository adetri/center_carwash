from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Outlet


class OutletAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'endpoin', 'alamat', 'no_telpn')
    search_fields = ('name', 'alamat', 'no_telpn__e164')


admin.site.register(Outlet, OutletAdmin)

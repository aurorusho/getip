from django.contrib import admin
from .models import IpStorage


class IpStorageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )

admin.site.register(IpStorage, IpStorageAdmin)
from django.contrib import admin

from .models import (
    AppStoreItem,
    Plattform,
    AppImage,
    ApiVersion,
    Version,
    Vendor
)

admin.site.register(AppStoreItem)
admin.site.register(Plattform)
admin.site.register(AppImage)
admin.site.register(ApiVersion)
admin.site.register(Version)
admin.site.register(Vendor)

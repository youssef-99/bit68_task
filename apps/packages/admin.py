from django.contrib import admin

from django.contrib import admin
from .models import Package


class PackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']  # Displayed columns in the list view
    search_fields = ['name']  # Enable search by name
    ordering = ['price']  # Order by price


admin.site.register(Package, PackageAdmin)

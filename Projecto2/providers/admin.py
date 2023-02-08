from django.contrib import admin

from providers.models import Providers

@admin.register(Providers)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email')
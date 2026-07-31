from django.contrib import admin
from .models import BusinessCard, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "mobile_number", "contact_date")
    list_display_links = ("id", "name")
    search_fields = ("name", "mobile_number")
    list_per_page = 25


admin.site.register(BusinessCard)
admin.site.register(Contact, ContactAdmin)

from django.contrib import admin
from .models import OwnerInfoModel, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "mobile_number", "contact_date")
    list_display_links = ("id", "name")
    search_fields = ("name", "mobile_number")
    list_per_page = 25


admin.site.register(OwnerInfoModel)
admin.site.register(Contact, ContactAdmin)

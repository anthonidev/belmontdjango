from django.contrib import admin
from .models import ListContact, Contact, ListItemContact, Campaign


class ListItemClientInline(admin.TabularInline):
    model = ListItemContact
    fields = ['contact', ]


class ListClientAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    inlines = [ListItemClientInline]


admin.site.register(ListContact, ListClientAdmin)
# admin.site.register(ListClient)
admin.site.register(Contact)
admin.site.register(Campaign)

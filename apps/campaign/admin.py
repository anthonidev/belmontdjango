from django.contrib import admin
from .models import ListClient, Client, ListItemClient


class ListItemClientInline(admin.TabularInline):
    model = ListItemClient
    fields = ['client', ]


class ListClientAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    inlines = [ListItemClientInline]


admin.site.register(ListClient, ListClientAdmin)
# admin.site.register(ListClient)
admin.site.register(Client)

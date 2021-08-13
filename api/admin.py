from django.contrib import admin

from api.models import Deal


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('username', 'item', 'total', 'quantity', 'date', )
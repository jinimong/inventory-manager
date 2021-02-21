from django.contrib import admin

from .models import Store, Event, InventoryChange

admin.site.register(Store)
admin.site.register(Event)
admin.site.register(InventoryChange)

from django.contrib import admin
from .models import Court


@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    list_display = ('courtID', 'num_availability',
                    'availabilityTag', 'address')
    list_filter = ('availabilityTag',)
    search_fields = ('address',)

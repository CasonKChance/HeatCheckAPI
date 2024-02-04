from django.contrib import admin
from .models import Court


@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    list_display = ('courtID', 'title', 'availability',
                    'address', 'availabilityTag')
    list_filter = ('availability', 'availabilityTag')
    search_fields = ('title', 'address')
    ordering = ('courtID',)

    fieldsets = (
        (None, {'fields': ('title', 'availability', 'num_availability',
         'availabilityTag', 'address', 'court_image')}),
    )

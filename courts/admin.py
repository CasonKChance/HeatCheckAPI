from django.contrib import admin
from .models import Court


@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    list_display = ('courtID', 'title', 'availability',
                    'address')
    list_filter = ('availability',)
    search_fields = ('title', 'address')
    ordering = ('courtID',)

    fieldsets = (
        (None, {'fields': ('title', 'availability', 'num_availability',
                           'address', 'court_image')}),
    )

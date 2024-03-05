from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser


class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ('emailAddress', 'firstName', 'lastName', 'position')
    search_fields = ('emailAddress', 'firstName', 'lastName')
    list_filter = ('position', 'skillLevel', 'ageGroup')
    ordering = ('emailAddress',)

    fieldsets = (
        (None, {'fields': ('emailAddress', 'password')}),
        ('Personal Info', {'fields': ('firstName', 'lastName', 'position',
                                      'hometown', 'skillLevel', 'height', 'weight', 'ageGroup', 'playType')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('emailAddress', 'password1', 'password2'),
        }),
    )

    readonly_fields = ('playerID',)

    # Additional list filters, if needed
    # list_filter = ('position', 'skillLevel', 'ageGroup', 'is_staff', 'is_superuser')

    # Additional list display fields, if needed
    # list_display = ('emailAddress', 'firstName', 'lastName', 'position', 'is_staff', 'is_superuser')

    # Customize the ordering, if needed
    # ordering = ('emailAddress',)

admin.site.register(CustomUser, CustomUserAdmin)
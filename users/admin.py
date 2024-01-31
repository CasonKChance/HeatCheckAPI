from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ['emailAddress', 'firstName', 'lastName', 'playerID']
    ordering = ('emailAddress',)  # Changed from 'username' to 'emailAddress'

    # Update list_filter based on the fields in your CustomUser model
    list_filter = ('is_staff', 'is_active',) if hasattr(
        CustomUser, 'is_staff') else ()
    # ... [rest of your admin class] ...


admin.site.register(CustomUser, UserAdmin)

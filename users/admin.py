from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('playerID', 'firstName', 'lastName',
                    'emailAddress', 'age', 'skill_level', 'position')
    search_fields = ('firstName', 'lastName', 'emailAddress')

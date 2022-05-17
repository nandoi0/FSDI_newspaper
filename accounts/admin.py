from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, UserType, Language
from .forms import CustomUserCreationFrom, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationFrom
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email', 'username',
        'usert_type', 'preffered_language',
        'is_staff'
    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type', 'preferred_language')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type', 'preferred_language')}),
    )

admin.site.register(CustomUser)
admin.site.register(UserType)
admin.site.register(Language)

# Register your models here.

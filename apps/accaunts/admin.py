from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from apps.accaunts.models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # model = User
    list_display = ('phone', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('phone', 'email', 'first_name', 'last_name')
    ordering = ('phone',)
    readonly_fields = ('date_joined',)

    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'photo')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2', 'groups'),
        }),
    )

    # Define which fields will be used when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2', 'first_name', 'last_name', 'email', 'photo', 'is_staff', 'is_superuser', 'is_active', 'groups'),
        }),
    )

    # To display full name in the list display
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = 'Full Name'

# admin.site.register(User, UserAdmin)

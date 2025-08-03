from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Create a tuple of the fields you want to include in the fieldsets
# This defines the sections and fields on the user edit page in the admin
fieldsets = (
    (None, {'fields': ('email', 'password')}), # Basic user info
    ('Personal info', {'fields': ()}), # You can add first_name, last_name here if you add them to CustomUser
    ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'is_app_active')}), # Include your custom flag
    ('Important dates', {'fields': ('last_login',)}), # last_login is from AbstractBaseUser
)

# Create a tuple of the fields you want to include in the add_fieldsets
# This defines the sections and fields on the user creation page in the admin
add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'is_active', 'is_staff', 'is_superuser', 'is_app_active'), # Include your custom flag
    }),
)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Custom Admin interface for CustomUser model.
    Inherits from Django's UserAdmin to maintain standard user management features.
    """
    # Override the default UserAdmin fieldsets with your custom ones
    fieldsets = fieldsets
    add_fieldsets = add_fieldsets

    # Fields to display in the user list view
    list_display = ('email', 'is_staff', 'is_active', 'is_app_active')

    # Fields to use for filtering in the user list view
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'is_app_active')

    # Fields to use for searching in the user list view
    search_fields = ('email',)

    # Ordering for the user list view
    ordering = ('email',)

    # Ensures that 'password' is only handled by set_password, not directly editable
    filter_horizontal = ('groups', 'user_permissions',) # For many-to-many fields
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User, Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    inlines = (ProfileInline,)
    list_display = ('email', 'is_staff', 'is_active', 'is_app_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'is_app_active')
    search_fields = ('email',)
    ordering = ('email',)
    readonly_fields = ('last_login',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {
            'fields': (
                'is_staff', 'is_active', 'is_superuser',
                'is_app_active',  # ✅ Add this line
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser', 'is_app_active')}
        ),
    )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return super().get_inline_instances(request, obj)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_name', 'phone', 'avatar', 'birth_date')

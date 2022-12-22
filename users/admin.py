from django.contrib import admin

from .models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    filter_horizontal = (
        "groups",
        "user_permissions",
    )  # Properly show m2m relations like permissions and groups

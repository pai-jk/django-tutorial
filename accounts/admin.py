from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser


# Register your models here.

# Register your models here.
class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserCreationForm
    model = CustomUser
    list_display = ["email", "username", "region"]


admin.site.register(CustomUser, CustomUserAdmin)
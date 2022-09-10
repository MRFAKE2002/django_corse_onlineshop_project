from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# admin.site.register(CustomUser, CustomUserAdmin)
# username = roozbeh password = roozbehbadali1381
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserChangeForm
    FORM = CustomUserCreationForm
    list_display = ('email', 'username', )
    

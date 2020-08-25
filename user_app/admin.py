# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     list_display = ('email', 'username', 'display_name', 'age',
#                     'homepage')
#     search_fields = ('email', 'username', 'display_name', 'age')
#     readonly_fields = ('date_joined', 'last_login')
#
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()

admin.site.register(CustomUser)
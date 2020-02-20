from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import AccountUser,Role
# Register your models here.

class AccountInLine(admin.StackedInline):
    model = AccountUser
    can_delete = False
    verbose_name_plural = 'Account'
    list_display = ("user_name", "role")

class UserAdmin(BaseUserAdmin):
    
    inlines = (AccountInLine,)


admin.site.unregister(User)
admin.site.register(Role)
admin.site.register(User, UserAdmin)
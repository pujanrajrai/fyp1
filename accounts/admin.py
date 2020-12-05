from django.contrib import admin
from .models import MyUser


# Register your models here.
@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['organization_name', 'email', 'is_active', 'is_admin']
    readonly_fields = ['organization_name']
    search_fields = ['email', 'organization_name']

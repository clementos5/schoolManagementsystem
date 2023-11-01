# apps/corecode/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import AcademicSession, AcademicTerm, SiteConfig, StudentClass, Subject
from apps.finance.models import Invoice, InvoiceItem, Receipt

# Custom Admin Site
class CustomAdminSite(admin.AdminSite):
    site_header = 'Saint Ignatius High School Management Site'
    site_title = 'Welcome, Headmaster'

custom_admin_site = CustomAdminSite(name='customadmin')

# Register Corecode Models
custom_admin_site.register(AcademicSession)
custom_admin_site.register(AcademicTerm)
custom_admin_site.register(SiteConfig)
custom_admin_site.register(StudentClass)
custom_admin_site.register(Subject)
custom_admin_site.register(Invoice)
custom_admin_site.register(InvoiceItem)
custom_admin_site.register(Receipt)

# Extend the UserAdmin class
class CustomUserAdmin(BaseUserAdmin):
    # Customize the user list display
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

# Unregister the default UserAdmin
admin.site.unregister(User)

# Register User with the extended CustomUserAdmin
admin.site.register(User, CustomUserAdmin)

# finance/admin.py
from django.contrib import admin
from django.contrib.auth.models import User  # Add this line to import User
from apps.corecode.models import AcademicSession, AcademicTerm, SiteConfig, StudentClass, Subject
from .models import Invoice, InvoiceItem, Receipt

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

# Register Finance Models
class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem

class ReceiptInline(admin.TabularInline):
    model = Receipt

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemInline, ReceiptInline]
    list_display = ('id', 'student', 'session', 'term', 'class_for', 'balance_from_previous_term', 'status', 'balance')
    search_fields = ('student__username',)  # Replace with the actual field you want to search

@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'invoice', 'description', 'amount')  # Adjust these based on your model fields
    search_fields = ('invoice__student__username',)  # Replace with the actual field you want to search

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('id', 'invoice', 'amount_paid', 'date_paid', 'comment')  # Adjust these based on your model fields
    search_fields = ('invoice__student__username',)  # Replace with the actual field you want to search

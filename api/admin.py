from django.contrib import admin

# Register your models here.

from django.contrib.auth.models import Permission
from django.contrib.admin.models import LogEntry

from .models import Organization, Product

# Django Permission and Logs
admin.site.register(LogEntry)
admin.site.register(Permission)

# Our Models
admin.site.register(Organization)
admin.site.register(Product)
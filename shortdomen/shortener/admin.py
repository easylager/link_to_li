from django.contrib import admin
from .models import Domain

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    fields = ['link', 'short_link', 'user']


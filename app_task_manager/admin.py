from django.contrib import admin
from .models import Assignment


class AccountAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'created_at', 'updated_at']

admin.site.register(Assignment, AccountAdmin)




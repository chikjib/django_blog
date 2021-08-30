from accounts.models import Support
from django.contrib import admin

class SupportAdmin(admin.ModelAdmin):
    list_display = ('user','email','phone_no','body','created_at')
    ordering = ['created_at']
    list_filter = ['created_at']
    search_fields = ['user','email']
    
admin.site.register(Support,SupportAdmin)
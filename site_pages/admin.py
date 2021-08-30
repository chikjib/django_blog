from site_pages.models import About, Advertise, Contact, Privacy, Terms
from django.contrib import admin
from django.utils.html import mark_safe
from django.template.defaultfilters import truncatechars


class AboutAdmin(admin.ModelAdmin):
    list_display = ('get_page_content',)
    
    def get_page_content(self,instance):
        return mark_safe(truncatechars(instance.page_content,1000))
    get_page_content.short_description = "Page Content"
    
class AdvertiseAdmin(admin.ModelAdmin):
    list_display = ('get_page_content',)
    
    def get_page_content(self,instance):
        return mark_safe(truncatechars(instance.page_content,1000))
    get_page_content.short_description = "Page Content"
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('get_page_content',)
    
    def get_page_content(self,instance):
        return mark_safe(truncatechars(instance.page_content,1000))
    get_page_content.short_description = "Page Content"
    
class PrivacyAdmin(admin.ModelAdmin):
    list_display = ('get_page_content',)
    
    def get_page_content(self,instance):
        return mark_safe(truncatechars(instance.page_content,1000))
    get_page_content.short_description = "Page Content"
    
class TermsAdmin(admin.ModelAdmin):
    list_display = ('get_page_content',)
    
    def get_page_content(self,instance):
        return mark_safe(truncatechars(instance.page_content,1000))
    get_page_content.short_description = "Page Content"


admin.site.register(About,AboutAdmin)
admin.site.register(Advertise,AdvertiseAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Privacy,PrivacyAdmin)
admin.site.register(Terms,TermsAdmin)

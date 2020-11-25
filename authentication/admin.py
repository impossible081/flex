# My django imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# My app imports
from authentication.models import Customer, EmailSendCount

class CustomerAdmin(UserAdmin):
    list_display = ('email', 'fullname', 'phoneNumber', 'date_joined', 'last_login', 'is_active', 'is_staff', )
    search_fields = ('email', 'fullname', 'phoneNumber',)
    ordering = ('email',)
    readonly_fields = ('date_joined', 'last_login',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(EmailSendCount)

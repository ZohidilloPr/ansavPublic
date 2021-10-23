from django.contrib import admin
from .models import UserProfile
# Register your models here.

class NameAdmin(admin.ModelAdmin):
    list_display = ('user','image')

admin.site.register(UserProfile, NameAdmin)

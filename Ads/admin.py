from django.contrib import admin
from .models import Category, ItemName, Images
# Register your models here.

class NameAdmin(admin.ModelAdmin):
    list_display = ('name','add_date')

admin.site.register(Category, NameAdmin)

class ItemNameAdmin(admin.ModelAdmin):
    list_display = ('creater','name','image', 'region')

admin.site.register(ItemName, ItemNameAdmin)

class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'itemname', 'images',)
    
admin.site.register(Images, ImagesAdmin)

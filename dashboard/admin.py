from django.contrib import admin
from .models import Images, Location, Category


class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('categories',)
    list_display = ('image_url','admin_image')
# Register your models here.
admin.site.register(Location)
admin.site.register(Images,admin_class=ImageAdmin)
admin.site.register(Category)
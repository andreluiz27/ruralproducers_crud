from django.contrib import admin

# Register your models here.
from .models import Farm

admin.site.register(Farm)

# adding field to display
class FarmAdmin(admin.ModelAdmin):
    list_display = ('farm_name', 'farm_area', 'vegetation_area', 'created_at', 'updated_at')
    search_fields = ('farm_name', 'farm_area', 'vegetation_area')
    list_filter = ('farm_name', 'farm_area', 'vegetation_area')

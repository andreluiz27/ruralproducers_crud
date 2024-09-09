from django.contrib import admin

# Register your models here.
from .models import RuralProducer

admin.site.register(RuralProducer)

# adding field to display
class RuralProducerAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'cpf', 'city', 'state', 'farm', 'created_at', 'updated_at')
    search_fields = ('name', 'cpf', 'city', 'state', 'farm')
    list_filter = ('name', 'cpf', 'city', 'state', 'farm')
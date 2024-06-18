from django.contrib import admin
from jeans.models import JeansStore
# Register your models here.
class JeansStoreAdmin(admin.ModelAdmin):
    list_display = ('brand', 'price', 'quantity')

admin.site.register(JeansStore, JeansStoreAdmin)
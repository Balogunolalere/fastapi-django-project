from django.contrib import admin

# Register your models here.
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'description', 'image', 'timestamp')
    list_filter = ('name', 'price', 'description', 'image', 'timestamp')
    search_fields = ('name', 'price', 'description', 'image')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Item, ItemAdmin)

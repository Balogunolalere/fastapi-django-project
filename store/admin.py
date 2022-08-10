from django.contrib import admin

# Register your models here.
from .models import Item, UpdateItem

class InlineUpdateItem(admin.TabularInline):
    model = UpdateItem
    extra = 1

class ItemAdmin(admin.ModelAdmin):
    inlines = [InlineUpdateItem]
    list_display = ('name', 'price', 'description', 'image', 'slug')
    list_filter = ('name', 'price', 'description', 'image', 'slug')
    search_fields = ('name', 'price', 'description', 'image', 'slug')
    ordering = ('name', 'price', 'description', 'image', 'slug')



admin.site.register(Item, ItemAdmin)
admin.site.register(UpdateItem)

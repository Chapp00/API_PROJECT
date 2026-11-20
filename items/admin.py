from django.contrib import admin
from .models import Category, Item, Claim

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin): 
    list_display = ('id', 'name', 'category', 'reporter', 'item_type', 'status', 'date_occurred')
    list_filter = ('category', 'item_type', 'status')
    search_fields = ('name', 'description', 'location')

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'claimant', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('explanation',)

list_filter = ('status')
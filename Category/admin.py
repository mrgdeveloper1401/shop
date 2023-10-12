from django.contrib import admin
from .models import CategoryModel, SubCategoryModel


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('create_at','update_at', 'name')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(SubCategoryModel)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    list_filter = ('create_at','update_at', 'name')
    prepopulated_fields = {'slug': ('name',)}
from django.contrib import admin

from images.models import Image
# Register your models here.


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

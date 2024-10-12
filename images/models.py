from hashlib import sha1
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import CreateMixin, UpdateMixin


# Create your models here.

class Image(CreateMixin, UpdateMixin):
    image_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/posts/%Y/%m/%d/', height_field="image_height", width_field="image_width")
    image_height = models.PositiveIntegerField(default=0)
    image_width = models.PositiveIntegerField(default=0)
    image_hash = models.CharField(_("image hash"), max_length=40, blank=True, null=True)
    image_size = models.PositiveIntegerField(default=0)
    image_name = models.CharField(_("image name"), max_length=255, blank=True, null=True)

    @property
    def get_image_address(self):
        return self.image.url

    @property
    def generate_hash(self):
        hasher = sha1()
        for c in self.image.chunks():
            hasher.update(c)
        return hasher.hexdigest()

    def save(self, *args, **kwargs):
        self.image_hash = self.generate_hash
        self.image_size = self.image.size
        # self.image.name = self.image_name
        return super().save(*args, **kwargs)

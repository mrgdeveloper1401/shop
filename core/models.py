from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now


class CreateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UpdateMixin(models.Model):
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDeleteMixin(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.deleted_at = now()
        self.is_deleted = True
        self.save(*args, **kwargs)

    class Meta:
        abstract = True

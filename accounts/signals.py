from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User, Otp


@receiver(post_save, sender=User)
def create_otp_code(sender, instance, created, **kwargs):
    if created:
        Otp.objects.create(
            user=instance,
        )

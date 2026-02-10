from django.contrib.auth.models import User
from signalapp.models import Profile
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('****************')
        print('Profile created!')
        print('****************')


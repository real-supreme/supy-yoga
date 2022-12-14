from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProfileModel as Profile, UserModel as User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("create_profile", instance, created)
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     print("save_profile", instance)
#     instance.profile.save()

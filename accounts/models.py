from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    The users profile information
    """
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    about_me = models.TextField()
    nationality = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.png', upload_to='img')

    def __unicode__(self):
        return f'{self.user.username} Profile'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
    def __unicode__(self):
        return self.title

    
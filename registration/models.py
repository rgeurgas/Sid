from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from course.models import Course

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	university = models.CharField(max_length=50, null=True, blank=True)
	courses = models.ManyToManyField(Course, blank=True)
	bio = models.TextField(default=" ")
	image = models.ImageField(upload_to='profile/pictures/', default="profile/pictures/default.webp")
	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	try:
		instance.profile.save()
	except:
		profile = Profile.objects.create(user=instance)	
		profile.save()

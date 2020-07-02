from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django import forms
from django.dispatch import receiver
# Create your models here.
from PIL import Image

class Profile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	image=models.ImageField(default='default.jpeg',upload_to='photos')

	def __str__(self):
		return self.user.username

	# def save(self):
	# 	# super().save(self)

	# 	img=Image.open(self.image.path)
	# 	if img.height> 300 or img.width >300:
	# 		output=(300,300)
	# 		img.thumbnail(output)
	# 		img.save(self.image.path)


class ProfileUpdate(forms.ModelForm):
	class Meta:
		model=Profile
		fields =['image']



@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=User) 
def save_profile(sender, instance, **kwargs):
		instance.profile.save()
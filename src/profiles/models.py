from django.db import models

# Create your models here.

class Profile(models.Model):
	"""docstring for Profile"""
	name = 'Model'
	def __unicode__(self):
		return self.name
		
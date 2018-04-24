from django.db import models

# Create your models here.

class Profile(models.Model):
	"""docstring for Profile"""
	name = 'Model'
	def __unicode__(self):
		return self.name


class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        )
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
        )

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)

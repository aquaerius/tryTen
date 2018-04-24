from django.contrib import admin
from .models import Student, Profile

#Register the model in the admin site
# Use: admin.site.register(<YOUR MODEL>)

admin.site.register(Student)
admin.site.register(Profile)

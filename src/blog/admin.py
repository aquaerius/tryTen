from django.contrib import admin
from .models import Post, Comment

#Register the Post model in the admin site
admin.site.register(Post)
admin.site.register(Comment)

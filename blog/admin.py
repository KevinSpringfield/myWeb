from django.contrib import admin
from .models import Post
#註冊models到admin
admin.site.register(Post)
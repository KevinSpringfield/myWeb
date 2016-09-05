from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    def publish(self):
        self.save()

    def __str__(self):
        return self.title
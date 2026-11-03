from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    permissions = models.CharField(default="user") # "user", "curator" y "admin" deben ser los únicos disponibles

    def __str__(self):
        return f"{self.user.username}"

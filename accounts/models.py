from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass


class NewsletterSub(models.Model):
    is_active = models.BooleanField(default=True)
    email = models.EmailField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

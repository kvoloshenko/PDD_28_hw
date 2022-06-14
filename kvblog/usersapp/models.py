from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class BlogUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_dbAdmin = models.BooleanField(default=False)
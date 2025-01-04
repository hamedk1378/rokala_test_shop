from django.db import models
from django.contrib.auth.models import AbstractUser

class AccountsUser(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.
    Username and password are required. Other fields are optional.
    """
    is_admin= models.BooleanField(default=False)
    region= models.CharField(max_length=256, default="IRI")


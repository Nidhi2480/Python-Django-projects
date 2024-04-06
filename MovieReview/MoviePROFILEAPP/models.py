from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=True)
    Profile=models.ImageField(upload_to='profile',blank=True)
    Bio=models.CharField(max_length=250)
    Preference=models.CharField(max_length=250)
    DOB=models.DateField(default=timezone.now)
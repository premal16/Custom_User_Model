from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=15)

    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    


    def __str__(self):
        return self.username
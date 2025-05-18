from django.db import models

# Create your models here.
# main/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField("Номер телефона", max_length=20, unique=True)
    email = models.EmailField("Электронная почта", unique=True)



    def __str__(self):
        return self.username
from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class Profile(models.Model):
    phone = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Address(models.Model):
    profile = models.ForeignKey(Profile, on_delete=CASCADE)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=4)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.profile}-{self.street}'


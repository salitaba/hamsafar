from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cash = models.IntegerField(default=0)

    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
    )


class RequestTravel(models.Model):
    status_choises = [
        ('pending', 'pending'),
        ('accepted', 'accepted'),
    ]

    lat = models.DecimalField(max_digits=15, decimal_places=13)
    long = models.DecimalField(max_digits=15, decimal_places=13)
    status = models.CharField(max_length=10, choices=status_choises)

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )


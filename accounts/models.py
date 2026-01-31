from django.conf import settings
from django.db import models

STATE_CHOICES = [
    ("ACT", "ACT"), ("NSW", "NSW"), ("NT", "NT"), ("QLD", "QLD"),
    ("SA", "SA"), ("TAS", "TAS"), ("VIC", "VIC"), ("WA", "WA"),
]

GENDER_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
]

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    notes = models.TextField(blank=True)

    first_name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)

    address = models.CharField(max_length=255)
    suburb = models.CharField(max_length=120)
    postcode = models.CharField(max_length=10)
    state = models.CharField(max_length=3, choices=STATE_CHOICES)

    phone_number = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"{self.user.username} profile"

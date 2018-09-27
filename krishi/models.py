from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    aadhaar = models.CharField(max_length=12)
    mobile = models.CharField(max_length=10)
    address_id = models.IntegerField()

    def __str__(self):
        return self.aadhaar

class Address(models.Model):
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    locality = models.CharField(max_length=20)
    sub_locality = models.CharField(max_length=20)
    pin = models.CharField(max_length=6)
    house_no = models.CharField(max_length=20)

    def __str__(self):
        return self.city + " " + self.state

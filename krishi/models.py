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


class Data(models.Model):
    crop_name=models.CharField(max_length=20)
    days=models.CharField(max_length=20)
    crop_diseases=models.CharField(max_length=255)
    current_price=models.CharField(max_length=30)
    fungicides=models.CharField(max_length=50)
    herbicides=models.CharField(max_length=50)
    seed_treatment=models.CharField(max_length=255)
    planting_teachnique=models.TextField()
    information=models.TextField()




class Mandi(models.Model):
    state=models.CharField(max_length=20)
    mandi=models.CharField(max_length=20)

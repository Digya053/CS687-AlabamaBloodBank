from django.db import models
from django.db.models.lookups import GreaterThan, GreaterThanOrEqual, LessThanOrEqual

# Create your models here.
class RegisteredUsers(models.Model):
    fname = models.CharField(max_length=20)
    mnit = models.CharField(max_length=1)
    lname = models.CharField(max_length=20)
    ssn = models.IntegerField(max_length=9)
    dob = models.DateField()
    city = models.CharField(max_length=15)
    blood_type = models.CharField(max_length=3)
    gender = models.CharField(max_length=1)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=300)
    weight_in_lbs = models.IntegerField(max_length=3)
    height_in_lbs = models.IntegerField(max_length=2)
    hmembership_no = models.IntegerField(max_length=1)

    def __str__(self):
        return str(self.ssn)

class Blood(models.Model):
    blood_id = models.CharField(max_length=2)
    available_from = models.DateField()
    d_gender = models.CharField(max_length=1)
    d_weight = models.IntegerField(max_length=3)
    d_height = models.IntegerField(max_length=2)
    d_age = models.IntegerField(max_length=2)
    ssn = models.ForeignKey(RegisteredUsers, on_delete=models.CASCADE)
    organizer_id = models.CharField(max_length=3)
    storage_id = models.CharField(max_length=4)

    def __str__(self):
        return self.blood_id






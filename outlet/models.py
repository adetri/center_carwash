from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Outlet(models.Model):
    name = models.CharField(max_length=99)
    endpoin = models.CharField(unique=True)
    alamat = models.TextField()
    slug = models.CharField(unique=True)
    no_telpn = models.CharField(max_length=14)

    def __str__(self):
        return "id: ({}) nama:({}) ".format(self.id, self.name)

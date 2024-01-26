from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from outlet.models import Outlet
# Create your models here.


class Usr(models.Model):
    id_usr = models.PositiveIntegerField()
    no_telpn = models.CharField(max_length=14, unique=True, default=0)

    def __str__(self):
        return "id: ({}) ".format(self.id)


class UsrOutletProfile(models.Model):
    outlet = models.ForeignKey(Outlet, on_delete=models.SET_NULL, null=True)
    usr = models.ForeignKey(Usr, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "id: ({}) ".format(self.id)

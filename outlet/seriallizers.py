from rest_framework import serializers
from .models import *


class OutletSeriallizers(serializers.ModelSerializer):
    class Meta:
        model = Outlet
        fields = '__all__'

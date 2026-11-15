from rest_framework import serializers
from .models import UpscUser

class UpscSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpscUser
        fields = ['username','password','userId','email']
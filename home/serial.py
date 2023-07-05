from .models import  *
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User





class locationSerial(serializers.ModelSerializer):
    class Meta:
        model = location 
        fields = '__all__'

class adSerial(serializers.ModelSerializer):
    class Meta:
        model = ad 
        fields = '__all__'
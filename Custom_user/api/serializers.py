from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','username','email','password','city','pincode','mobile_number')
        extra_kwargs = {'password': {'write_only': True}}



    def create(self, validated_data):
        validated_data['password']= make_password(validated_data['password'])
        return super().create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields =['email', 'password']
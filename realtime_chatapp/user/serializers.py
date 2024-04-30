from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework import generics, status
class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()


    def validate(self, data):

        user = authenticate(**data)
       
        if user:
            return user
        raise serializers.ValidationError('Incorrect Credentials')


class UserSerializer(serializers.ModelSerializer):
    	class Meta:
            model = User
            fields = "__all__"



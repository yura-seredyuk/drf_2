from rest_framework import serializers
from .models import UserList

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserList
        fields =['id', 'username', 'email']
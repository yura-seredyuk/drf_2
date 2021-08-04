from rest_framework import serializers
from .models import UserList, Address
      

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields =['id', 'country', 'city', 'zip_code', 'street', 'apartament' ]



class UsersSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = UserList
        fields =['id', 'username', 'email', 'address']
    
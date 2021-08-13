from rest_framework import serializers
from .models import UserList, Address
from .validator import AddressValidator
      

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields =['id', 'country', 'city', 'zip_code', 'street', 'apartament' ]
        # fields = '__all__'
        validators = [AddressValidator()]

    
    def create(self, validated_data):
        # print("validated_data:",validated_data)
        result = Address.objects.create(**validated_data)
        return result
    
    def update(self, instance, validated_data):
        # print(validated_data, validated_data )
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.zip_code = validated_data.get('zip_code', instance.zip_code)
        instance.street = validated_data.get('street', instance.street)
        instance.apartament = validated_data.get('apartament', instance.apartament)
        instance.save()
        return instance

class UsersSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = UserList
        fields =['id', 'username', 'email', 'address']
    
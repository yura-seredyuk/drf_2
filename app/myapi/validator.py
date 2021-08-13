from rest_framework.utils.representation import smart_repr
from rest_framework import serializers
import re

class AddressValidator:
    message = 'Validation error: '
    def __init__(self, message=None):
        # self.data = validated_data
        self.validated_field = ''
        self.validated_data = None
        self.message = message or self.message

    def __call__(self, attrs):
        message = self.message
        if "zip_code" in attrs and len(str(attrs["zip_code"])) != 5:
            message = 'must contain 5 digits'
            self.raize_error(attrs, 'zip_code', message)
        elif "country" in attrs and len(attrs["country"]) < 3:
            message = 'must contain more letters'
            self.raize_error(attrs, 'country', message)
        elif "city" in attrs and  len(attrs["city"]) < 3:
            message = 'must contain more letters'
            self.raize_error(attrs, 'city', message)
        elif "street" in attrs and  len(re.findall(r'([A-z0-9]+ str\. [^0][A-z0-9]+$)',attrs["street"])) != 1:
            message = 'wrong street format. It must be like: Soborna str. 16'
            self.raize_error(attrs, 'street', message)
        elif "apartament" in attrs and  attrs['apartament'] == 0:
            message = 'cannot be zero'
            self.raize_error(attrs, 'apartament', message)

    def raize_error(self, attrs, field_name, message):
        message = self.message + f'The "%s" field %s.'%(field_name, message)
        self.validated_field = field_name
        self.validated_data = attrs[field_name]
        raise serializers.ValidationError(message, code=field_name)

    def __repr__(self):
        return '<%s(%s=%d)>' % (
            self.__class__.__name__,
            self.validated_field,
            self.validated_data
        )

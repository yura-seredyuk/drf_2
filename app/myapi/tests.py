from django.test import TestCase, Client
from rest_framework import status
import json
from django.urls import reverse
from .models import Address
from .serializers import AddressSerializer


# initialize the APIClient app
client = Client()


class GetAllAddressTest(TestCase):
    """ Test module for GET all address API """
    def setUp(self):
        self.addr = Address.objects.create(
            country = "Ukraine", city = "Rivne", zip_code = 33026, 
            street = "Soborna str. 16", apartament = 233)


    def test_get_all_address(self):
        # get API response
        response = client.get('http://127.0.0.1:8000/address/')
        # get data from db
        address = Address.objects.all()
        serializer = AddressSerializer(address, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleAddressTest(TestCase):
    """ Test module for GET single address API """

    def setUp(self):
        self.addr = Address.objects.create(
            country = "Ukraine", city = "Rivne", zip_code = 33026, 
            street = "Soborna str. 16", apartament = 233)
            
    def test_get_valid_single_address(self):
        response = client.get('/address/1/')
        address = Address.objects.get(pk=self.addr.pk)
        serializer = AddressSerializer(address)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_address(self):
        response = client.get('/address/100/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewAddressTest(TestCase):
    """ Test module for inserting a new puppy """

    def setUp(self):
        self.valid_adrdess = {
                'country':"Ukraine", 'city':"Rivne", 'zip_code': 33026, #
                'street':"Test_post str. 16", 'apartament':200}
        self.invalid_address = {
                'country':"", 'city':"Rivne", 'zip_code': 33026, 
                'street':"Test_post str. 16", 'apartament':233}

    def test_create_valid_address(self):
        response = client.post(
            '/address/',
            data=json.dumps(self.valid_adrdess),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_address(self):
        response = client.post(
            '/address/',
            data=json.dumps(self.invalid_address),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleAddressTest(TestCase):
    """ Test module for updating an existing address record """

    def setUp(self):
        self.addr = Address.objects.create(
            country = "Ukraine", city = "Rivne", zip_code = 33026, 
            street = "Test_update str. 16", apartament = 2003)
        self.valid_address = {"country": "Ukraine","city": "Rivne","zip_code": 33026,"street": "Soborna str. 16","apartament": 201}
        self.invalid_address = {'country':"", 'city':"Rivne", 'zip_code': 33026,'street':"Test_update str. 16", 'apartament':233}


    def test_valid_update_address(self):
        response = client.put(
            '/address/1/',
            data=json.dumps(self.valid_address),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_address(self):
        response = client.put(
            '/address/1/',
            data=json.dumps(self.invalid_address),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSinglePuppyTest(TestCase):
    """ Test module for deleting an existing puppy record """

    def setUp(self):
        self.addr = Address.objects.create(
            country = "Ukraine", city = "Rivne", zip_code = 33026, 
            street = "Soborna str. 16", apartament = 233)

    def test_valid_delete_address(self):
        response = client.delete('/address/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_address(self):
        response = client.delete('/address/2/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


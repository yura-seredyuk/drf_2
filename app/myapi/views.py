from rest_framework import viewsets

from .serializers import UsersSerializer, AddressSerializer
from .models import UserList, Address

class UsersViewSet(viewsets.ModelViewSet):
    queryset = UserList.objects.all().order_by('id')
    serializer_class = UsersSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all().order_by('id')
    serializer_class = AddressSerializer
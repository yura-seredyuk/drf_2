from rest_framework import viewsets

from .serializers import UsersSerializer
from .models import UserList

class UsersViewSet(viewsets.ModelViewSet):
    queryset = UserList.objects.all().order_by('id')
    serializer_class = UsersSerializer
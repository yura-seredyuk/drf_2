from rest_framework import viewsets, status

from django.http import Http404, response
from rest_framework.response import Response
from rest_framework.views import APIView



from .serializers import UsersSerializer, AddressSerializer
from .models import UserList, Address

class UsersViewSet(viewsets.ModelViewSet):
    queryset = UserList.objects.all().order_by('id')
    serializer_class = UsersSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all().order_by('id')
    serializer_class = AddressSerializer

# -------------
class AddressViev:

    class AddressList(APIView):
        """
        List all address, or create a new address.
        """
        def get(self, request, format=None):
            address = Address.objects.all()
            serializer = AddressSerializer(address, many=True)
            return Response(serializer.data)

        def post(self, request, format=None):
            serializer = AddressSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class AddressDetail(APIView):
        """
        Retrieve, update or delete an address instance.
        """
        
        def get_object(self, pk):
            try:
                return Address.objects.get(pk=pk)
            except Address.DoesNotExist:
                raise Http404

        def get(self, request, pk, format=None):
            address = self.get_object(pk)
            serializer = AddressSerializer(address)
            return Response(serializer.data)

        def put(self, request, pk, format=None):
            data = request.data 
            address = self.get_object(pk)
            serializer = AddressSerializer(address, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            address = self.get_object(pk)
            address.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

# get_object -> return user instance 
    # get data by username and/or email (unique parameters)
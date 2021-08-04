from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    street = models.CharField(max_length=100)
    apartament = models.IntegerField(null=True)

    def __str__(self):
        return self.city + ' ' + self.street

class UserList(models.Model):
    username = models.CharField(max_length=64)
    email = models.EmailField(max_length=320)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username

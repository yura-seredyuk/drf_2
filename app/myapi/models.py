from django.db import models

class UserList(models.Model):
    username = models.CharField(max_length=64)
    email = models.EmailField(max_length=320)

    def __str__(self):
        return self.username

from curses import meta
from itertools import count
from django.db import models


# User data storage
class FollowerCount(models.Model):
    name = models.CharField(max_length=110)
    count = models.IntegerField()

    def __str__(self):
        return self.name, self.count


# User Handle input table
class UserRequired(models.Model):
    list_of_users = models.CharField(max_length=1500)


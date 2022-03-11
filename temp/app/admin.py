from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(UserRequired)
admin.site.register(FollowerCount)
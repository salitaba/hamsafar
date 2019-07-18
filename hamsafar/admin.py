from django.contrib import admin

# Register your models here.

from hamsafar.models import Profile, Request

admin.site.register(Profile)
admin.site.register(Request)
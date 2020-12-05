from django.contrib import admin

# Register your models here.
from accounts.models import Profile, Address

admin.site.register(Profile)
admin.site.register(Address)
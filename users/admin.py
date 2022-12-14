from django.contrib import admin
from .models import ProfileModel, UserModel

admin.site.register(UserModel)
admin.site.register(ProfileModel)

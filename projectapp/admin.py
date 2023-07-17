from django.contrib import admin
from projectapp.models.auth import User,OTP
from projectapp.models.crm import Ishchi

# Register your models here.
admin.site.register(User)
admin.site.register(Ishchi)
admin.site.register(OTP)

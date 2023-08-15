from django.contrib import admin
from projectapp.models.auth import User,OTP
from projectapp.models.crm import Ishchi
from projectapp.models.follow import Post,Likes

# Register your models here.
admin.site.register(User)
admin.site.register(Ishchi)
admin.site.register(OTP)
admin.site.register(Post)
admin.site.register(Likes)

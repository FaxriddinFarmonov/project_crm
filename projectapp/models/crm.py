from django.db import models
from .auth import User
from django.dispatch import  Signal
from django.db.models.signals import post_save

class Ishchi(models.Model):
    name = models.CharField(max_length=50)
    familyasi = models.CharField(max_length=50)
    yoshi = models.IntegerField("yoshi")
    lavozimi = models.CharField(max_length=50)
    maosh = models.CharField(max_length=50)
    
    def __str__(self) :
        return self.name
    
# def create_profile(sender,instance,created, **kwargs):
#     print(f"sender {sender}\n instanse {instance}\n created {created}")
#     if created:
#         Ishchi.objects.create(
#             user=instance
#         )
    
# Signal.connect(post_save,create_profile)
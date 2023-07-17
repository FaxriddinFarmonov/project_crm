from django.db import models


class Ishchi(models.Model):
    name = models.CharField(max_length=50)
    familyasi = models.CharField(max_length=50)
    yoshi = models.IntegerField("yoshi")
    lavozimi = models.CharField(max_length=50)
    maosh = models.CharField(max_length=50)
    
    def __str__(self) :
        return self.name
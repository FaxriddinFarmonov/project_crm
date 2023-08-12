from django.db import models
from .auth import User


class Post(models.Model):
    name = models.CharField(max_length=250)
    body = models.TextField(default="not body")
    created = models.DateTimeField(auto_now_add=True,editable=False)
    image = models.ImageField(upload_to='media',null=True)
    like = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    


class Likes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,name='like')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,name='post')
from projectapp.models.follow import Post,Likes
from django.http import  HttpResponseRedirect
from django.urls import  reverse

def like(request,post_id):
    
    user = request.user
    post =  Post.objects.get(id=post_id)
    current_likes = post.like
    liked = Likes.objects.filter(user=user,post=post).count()
    
    if not liked:
        
        liked = Likes.objects.create(user=user,post=post)
        current_likes+=1
        
    else:
        liked = Likes.objects.filter(user=user,post=post).delete()
        current_likes-=1
    
    post.like = current_likes
    post.save()
    return HttpResponseRedirect(reverse('post_detail',args=[post_id]))
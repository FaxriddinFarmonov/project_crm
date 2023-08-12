from django.shortcuts import render,redirect
from projectapp.models.crm import Ishchi
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import  messages


@login_required(login_url="login")
def index(request):
    return render(request,'index.html')

def search_wor(request):
    
    if request.user.is_superuser:
        q = request.GET['q']
        
        multiple_q = Q(Q(name__icontains=q) |
                     Q(familyasi__icontains=q) | 
                     Q(lavozimi__icontains=q))
        
        worker = Ishchi.objects.filter(multiple_q)
        print(worker)
      
        ctx = {
            "i":worker
        }
        messages.success(request,'natijalar topilddi')
        
    else:
        messages.error(request,'natija topilmadi')
        return redirect('home')    
    return render(request,"search/search_worker.html",ctx)



from django.shortcuts import render,redirect
from projectapp.models.crm import Ishchi
from django.contrib.auth.decorators import login_required
from forms.ishchi_add import IshchiForm


@login_required(login_url="login")
def ishchi_list_delete(request,pk=None,delete_id=None):
    
    if delete_id:
        root = Ishchi.objects.filter(id=delete_id).first()
        if root:
            root.delete()
        return redirect("ishchi_list")
       
       
    
    if pk:
        root = Ishchi.objects.filter(id=pk).first()
        
        if  not root:
            return redirect("ishchi_list")
        
        ctx = {
            "root":root
        }
        return render(request,"ishchi/detail.html",ctx)
    
    ctx = {
        "ishchi" : Ishchi.objects.all().order_by("-pk")
    }
    return render(request,"ishchi/ishchi.html",ctx)


def wor_format(data:Ishchi):
    return {
        "id":data.pk,
        "name":data.name,
        "familyasi":data.familyasi,
        "yoshi":data.yoshi,
        "lavozimi":data.lavozimi,
        "maosh":data.maosh
    }
    

   

def add(request,pk=None):
    if pk:
        root = Ishchi.objects.get(id=pk)
        
    form = IshchiForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return redirect('ishchi_list')
    else:
        print(form.errors)
    return render(request,"ishchi/form.html",{'form':form})


def edit(request,pk):
    root = Ishchi.objects.filter(id=pk).first()
    print(root,'+++++++++++++++++++++++++++++++++++++++++++++++=====    ')
    if root:
        if request.POST:
            forms = IshchiForm(request.POST,request.FILES,instance=root)
            if forms.is_valid():
                forms.save()
                return redirect('ishchi_det',pk=root.id)
            else:
                print(forms.errors)
     
        
    else:
       return redirect("ishchi_list")
    form=IshchiForm(instance=root)        
    ctx = {
            "form":form
        }
    return render(request,"ishchi/form.html",ctx) 



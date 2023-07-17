from django.shortcuts import render
from projectapp.models.crm import Ishchi
from django.contrib.auth.decorators import login_required



@login_required(login_url="login")
def ishchi_list(request):
    ctx = {
        "ishchi" : Ishchi.objects.all()
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
from django.shortcuts import render,redirect
from projectapp.models.auth import User
from django.contrib.admin.views.decorators import staff_member_required



@staff_member_required(login_url="login")
def get_list(request):
    ctx = {
        "users" : User.objects.all()
    }
    return render(request,"users/user.html",ctx)


@staff_member_required(login_url="login")
def change_perm(request,pk,status=[0,1]):
    user = User.objects.filter(id=pk).first()
    if user and status in [0,1]:
        user.perm = True if status==1 else False
        user.save()
    return redirect("get_list")


    
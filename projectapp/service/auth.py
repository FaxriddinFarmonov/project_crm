from django.shortcuts import render,redirect
from projectapp.models.auth import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required



def sign_in(request):
    if not request.user.is_anonymous:
        return redirect("home")
    if request.POST:
        data = request.POST
        user = User.objects.filter(email=data["email"]).first()
        
        if not user:
            return render(request,"auth/login.html",{"error":"Parol yoki Email xato"})
         
        if not user.check_password(data["password"]): 
            return render(request,"auth/login.html",{"error":"Parol yoki Email xato"})
        
        if not user.is_active:
            return render(request,"auth/login.html",{"error":"Profile Ban Qilingan"})
        
        login(request,user)
        return redirect("home")

    return render(request,"auth/login.html")



def sign_up(request):
    
    if request.POST:
        data = request.POST
        user = User.objects.filter(email=data['email']).first()
        
        if user:
            return render(request,"auth/regis.html",{"error":"Siz kiritgan email band"})
        
        if data["pass"] != data["pass_conf"]:
            return render(request,"auth/regis.html",{"error":"Parollar mos kelmadi"})

        user=User.objects.create_user(email=data["email"],
                                      password=data["pass"],
                                      fname=data["name"],
                                      lname=data["familya"])
        authenticate(request)
        login(request,user)
        return redirect('home')
        
    return render(request,"auth/regis.html")


@login_required(login_url="login")
def sign_out(request):
    logout(request)
    return redirect("login")
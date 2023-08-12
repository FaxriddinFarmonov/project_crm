import random
import datetime
from base.helper import send_sms
from django.shortcuts import render,redirect
from projectapp.models.auth import User,OTP
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from methodism import code_decoder


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
        
        code = random.randint(100000,999999)
        # send_sms(998951808802,code)
        key = code_decoder(code)
        
        otp = OTP.objects.create(
            key=key,
            email=user.email,
            step='login',
            by=2
        )
        otp.save()
        
        request.session["id"]=user.id
        request.session["code"]=code
        request.session["email"]=user.email
        request.session["otp_token"]=otp.key
        
        return redirect("otp")

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

        # user=User.objects.create_user(email=data["email"],
        #                               password=data["pass"],
        #                               fname=data["name"],
        #                               lname=data["familya"]
        #                               )

           
        code = random.randint(100000,999999)
        # send_sms(998951808802,code)
        key = code_decoder(code)
        
        otp = OTP.objects.create(
            key=key,
            email=data["email"],
            step='regis',
            by=1,
            extra = {
                'email':data["email"],
                'password':data["pass"],
                'fname':data["name"],
                'lname':data["familya"]
            }
        ) 
        otp.save()
        

        request.session["code"]=code
        request.session["email"]=otp.email
        request.session["otp_token"]=otp.key
        
        return redirect("otp")
        authenticate(request)
        login(request,user)
        return redirect('home')
        
    return render(request,"auth/regis.html")


@login_required(login_url="login")
def sign_out(request):
    logout(request)
    return redirect("login")


def otp(request):
    
    if not request.session.get("otp_token"):
        return redirect("login")
    
    if request.POST:
        otp = OTP.objects.filter(key=request.session["otp_token"]).first()
        code = ''.join( x for x in  request.POST.getlist('otp'))
        
        if not code.isdigit():
            return render(request,"auth/otp.html",{"error":"Harflar kiritmang!!!"})

        if otp.is_expire:
            otp.step="faild"
            otp.save()
            return render(request,"auth/otp.html",{"error":"Token eskirgan!!!"})
        
        
        if (datetime.datetime.now()-otp.created).total_seconds()>=120:
            otp.is_expire=True
            otp.save()
            return render(request,"auth/otp.html",{"error":"Vaqt tugadi!!!"})
         
         
        if int(code_decoder(otp.key,decode=True,l=1)) != int(code):
            otp.tries +=1
            otp.save()
            return render(request,"auth/otp.html",{"error":"Cod hato!!!"})
        
        if otp.by==1:
            user = User.objects.create_user(**otp.extra)
            authenticate(request)
            otp.step = "registered"
           
            
        else:
            user = User.objects.get(id=request.session["id"])   
            otp.step = "logged"
        
       
        login(request,user)
        otp.save() 
        
        try:
            if 'user_id' in request.session:
                del request.session["id"]
            del request.session["code"]
            del request.session["email"]
            del request.session["otp_token"]
        except:
            pass


        return redirect("home")
    
    

    return render(request,"auth/otp.html")



def resent_otp(request):
    
    if not request.session.get("otp_token"):
        return redirect("login")

    old = OTP.objects.filter(key=request.session["otp_token"]).first()
    old.step = 'failed'
    old.is_expire = True
    old.save()
    
    
    code = random.randint(100000,999999)
    # send_sms(998951808802,code)
    key = code_decoder(code)
    
    
        
    otp = OTP.objects.create(
        key=key,
        email=old.email,
        step= 'login' if old.by == 2 else 'regis',
        by=old.by,
        extra=old.extra
    ) 
    otp.save()
        

    request.session["code"]=code
    request.session["email"]=otp.email
    request.session["otp_token"]=otp.key
        
    return redirect("otp")

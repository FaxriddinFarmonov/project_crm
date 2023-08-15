from django.urls import path
from .views import index,search_wor
from projectapp.service.ishchi import ishchi_list_delete,add,edit
from projectapp.service.auth import sign_in,sign_up,sign_out,otp,resent_otp
from projectapp.service.users import get_list,change_perm
from projectapp.worker.workerWiev import WorkerWiev


from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name="home"),
    path('ishchi/',ishchi_list_delete,name="ishchi_list"),
    path('det/<int:pk>/',ishchi_list_delete,name="ishchi_det"),
    path('del/<int:delete_id>/',ishchi_list_delete,name="ishchi_del"),
    path('add/',add,name="add"),
    path('edit/<int:pk>/',edit,name="edit"),

    
    #user
    path("login/",sign_in,name="login"),
    path("regis/",sign_up,name="regis"),
    path("logout/",sign_out,name="logout"),
    path("users/",get_list,name="get_list"),
    path("otp/",otp,name="otp"),
    path("resent/otp/",resent_otp,name="re-otp"),

    path("search/",search_wor,name="search_wor"),

    path("change_perm/<int:pk>/<int:status>/",change_perm,name="change_perm"),
    path("faxri/",WorkerWiev.as_view(),name="worker"),
    path("ishchisave/",WorkerWiev.as_view(),name="worker"),




]
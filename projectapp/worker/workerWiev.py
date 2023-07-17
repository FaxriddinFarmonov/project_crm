from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from projectapp.models.crm import Ishchi
from projectapp.service.ishchi import wor_format


class WorkerWiev(GenericAPIView):
    def get(self,request,*args, **kwargs):
        worker = Ishchi.objects.all()
        wor_list=[]
        for i in worker:
            wor_list.append(wor_format(i))
        ctx = {
            "result":wor_list
        }
        return Response(ctx)
    
    def post(self,request,*args, **kwargs):
        data = request.data
        ishchi = Ishchi.objects.create(name=data["name"],
                                       familyasi=data["familyasi"],
                                       yoshi=data["yoshi"],
                                       lavozimi=data["lavozimi"],
                                       maosh=data["maosh"]
                                       )
        ishchi.save()
       
        return Response(data)
from django.forms import model_to_dict
from django.http import JsonResponse, QueryDict
from django.views.generic import View
from .mysigal import mysigal

from .models import *

NOT_FOUND = 2
SUCCESS = 1

class AdminAPI(View):

    def get(self,req):
        a_id = int(req.GET.get("aid"))
        mysigal.send(sender="有钱人",pa1="川菜",pa2="在如家吃")
        try:
            res = MyAdmin.objects.get(pk=a_id)
        except:
            data = {
                'code':NOT_FOUND,
                'msg':"没有找到此ID对应的数据",
                'data':None
            }
            return JsonResponse(data)
        data = {
            'code':SUCCESS,
            'data':model_to_dict(res),
            'msg':'ok'
        }
        return JsonResponse(data)

    def post(self,req):
        a_id = int(req.POST.get("aid"))
        desc = req.POST.get("desc")
        res = MyAdmin.objects.create(
            user_id=a_id,
            desc = desc
        )
        data = {
            'code':SUCCESS,
            'msg':'created',
            'data':model_to_dict(res)
        }
        return JsonResponse(data)

    # def post(self,req):

    def put(self,req):
        return JsonResponse({"data":"hehe"})

    def delete(self,req):
        params = QueryDict(req.body)
        print(params)
        aid = params.get("aid")
        print(aid)
        MyAdmin.objects.get(pk=int(aid)).delete()
        data = {
            'code':SUCCESS,
            'msg':"deleted",
            'data':{
                "admin_id":aid
            }
        }
        return JsonResponse(data)
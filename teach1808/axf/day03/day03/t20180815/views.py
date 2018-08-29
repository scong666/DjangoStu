from django.shortcuts import render
from .models import *
# Create your views here.


# def search_by_name(req):
#     param = req.GET
#     #t_id = param.get("tid")
#     res = Language.objects.filter(
#         #name = t_id
#
#     )
#     return render(req,"serch_language.html",{"langs":res})
def search_by_name(req):
    param = req.GET
    res = Language.objects.filter(
        name__contains=param.get("tid")
    )
    return render(req,"serch_language.html",{"langs":res})
from django.http import HttpResponse
from django.shortcuts import render
from .models import FireCart
# Create your views here.
def my_carts(req):
    #拿火车数据
    data = FireCart.objects.filter(speed__lte=280).order_by("speed")
    #准备返回数据
    result = {
        "title":"火cart",
        "carts":data
    }
    return render(req,"trains.html",result)

def search_by_name(req):
    #获取get请求参数
    param = req.GET
    kw = param.get("kw")
    #根据参数 去搜索数据
    # res = FireCart.objects.filter(
    #     name__contains=kw
    # )
    # res = FireCart.objects.filter(
    #     name__endswith=kw
    # )
    # res = FireCart.objects.filter(speed__in=[300,251])
    #查询2018年的数据
    res = FireCart.objects.filter(create_date__year=1018)
    return render(req,"trains.html",{"carts":res})
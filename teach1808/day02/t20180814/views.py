from django.shortcuts import render
from .models import Goods
# Create your views here.
def my_goods(req):
    #拿数据
    data = Goods.objects.all()
    #返回数据
    result = {
        "title":"商品",
        "shangpin":data
    }
    return render(req,"thegoods.html",result)
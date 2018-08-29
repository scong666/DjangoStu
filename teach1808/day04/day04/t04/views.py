from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse

from .models import *
# Create your views here.

def my_as(req):
    my_data = MyAs.objects.all()
    #拿到模板
    tmp = loader.get_template("myas.html")
    print(tmp)
    my_str = tmp.render({"ass":my_data})
    my_code = "<h2>呵呵</h2>"
    my_code1 = "<script>alert('智商占领制高点')</script>"
    #my_str = tmp.render({"ass": []})
    my_str = tmp.render({"ass": my_data,"code":my_code})
    print(my_str)
    return HttpResponse(my_str)
    #return render(req,"myas.html",{"ass":my_data})


def my_search(req,hh1,hh2):
    print(hh1,hh2)
    #拿参数
    kw = req.GET.get("kw","")
    #拿数据
    data = MyAs.objects.filter(
        #name__contains=kw
        Q(name__contains=kw) | Q(ac__name__contains=kw)
    )
    return render(req,"homework.html",{"ass":data})

#重定向
def index(req):
    # return HttpResponseRedirect(reverse("python1808:ashehe"))
    # return HttpResponseRedirect("/t04/abs")
    return redirect(reverse("python1808:hzn",kwargs={"hh2":23,"hh1":30}))

def get_as_by_id(req,a_id,extra):
    #获取空姐ID
    aid = int(a_id)
    #根据id 拿到空姐的信息
    my_as = MyAs.objects.get(id=aid)
    #返回跟前端
    return HttpResponse(my_as.name+extra)


def home(req):
    return render(req,"child.html")
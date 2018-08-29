from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.views import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .decorators import api_permission_check


# Create your views here.
def login_view(req):
    if req.method == "GET":
        return render(req,"login.html")
    else:
        param = req.POST
        uname = param.get("uname")
        pwd = param.get("pwd")
        print(uname)
        print(pwd)
        user = authenticate(username=uname,password=pwd)
        if user:
            login(req,user)
            return redirect("/t10/welcome")
            # return HttpResponse("ok")
        else:
            return HttpResponse("error")

# @login_required(login_url="/t10/login")
# @api_permission_check(2)

def welcome(req):
    user = req.user
    return HttpResponse("欢迎"+user.username)
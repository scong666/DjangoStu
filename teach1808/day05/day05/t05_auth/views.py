from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def register_api(req):
    if req.method == "GET":
        return render(req,"user/register.html")
    else:
        # 获取post请求参数
        params  = req.POST
        u_name = params.get("u_name")
        pwd = params.get("pwd")
        c_pwd = params.get("confirm_pwd")
        # 检验用户名
        if len(u_name) >= 3:
            # 用户名是不是被人注册了
            # exists方法判断你查询的数据有没有
            if User.objects.filter(username=u_name).exists():
                return HttpResponse("坚持住，这名不能用")
            else:
                # 如果没有查到 校验密码
                # print(pwd)
                if pwd and len(pwd) > 3 and pwd == c_pwd:
                    # 校验通过 创建用户
                    User.objects.create_user(
                        username=u_name,
                        password=pwd
                    )
                else:
                    return HttpResponse("两次密码不一致")

        #跳转到登录页
            # return redirect(reverse("t05_auth:login"))
            return HttpResponse("注册成功")
        else:
            return HttpResponse("用户名长度过短")

def login_api(req):
    if req.method == "GET":
        return render(req,"user/login.html")
    else:
        # 登录逻辑
        params = req.POST
        u_name = params.get("uname")
        pwd = params.get("pwd")
        # 校验数据长度
        if pwd and len(pwd) >= 3 and u_name and len(u_name) >= 3 :
            # 校验用户
            user = authenticate(username = u_name,password = pwd)
            if user:
                # 校验通过 获得用户 可让用户登录
                login(req,user)
                return render(req,'index.html',{"u_name":user.username})
            else:
                return render(req,"user/login.html")
        else:
            return HttpResponse("用户名或密码过短")

def logout_api(req):
    logout(req)
    return render(req,'index.html',{"u_name":"游客"})
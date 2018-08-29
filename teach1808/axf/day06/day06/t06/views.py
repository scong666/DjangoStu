import hashlib

import os

from django.conf import settings
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

import uuid
# Create your views here.
def my_login(req):
    if req.method == "GET":
        return render(req,"login.html")
    else:
        # 处理登录了逻辑
        param = req.POST
        uname = param.get("uname")
        pwd = param.get("pwd")
        #验证用户
        user = authenticate(
            username=uname,
            password=pwd
        )
        if user:
            login(req,user)
            return HttpResponse("欢迎{u_name}".format(u_name=user.username))
        else:
            return HttpResponse("账号或密码错误")

#添加一个装饰器
@login_required(login_url="/t06/login")
def get_login_user(req):
    user = req.user
    print(user)
    return HttpResponse("欢迎{u_name}".format(u_name=user.username))

@login_required(login_url="/t06/login")
def upload_img_v1(req):
    if req.method == "GET":
        u_name = req.user.username
        # icon = req.user.icon.url
        #先拿到访问的域名
        tmp = req.user.icon
        icon = tmp.url if tmp else ""
        # icon = req.user.icon.url

        host = req.get_host()
        icon_str="http://" + host + "/static/imgs/" + icon
        print(icon)
        # return render(
        #     req,"uploadimg.html",
        #     {"uname":u_name}
        #     )

        return render(
            req, "uploadimg.html",
            {"uname": u_name, 'u_icon': icon_str}
        )
    else:
        #拿文件数据
        my_img = req.FILES.get("img")
        #知道是谁在上传照片
        user = req.user
        #头像数据保存在对应的icon字段上
        user.icon = my_img
        # 保存修改
        user.save()
        return HttpResponse("ok")

def get_unique_name():
    uuid_val = uuid.uuid4()
    uuid_str = str(uuid_val).encode("utf-8")
    #获取一个md5
    # md5 = hashlib.md5()
    md5 = hashlib.md5()
    # 将uuid的字符串 做摘要
    md5.update(uuid_str)
    # 返回32位15进制结果
    return md5.hexdigest()


def upload_img_v2(req):
    if req.method == "POST":
        # 获得照片
        img = req.FILES.get("img")
        file_name = get_unique_name() + ".png"
        # file_path = os.path.join(settings.MEDIA_ROOT,"hehe.png")
        file_path = os.path.join(settings.MEDIA_ROOT,file_name)
        with open(file_path,'wb') as fp:
            for i in img.chunks():
                fp.write(i)
            print(file_path)
            return HttpResponse("ok")

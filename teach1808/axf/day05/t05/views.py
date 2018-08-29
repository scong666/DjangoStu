from django.http import HttpResponse, HttpResponseRedirect, QueryDict, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.urls import reverse



def game(req):
    return render(req,"2048.html")

def testreq(request):
    # request 请求对象
    # print(dir(request))
    # print(request.method)#打印请求方法
    # print(request.POST)#POST请求
    # print(request.COOKIES)#打印cookie
    # print(request.META.get("REMOTE_ADDR"))#客户端IP
    # print(request.FILES)
    # print("--------")
    # param = QueryDict(request.body)
    # print(param)
    # print(request.path)#拿请求路径
    # print(request.get_host())#拿请求的域名加端口
    # print(request.get_port())#访问的端口
    # return HttpResponse("ok")

    # response响应对象
    # response = HttpResponse()
    # response.content = "别玩了，学习"
    # response.status_code = 404
    # response.write("!!!玩")
    # response.flush()
    # response.content = "藏猫猫"
    # return response

    my_dict = {"key":"呵呵"}
    return JsonResponse(my_dict)

#首页API
def index(req):
    user_name = req.COOKIES.get("uname","游客")
    # 读取session
    data = req.session.get("msg")
    print(data)
    return render(req,"index.html",{"u_name":user_name})

def login_api(req):
    # 如果是get请求 就返回页面
    if req.method == "GET":
        return render(req,"login.html")
    else:
        # 如果是post请求就去处理登录逻辑
        param = req.POST
        u_name = param.get("uname")
        pwd = param.get("pwd")
        # 设置session
        req.session['msg'] = "ok"
        # 假装这里有校验 并且校验通过
        response = HttpResponseRedirect("/t05/index")
        # 设置cookie 并在十秒后过期
        response.set_cookie("uname",u_name,max_age=2)
        return response
# 退出
def logout_api(req):
    response = HttpResponseRedirect(reverse("t05:index"))
    del req.session["msg"]
    # 删除uname对应的cookie
    response.delete_cookie("uname")
    return response
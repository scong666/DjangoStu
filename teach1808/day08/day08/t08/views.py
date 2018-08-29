import time

from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail, send_mass_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# from .models import Book
from django.db import connection

# Create your views here.
from django.template import loader
from django.views.decorators.cache import cache_page

from .util import create_random_str

def index(req):
    return render(req,"RTF.html")

#缓存60秒，60秒后还需在睡3秒
@cache_page(60)
def home(req):
    #模拟查询速度慢的情况
    time.sleep(3)
    return HttpResponse("开心")

def fetch_to_dict(cursor):
    colums = [i[0] for i in cursor.description]
    return [dict(zip(colums,row)) for row in cursor.fetchall()]

def ys_cache(req):
    data = cache.get("data")
    if data:
        return HttpResponse(data)
    else:
        time.sleep(3)
        # 获取数据库连接
        cursor = connection.cursor()
        # 执行sql语句
        cursor.execute("SELECT name FROM t08_book")
        # res = cursor.fetchall()
        res = fetch_to_dict(cursor)
        print(res)
        cache.set("data",res[0].get("name"),20)
        return HttpResponse("ok")

def send_my_email(req):
    email_addr = req.GET.get("addr")
    title = "python1808offer"
    msg = "恭喜您在千锋占座成功"
    #发送者
    email_from = settings.DEFAULT_FROM_EMAIL
    #接受者
    recevies = [email_addr]
    send_mail(
        title,
        msg,
        email_from,
        recevies,
        fail_silently=False
    )
    data = {
        "code":1,
        "msg":"邮件发送成功",
        "data":[]
    }
    return JsonResponse(data)

def sendmail(req):
    return render(req,"sendemail.html")

def send_email_v2(req):
    addr = req.GET.get("addr")
    #加载我们Email 模板页面
    templte = loader.get_template("emtemplate.html")
    #渲染
    html = templte.render({"mail":addr})

    title = "python1808offer"
    msg = ""
    # 发送者
    email_from = settings.DEFAULT_FROM_EMAIL
    # 接受者
    recevies = [addr]
    send_mail(
        title,
        msg,
        email_from,
        recevies,
        html_message=html,
        fail_silently=False
    )
    data = {
        "code": 1,
        "msg": "邮件发送成功",
        "data": []
    }
    return JsonResponse(data)

def send_many_email(req):
    msgl = (
        "标题1",
        "消息体1",
        settings.DEFAULT_FROM_EMAIL,
        ['1605786112@qq.com','1060800291@qq.com']
    )
    msg2 = (
        "标题2",
        "消息体2",
        settings.DEFAULT_FROM_EMAIL,
        ['1533482125@qq.com','357870436@qq.com']
    )
    send_mass_mail((msgl,msg2),fail_silently=False)
    return HttpResponse("本是共根生")


def create_confirm_email(req):
    addr = req.GET.get('addr')
    code = create_random_str()
    url = "http://{host}/t08/confirm/{random_str}".format(
        host=req.get_host(),
        random_str=code
    )
    # 发送邮件
    tmp = loader.get_template("emtemplate.html")
    html = tmp.render({"mail":"恭喜加入了会员","url":url})
    title = "会员激活"
    msg = ""
    # 发送者
    email_from = settings.DEFAULT_FROM_EMAIL
    # 接受者
    recevies = [addr]
    send_mail(
        title,
        msg,
        email_from,
        recevies,
        html_message=html,
        fail_silently=False
    )
    #设置缓存
    cache.set(code,addr,30)
    data = {
        "code": 1,
        "msg": "邮件发送成功",
        "data": []
    }
    return JsonResponse(data)

def confirm_api(req,p1):
    # 去缓存拿p1对应的值
    res = cache.get(p1)
    if res:
        #根据res去找对应的用户 然后给用户的状态变成激活态
        return HttpResponse("激活成功，送30000元")
    else:
        return HttpResponse("验证链接无效")
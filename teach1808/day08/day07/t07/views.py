import os
import random

from PIL import Image,ImageDraw,ImageFont
from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render
from .models import Person
from .util import get_random_color

import io
# Create your views here.
from .models import Person

PAGE_PEER_NUM = 10
def persons_api(req,current_page):
    #拿到全部数据
    persons = Person.objects.all()

    #实例化分页对象
    paginator = Paginator(
        persons,
        PAGE_PEER_NUM
    )
    # 需要知道用户点了第几页的数字按钮，所以我需要前端传递页码的参数
    datas = []
    try:
        page = paginator.page(current_page)
        datas = page.object_list
    except:
        pass

    data = {
        "persons":datas,#page.object_list,
        "page_range":paginator.page_range,
        "page":page,
        "last_page":paginator.num_pages
    }
    return render(req,"paginator.html",data)


def get_confirm_img(req):
    #有一个颜色
    # bg = (255,0,0)
    bg = get_random_color()
    #设置画布大小
    img_size = (130,45)
    #实例化一个画布
    image = Image.new("RGB",img_size,bg)

    #实例化一个画笔
    draw = ImageDraw.Draw(image)
    #实例化字体
    font_path = os.path.join(settings.BASE_DIR,"static/fonts/ADOBEARABIC-BOLDITALIC.OTF")
    font_size = 30
    my_font = ImageFont.truetype(font_path,font_size)

    #画一个字母
    # font_color = (0,255,0)

    source = "zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP1234567890"
    loop = 4
    confirm_code = ""
    for i in range(loop):
        #生成一个随机数字
        tmp = random.randrange(len(source))
        #获得随机数字对应下标的字母
        tmp_str = source[tmp]
        # 记录生成的每个字符
        confirm_code += tmp_str
        print("confirm is ", confirm_code)
        #生成字母的随机颜色
        font_color = get_random_color()
        #将字母画到画布
        draw.text((15+30*i,10), tmp_str, font_color, font=my_font)
    # draw.text((20,10),"shang",font_color,font=my_font)

    #保存
    buf = io.BytesIO()
    #将图片保存到io流里
    image.save(buf,"png")

    # 设置session 将生成的四位验证码保存到session里
    req.session["c_code"] = confirm_code

    # content_type告诉浏览器我这是个图片，png格式
    return HttpResponse(buf.getvalue(),content_type="image/png")

def my_login(req):
    return render(req,"login.html")

def confirm_api(req):
# 先拿到用户传递过来的参数
    user_code = req.POST.get("code")
# 从session里拿生成的验证码字符
    bg_code = req.session.get("c_code")
# 不区分大小写 验证lower
    if user_code.lower() == bg_code.lower():
        data = {
            "code":1,
            "msg":"ok",
            "data":[]
        }
        return JsonResponse(data)
    else:
        data = {
            "code":2,
            "msg":"验证码错误",
            "data":[]
        }
        return JsonResponse(data)
# 根据不同的比对结果不同的反馈
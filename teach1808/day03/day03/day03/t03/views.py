import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import Avg
from .models import Player, Team, Person, IdCard, Book, Author
from django.forms import model_to_dict

# Create your views here.

def get_player_avg_age(res):
    #拿国家队的数据
    players = Player.objects.filter(team__name="国家队")
    #求年纪平均
    res = players.aggregate(Avg("age"))
    print(res)
    #使用自定义的类管理对象去创建数据
    #p = Player.my_obj.create_player("三胖")
    #print(p)
    return HttpResponse(json.dumps(res))


def get_teams(req):
    #需要查询全部的球队数据
    data = Team.objects.raw("select * from t03_team")
    return render(req,"teams.html",{"teams":data})

def get_players_by_tid(req):
    #解析参数
    param = req.GET
    t_id = param.get("tid")
    #去找队员team_id对应的数据
    res = Player.objects.filter(
        team_id = int(t_id)
    )
    return render(req,"players.html",{"players":res})

def get_idcard_by_person(req):
    #先找个人的数据
    p = Person.objects.all().last()
    #获取身份证
    my_card = p.idcard
    print(my_card)
    return HttpResponse(my_card.num)

def get_person_by_card(req):
    #先获得的身份证数据
    card = IdCard.objects.get(pk=1)
    #通过身份证去拿人的信息
    p = card.person
    print(type(p))
    #让对象转成字典
    res = model_to_dict(p)
    print(type(res))
    return HttpResponse(json.dumps(res))

#删人的数据
def delete_person():
    person = Person.objects.all().last()
    #删除数据
    person.delete()
    return HttpResponse("ok")

#删身份证
def delete_card(req):
    card = IdCard.objects.all().first()
    card.delete()
    return HttpResponse("oko")

def get_player_by_team(req):
    #拿id是1的队伍
    team = Team.objects.get(pk=1)
    #通过队伍 拿运动员数据
    #players = team.player_set.all().values("name")
    players = team.player_set.all()
    print(dir(players))
    #print(type(players))
    #res = [model_to_dict(i) for i in players]
    #return JsonResponse(players)
    #return HttpResponse(json.jumps(players))
    return HttpResponse(players)

def get_author_by_book(req):
    book = Book.objects.get(pk=1)
    print(dir(book.author))
    print(book.author.all())
    return HttpResponse("ok")

def get_book_by_author(req):
    #拿作者
    author = Author.objects.get(id=1)
    #通过作者取书 Book类名小写_set.all() 拿到全部
    res = author.book_set.all()
    return HttpResponse(res)
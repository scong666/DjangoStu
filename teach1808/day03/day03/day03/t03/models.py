from django.db import models

# Create your models here.

class PlayerManger(models.Model):
    def create_player(self,u_name):
        p = Player()
        p.name = u_name
        p.age = 18
        p.team_id = 1
        p.is_live = True
        p.save()
        return p

class Team(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="球名"
    )
    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="名字"
    )
    age = models.IntegerField(
        verbose_name="年纪"
    )
    is_live = models.BooleanField(
        verbose_name="是否现役"
    )
    team = models.ForeignKey(
        Team,
        null=True,
        verbose_name="归属球队"
    )
    obj = models.Manager()
    my_obj = PlayerManger()
    objects = models.Manager()
    def __str__(self):
        return self.name

class IdCard(models.Model):
    num = models.CharField(
        max_length=19,
        verbose_name="身份证号"
    )
    org = models.CharField(
        max_length=30,
        verbose_name="签发单位"
    )

class Person(models.Model):
    name = models.CharField(
        max_length=30
    )
    idcard = models.OneToOneField(
        IdCard,
        on_delete=models.PROTECT
    )

class Author(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="名字"
    )
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(
        verbose_name="书的标题",
        max_length=30
    )
    author = models.ManyToManyField(
        Author,
        verbose_name="作者"
    )
    def __str__(self):
        return self.title

class Humen(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="人名"
    )
    age = models.IntegerField(
        verbose_name="年纪"
    )
    height = models.FloatField(
        verbose_name="身高"
    )
    class Meta:
        #声明此类是抽象类
        abstract = True

class Boy(Humen):
    salary = models.CharField(
        max_length=20
    )

class Boy(Humen):
    salary = models.CharField(
        max_length=20
    )

class Girl(Humen):
    face_score = models.IntegerField(
        verbose_name="颜值"
    )
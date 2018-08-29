from django.contrib.auth.models import AbstractUser
from django.db import models
# 权限
from .choices import PERMISSION
# Create your models here.

class AxfUser(AbstractUser):
    phone = models.CharField(
        verbose_name="手机号",
        max_length=12,
        null=True
    )
    address = models.CharField(
        verbose_name="地址",
        max_length=200,
        null=True
    )
    permission = models.IntegerField(
        verbose_name="权限",
        choices=PERMISSION,
        default=1  #默认都是普通用户
    )
    icon = models.ImageField(
        upload_to="icons",
    )

# axf_wheel(img,name,trackid)
class BaseData(models.Model):
    img = models.CharField(
        max_length=255
    )
    name = models.CharField(
        max_length=40
    )
    trackid = models.CharField(
        max_length=10
    )
    # 声明之后认为是抽象类
    class Meta:
        abstract = True

# 轮播图
class MyWheel(BaseData):

    class Meta:
        db_table = "axf_wheel"

class MyNav(BaseData):

    class Meta:
        db_table = "axf_nav"

class MustBuy(BaseData):

    class Meta:
        db_table ="axf_mustbuy"

class Shop(BaseData):
    class Meta:
        db_table = "axf_shop"

class MainShow(BaseData):
    categoryid = models.CharField(
        max_length=100
    )
    brandname = models.CharField(
        max_length=100
    )

    img1 = models.CharField(
        max_length=255
    )
    childcid1 = models.CharField(
        max_length=100
    )
    productid1 = models.CharField(
        max_length=100
    )
    longname1 = models.CharField(
        max_length=100
    )
    price1 = models.CharField(
        max_length=100
    )
    marketprice1 = models.CharField(
        max_length=100
    )

    img2 = models.CharField(
        max_length=255
    )
    childcid2 = models.CharField(
        max_length=100
    )
    productid2 = models.CharField(
        max_length=100
    )
    longname2 = models.CharField(
        max_length=100
    )
    price2 = models.CharField(
        max_length=100
    )
    marketprice2 = models.CharField(
        max_length=100
    )
    img3 = models.CharField(
        max_length=255
    )
    childcid3 = models.CharField(
        max_length=100
    )
    productid3 = models.CharField(
        max_length=100
    )
    longname3 = models.CharField(
        max_length=100
    )
    price3 = models.CharField(
        max_length=100
    )
    marketprice3 = models.CharField(
        max_length=100
    )

    class Meta:
        db_table = "axf_mainshow"

class Goods(models.Model):
    productid = models.CharField(
        max_length=20
    )
    productimg = models.CharField(
        max_length=200
    )
    productname = models.CharField(
        max_length=200,
        null=True
    )
    productlongname = models.CharField(
        max_length=200
    )
    isxf = models.BooleanField(
        default=0
    )
    pmdesc = models.BooleanField(
        default=0
    )
    specifics = models.CharField(
        max_length=20
    )
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(
        max_length=10
    )
    dealerid = models.CharField(
        max_length=20
    )
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    current_num = models.IntegerField(
        default=0,
        verbose_name="当前显示数量"
    )

    def __str__(self):
        return str(self.price)

    class Meta:
        db_table = "axf_goods"


class GoodsTypes(models.Model):
    typeid = models.CharField(
        max_length=40
    )
    typename = models.CharField(
        max_length=10
    )
    childtypenames = models.CharField(
        max_length=200,
    )
    typesort = models.IntegerField()

    class Meta:
        db_table = "axf_foodtypes"


class Cart(models.Model):
    user = models.ForeignKey(
        AxfUser,
        verbose_name="用户",
    )
    goods = models.ForeignKey(
        Goods,
        verbose_name="商品"
    )
    num = models.IntegerField(
        verbose_name="数量",
        default=1
    )
    is_select = models.BooleanField(
        verbose_name="选中状态",
        default=True
    )
    class Meta:
        verbose_name = "购物车"
        # 建立索引
        index_together = ("user","is_select")


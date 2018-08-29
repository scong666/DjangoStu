from django.db import models

# Create your models here.
class Goods(models.Model):
    #字符串
    name = models.CharField(
        max_length=30,
        verbose_name="名字"
    )
    #整型
    price = models.IntegerField(
        verbose_name="价格",
        default=300,
        db_column="my_price"
    )
    #日期
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="生产日期"
    )
    #日期
    last_update = models.DateField(
        auto_now=True
    )
    #布尔值
    is_used = models.BooleanField(
        default=True,
        verbose_name = "是否再用"
    )
    def __str__(self):
        return self.name+str(self.price)
    class Meta:
        verbose_name="商品类"
        db_table="comm"
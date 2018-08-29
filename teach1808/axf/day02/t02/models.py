from django.db import models

# Create your models here.
class FireCart(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="名字"
    )
    speed = models.IntegerField(
        verbose_name="时速",
        default=300,
        db_column="my_speed"
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="出厂日期"
    )
    last_update = models.DateField(
        auto_now=True
    )
    is_used = models.BooleanField(
        default=True,
        verbose_name = "是否再用"
    )
    def __str__(self):
        return self.name+str(self.speed)
    class Meta:
        verbose_name="火车类"
        db_table="huocart"
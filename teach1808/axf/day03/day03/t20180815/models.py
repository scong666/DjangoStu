from django.db import models

# Create your models here.
class Language(models.Model):

    objects = models.Manager()
    name = models.CharField(
        max_length=30,
        verbose_name="语种"
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="日期"
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="语言类"
        db_table="languages"
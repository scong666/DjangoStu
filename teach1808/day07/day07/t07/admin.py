from django.contrib import admin
from .models import Person,Home
# Register your models here.

class PersonInfo(admin.TabularInline):
    model = Person
    extra = 3

class HomeAdmin(admin.ModelAdmin):
    inlines = [PersonInfo]

#针对于人的站点管理类
class PersonAdmin(admin.ModelAdmin):

    def get_oldmen(self):
        if self.age >= 18:
            return "精英"
        else:
            return "太嫩"

    #设置显示的字段
    list_display = ["name","age",get_oldmen]

    get_oldmen.short_description = "精英与否"
    #添加过滤条件
    list_filter = ["name"]
    search_fields = ["name"]
    list_per_page = 20
    ordering = ["age"]

    fieldsets = [
        ("人的名字",{"fields":("name",)}),
        ("年龄", {"fields": ("name",)})
    ]
# 将需要管理的类注册到站点管理
admin.site.register(Person,PersonAdmin)

admin.site.register(Home,HomeAdmin)
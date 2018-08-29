from django.conf.urls import url
from .views import my_goods
urlpatterns = [
    url(r"^hello$",my_goods)
]
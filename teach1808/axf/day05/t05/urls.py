from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^game$",game),
    url(r"^test$",testreq),
    url(r"^index$",index,name="index"),
    url(r"^login$",login_api,name="login"),
    url(r"^logut$",logout_api,name="logout")
]
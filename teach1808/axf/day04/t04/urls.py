from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^absiissss$",my_as,name="ashehe"),
    # url(r"^search$",my_search)
    url(r"^search/(?P<hh1>\d+)/(?P<hh2>\d+)$",my_search,name="hzn"),
    url(r"^index$",index,name="myindex"),
    url(r"getas/(\d+)/(.*)",get_as_by_id,name="getas"),
    url(r"^home$",home)
]
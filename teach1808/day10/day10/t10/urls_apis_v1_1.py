from django.conf.urls import url
from .apis_v1_1 import *

urlpatterns = [
    url(r"^admin$",AdminAPI.as_view())
]
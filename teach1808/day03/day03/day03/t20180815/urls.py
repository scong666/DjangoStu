from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^get_lang$",search_by_name)
]
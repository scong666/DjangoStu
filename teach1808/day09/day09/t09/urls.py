from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r"^index$",index),
    url(r"^test$",celery_test),
    url(r"^zp$",zp)
]
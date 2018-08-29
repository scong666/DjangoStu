from django.conf.urls import url
from .views import my_carts,search_by_name
urlpatterns = [
    url(r"^train$",my_carts),
    url(r"^getcart$",search_by_name)
]

from django.urls import path, include
from .views import pal
urlpatterns = [
    path("pal/",pal)

]

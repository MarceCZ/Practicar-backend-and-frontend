from django.urls import path
from .views import loginEndPoint,loginPathEndPoint

urlpatterns = [
    path("login/", loginEndPoint),
    path("login/<str:username>/<str:password>",loginPathEndPoint),
]
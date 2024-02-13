from django.urls import path
from .views import loginEndPoint,loginPathEndPoint, loginPostEndPoint, loginPostJsonEndPoint

urlpatterns = [
    path("login/", loginEndPoint),
    path("login/<str:username>/<str:password>",loginPathEndPoint),
    path("login-post",loginPostEndPoint),
    path("login-json",loginPostJsonEndPoint)
]
from django.urls import path
from .views import loginPostJsonEndPoint, loginEndPoint

urlpatterns = [
    path("login-json",loginPostJsonEndPoint),
    path("login",loginEndPoint)
]
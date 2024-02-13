from django.urls import path
from .views import loginPostJsonEndPoint

urlpatterns = [
    path("login",loginPostJsonEndPoint)
]
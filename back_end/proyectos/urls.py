from django.urls import path
from .views import loginEndPoint

urlpatterns = [
    path("login/", loginEndPoint),
]
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

usuarios = """
[
    {
        "username": "20210651",
        "password": "123"
    },
    {
        "username": "marce",
        "password": "abc"
    }
]
"""

def loginEndPoint(request):
    if request.method == "GET":
        username = request.GET.get("username")
        password = request.GET.get("password")

        listaUsers = json.loads(usuarios)
        listaUsersFiltrado = list(
            filter(
                lambda x: x["username"]==username and x["password"]==password,listaUsers
            )
        )
    
        if len(listaUsersFiltrado)>0:
            respuesta = {
                "msg": ""
            }
        else:
            respuesta = {
                "msg": "Error en el login"
        }
        return HttpResponse(json.dumps(respuesta))







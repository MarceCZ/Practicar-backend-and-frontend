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


#Path parameters
def loginPathEndPoint(request,username,password):
    if request.method == "GET":
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

@csrf_exempt
def loginPostEndPoint(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

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
    
#JSON
@csrf_exempt
def loginPostJsonEndPoint(request):
    if request.method == "POST":
        data = request.body
        userData = json.loads(data)

        username = userData["username"]
        password = userData["password"]

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

    







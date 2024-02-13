from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Usuario

def loginEndPoint(request):
    if request.method == "GET":
        username = request.GET.get("username")
        password = request.GET.get("password")

        listaUsers = Usuario.objects.filter(username=username,password=password)

        if len(listaUsers)>0:
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

        listaUsers = Usuario.objects.filter(username=username,password=password)

        if len(listaUsers)>0:
            respuesta = {
                "msg": ""
            }
        else:
            respuesta = {
                "msg": "Error en el login"
            }
        return HttpResponse(json.dumps(respuesta))
    
        

    







from django.shortcuts import render

def inicio(request):
    return render (request, "perez/inicio.html")
def registro(request):
    return render (request, "perez/formregistro.html")


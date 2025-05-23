from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def another(request):
    return HttpResponse(f"Usuario: {request.user} | ¿Autenticado? {request.user.is_authenticated}")

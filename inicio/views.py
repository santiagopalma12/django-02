from django.http import HttpResponse

def home(request):
    return HttpResponse("¡hola mundoo!")

def another(request):
    return HttpResponse(f"Usuario: {request.user} | ¿Autenticado? {request.user.is_authenticated}")

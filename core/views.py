from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def comunidad(request):
    return render(request, 'comunidad.html')

def tienda(request):
    return render(request, 'tienda.html')

def producto(request, id):
    return render(request, 'producto.html')

def entrada(request):
    return render(request, 'entrada.html')

def lobby(request):
    return render(request, 'lobby.html')

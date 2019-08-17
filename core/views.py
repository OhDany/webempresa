from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Web Empresarial</h1><h2>Home</h2>")

def about(request):
    return HttpResponse("<h1>About</h1><h2>Todo sobre nosotros</h2>")

def services(request):
    return HttpResponse("<h1>services</h1><h2>Todos nuestros servicios</h2>")

def store(request):
    return HttpResponse("<h1>Visitanos</h1><h2>Visita nuestra tienda</h2>")

def contact(request):
    return HttpResponse("<h1>Contact</h1><h2>Contacta con nosotros</h2>")

def blog(request):
    return HttpResponse("<h1>Blog</h1><h2>Nuestro blog</h2>")

def sample(request):
    return HttpResponse("<h1>Sample</h1><h2>Ejemplo de nuestros productos</h2>")
from django.shortcuts import render

# Create your views here.

# se crea la vista home que se encarga de renderizar la plantilla home.html de la aplicación agv.
def home(request):
    return render(request, 'agv/home.html')
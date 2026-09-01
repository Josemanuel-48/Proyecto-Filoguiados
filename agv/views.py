from django.shortcuts import render
# se importa el decorador login_required para proteger las vistas que requieren autenticación.
from django.contrib.auth.decorators import login_required

# Create your views here.

# se crea la vista home que se encarga de renderizar la plantilla home.html de la aplicación agv.
def home(request):
    return render(request, 'agv/home.html')
# se crea la vista dashboard que se encarga de renderizar la plantilla dashboard.html de la aplicación agv. 
# Esta vista requiere que el usuario esté autenticado para poder acceder a ella.
@login_required
def dashboard(request):
    return render(request, 'agv/dashboard.html')
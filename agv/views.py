from django.shortcuts import render
# se importa el decorador login_required para proteger las vistas que requieren autenticación.
from django.contrib.auth.decorators import login_required
# se importa el modelo RegistroParada para poder utilizarlo en las vistas que lo requieran.
from .models import RegistroParada
# se crea import para tener la fecha y hora actual en las vistas que lo requieran.
from django.utils import timezone
# se importa la función Avg para poder calcular la duración media de las paradas en el dashboard.
from django.db.models import Avg
from django.db.models import Avg, Count
# Create your views here.

# se crea la vista home que se encarga de renderizar la plantilla home.html de la aplicación agv.
def home(request):
    return render(request, 'agv/home.html')
# se crea la vista dashboard que se encarga de renderizar la plantilla dashboard.html de la aplicación agv. 
# Esta vista requiere que el usuario esté autenticado para poder acceder a ella.
@login_required
def dashboard(request):
    # se obtiene la fecha actual y se filtran los registros de paradas que ocurrieron en el día actual.
    hoy = timezone.now().date()
    # se cuenta el número de registros de paradas que ocurrieron en el día actual y se almacena en la variable paradas_hoy.
    paradas_hoy = RegistroParada.objects.filter(hora__date=hoy).count()
    # se calcula la duración media de las paradas que ocurrieron en el día actual y se almacena en la variable duracion_media.
    duracion_media = RegistroParada.objects.filter(hora__date=hoy).aggregate(Avg('duracion'))['duracion__avg']
    # se obtiene el segmento crítico, que es el sensor con mayor número de paradas en el día actual y cuya duración sea mayor a 20 segundos.
    segmento_critico = RegistroParada.objects.filter(hora__date=hoy, duracion__gt=20).values('sensor').annotate(total=Count('sensor')).order_by('-total').first()
    # se obtiene la lista de las últimas 10 paradas registradas en la base de datos, ordenadas por hora de manera descendente.
    ultimas_paradas = RegistroParada.objects.order_by('-hora')[:10]
    # se crea un diccionario con las variables paradas_hoy y duracion_media para pasarlas a la plantilla dashboard.html, añadiendo también el segmento crítico si existe y las últimas paradas registradas.
    return render(request, 'agv/dashboard.html', {'paradas_hoy': paradas_hoy, 'duracion_media': duracion_media, 'segmento_critico': segmento_critico, 'ultimas_paradas': ultimas_paradas})


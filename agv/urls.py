# se crea el archivo urls.py que contiene las rutas de la aplicación agv.

from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
# se define el nombre de la aplicación para poder referenciar las rutas desde otras aplicaciones.
app_name = 'agv'
# se definen las rutas de la aplicación agv, que corresponden a las vistas que se van a mostrar en la interfaz web.
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='agv/login.html'), name='login'),
    # se añade la ruta de logout para poder cerrar sesión desde la interfaz web.
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # se añade la ruta de dashboard para poder acceder a la vista dashboard desde la interfaz web.
    path('dashboard/', views.dashboard, name='dashboard'),
    # se añade la ruta de historico para poder acceder a la vista historico desde la interfaz web.  
    path('historico/', views.historico, name='historico'),

]
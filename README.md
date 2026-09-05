# Sistema de Monitorización AGV

Aplicación web desarrollada con Django que simula la monitorización en tiempo real de una flota de 3 AGVs (vehículos de guiado automático), registrando sus paradas y mostrando un panel de control con las incidencias detectadas.

## Stack tecnológico

- Python 3
- Django
- SQLite (base de datos)

## Instalación

1. Crear y activar un entorno virtual:
   ```
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
2. Instalar las dependencias del proyecto:
   ```
   pip install -r requirements.txt
   ```
3. Aplicar las migraciones:
   ```
   python manage.py migrate
   ```
4. Crear un superusuario (opcional, para acceder al panel de administración):
   ```
   python manage.py createsuperuser
   ```
5. Arrancar el servidor:
   ```
   python manage.py runserver
   ```

La aplicación queda disponible en `http://127.0.0.1:8000/`.

## Cuenta de demostración

Para probar la aplicación sin crear un usuario propio:

- **Usuario:** demo
- **Contraseña:** 012124striper

## Comandos propios del proyecto

- `python manage.py simular` — lanza la simulación de los 3 AGVs, generando paradas de forma continua en tiempo real.
- `python manage.py test agv` — ejecuta las pruebas mínimas del proyecto.

## Documentación completa

Ver `Documento_Entrega_AGV.md` para la explicación completa del proyecto (objetivos, stack, base de datos, requisitos, manual de instalación detallado y conclusiones).

"""
URL configuration for gaslicuado project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py  
from django.contrib import admin  
from django.urls import path  
from solicitudes import views  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('administrador/', views.lista_solicitud, name='administrador'), 
    path('solicitud/', views.crear_solicitud, name='crear_solicitud'),
    path('buscar/', views.buscar_solicitud, name='buscar_solicitud'),
    path('adm/solicitud/<int:id>/', views.detalles_solicitud, name='detalles_solicitud'),
    path('adm/solicitud/edit/<int:id>/', views.editar_solicitud, name='editar_solicitud'),
    path('adm/solicitud/delete/<int:id>/', views.delete_solicitud, name='eliminar_solicitud'),
    path('adm/solicitud/<int:id>/cambiar-estado/', views.cambiar_estado_solicitud, name='cambiar_estado'),
]
from django.shortcuts import render, redirect, get_object_or_404
from solicitudes.models import Solicitud
from django.http import HttpRequest
from datetime import timedelta
from django.utils import timezone

def inicio(request):
    titulo = "La Agrupación de Municipalidades de Chile"
    data = {'titulo': titulo}
    return render(request, 'inicio.html', data)

def buscar_solicitud(request: HttpRequest):  
    if request.method == 'POST':  
        rut = request.POST.get('rut')  
        solicitud = Solicitud.objects.filter(rut=rut).first()  
        return render(request, 'buscar.html', {'solicitud': solicitud}) 
    return render(request, 'buscar.html')


def lista_solicitud(request: HttpRequest):
    solicitudes = Solicitud.objects.all()

    # Verificar expiraciones antes de mostrar la lista
    for solicitud in solicitudes:
        if solicitud.estado == 'ACEPTADA' and solicitud.fecha_aceptacion:
            if solicitud.fecha_aceptacion + timedelta(days=30) < timezone.now().date():
                solicitud.estado = 'EXPIRADA'
                solicitud.save()

    data = {"solicitudes": solicitudes}
    return render(request, 'administrador.html', data)



def crear_solicitud(request: HttpRequest):  
    if request.method == 'POST':  
        rut = request.POST.get('rut')  
        nombre = request.POST.get('nombre')  
        apellidos = request.POST.get('apellido')  
        comuna = request.POST.get('comuna')  
        direccion = request.POST.get('direccion')  
        telefono = request.POST.get('telefono')  

        nueva_solicitud = Solicitud(
            rut=rut, nombre=nombre, apellidos=apellidos,
            comuna=comuna, direccion=direccion, telefono=telefono
        )
        nueva_solicitud.save()  
        return redirect('administrador')
    return render(request, 'solicitud.html')



def cambiar_estado_solicitud(request:HttpRequest, id: int):
    solicitud = get_object_or_404(Solicitud, id=id)
    if solicitud.estado == "Pendiente":
        solicitud.estado = "Aceptada"  
    elif solicitud.estado == "Aceptada":
        solicitud.estado = "Rechazada" 
    else:
        solicitud.estado = "Pendiente"
    solicitud.save()
    return redirect('detalles_solicitud', id=id)


def editar_solicitud(request: HttpRequest, id: int):  
    solicitud = get_object_or_404(Solicitud, id=id)  
    if request.method == 'POST':  
        solicitud.rut = request.POST.get('rut')  
        solicitud.nombre = request.POST.get('nombre')  
        solicitud.apellidos = request.POST.get('apellido')  
        solicitud.comuna = request.POST.get('comuna')  
        solicitud.direccion = request.POST.get('direccion')  
        solicitud.telefono = request.POST.get('telefono')  
        solicitud.save()  
        return redirect('detalles_solicitud', id=id)  
    return render(request, 'editar_solicitud.html', {'solicitud': solicitud})

def delete_solicitud(request: HttpRequest, id: int):  
    solicitud = get_object_or_404(Solicitud, id=id)  
    if request.method == 'POST':  
        solicitud.delete()  
        return redirect('administrador')  
    return render(request, 'eliminar_solicitud.html', {'solicitud': solicitud})


def detalles_solicitud(request: HttpRequest, id: int):
    solicitud = get_object_or_404(Solicitud, id=id)

    if solicitud.estado == 'ACEPTADA' and solicitud.fecha_aceptacion:
        if solicitud.fecha_aceptacion + timedelta(days=30) < timezone.now().date():
            solicitud.estado = 'EXPIRADA'
            solicitud.save()

    return render(request, 'detalles_solicitud.html', {'solicitud': solicitud})

def administrador(request):  
    return render(request, 'administrador.html')  
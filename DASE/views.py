from django.shortcuts import render

# Usar objectos "Q"
from django.db.models import Q

# Models
from DASE.models import estudiantes

# Verificacion de datos del excel
import math


def home(request):
    return render(request, 'home.html')


def busqueda(request):

    # Query para solicitar los valores que contendran  los select
    c = estudiantes.objects.values('carrera').distinct()
    b = estudiantes.objects.values('tipo_beneficio').distinct()
    t = estudiantes.objects.values('trimestre').distinct()

    if request.method == 'POST':

        # Recuperar los valores ingresados
        input_text = request.POST['data']
        s1 = request.POST.getlist('select_carrera')
        s2 = request.POST.getlist('select_beneficio')
        s3 = request.POST.getlist('select_trimestre')
        s4 = request.POST['select_order']

        # Inicializando variable donde se guardará el query
        query = Q()

        # Construcción del query a partir de las opciones ingresadas por el usuario

        if (input_text):
            for i in input_text.split(" "):
                if (i.isdigit()):
                    query |= Q(cedula=i)
                elif (not i.isdigit() and i != ''):
                    query |= Q(nombre__icontains=i)

        if (s1):
            query &= Q(carrera__in=s1)
        if (s2):
            query &= Q(tipo_beneficio__in=s2)
        if (s3):
            query &= Q(trimestre__in=s3)

        print(query)

        # Solicitando los datos a la base de datos
        if(s4):
            datos = estudiantes.objects.filter(query).order_by(s4)
        else:
            datos = estudiantes.objects.filter(query).order_by("cedula")

        # Si no se encentran resultados se muestra un mensaje al usuario
        if not datos:
            messages.info(
                request, "No hay resultados que coincidan con su búsqueda")

        return render(request, 'busqueda.html', {"c": c, "b": b, "t": t, "search": datos})

    else:
        return render(request, 'busqueda.html', {"c": c, "b": b, "t": t})


def more_info(request, cedula):
    # Busca toda la información relacionada con el estudiante solicitado
    estudiante = estudiantes.objects.filter(cedula=cedula)
    return render(request, 'more_info.html', {"estudiante": estudiante})

from django.shortcuts import render

# Models
from DASE.models import estudiantes

from django.db.models import Sum, Count
from django.db.models import Q

# Verificar que el usuario esta logueado
from django.contrib.auth.decorators import login_required

# Mostrar mensajes en pantalla
from django.contrib import messages


@login_required
def graficas(request):

    if request.method == 'POST':

        # INFORMACION DE LOS SELECT
        s1 = request.POST['group']
        s2 = request.POST.getlist('select_carreras')
        s3 = request.POST.getlist('select_beneficios')
        s4 = request.POST['tipo_grafica']
        t = request.POST['titulo']

        # SOLICITANDO LOS DATOS A LA BASE DE DATOS

        # FILTROS (WHERE) DEL QUERY

        query = Q()

        if (s2):
            query &= Q(carrera__in=s2)

        if (s3):
            query &= Q(tipo_beneficio__in=s3)

        # print(query)

        data = estudiantes.objects.values(s1).filter(
            query).annotate(cantidad=Count('cedula'))

        if data:
            v = []

            # GUARDANDO INFORMACION EN LAS VARIABLES
            for i in data:
                v.append([i[s1], i['cantidad']])

            datos = v

            # Opciones visuales de la gráfica
            # Si la grafica es 3D
            dimension = 'true'

        else:
            messages.info(
                request, "No hay resultados que coincidan con su búsqueda")
            return render(request, 'graficas.html')

        # return render(request, 'google.html', {'values': [['foo', 32], ['bar', 64], ['baz', 96]] })
        return render(request, 'graficas.html', {'values': datos, 'titulo': t, 'dimension': dimension, 'tipo_grafica': s4})

    else:
        return render(request, 'graficas.html')

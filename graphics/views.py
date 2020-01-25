from django.shortcuts import render

# Models
from DASE.models import estudiantes

from django.db.models import Sum, Count
from django.db.models import Q

# Verificar que el usuario esta logueado
from django.contrib.auth.decorators import login_required


@login_required
def graficas(request):

    if request.method == 'POST':

        # INFORMACION DE LOS SELECT
        s1 = request.POST['primary']
        s2 = request.POST.getlist('secondary')
        s3 = request.POST['tipo_grafica']
        t = request.POST['titulo']

        # SOLICITANDO LOS DATOS A LA BASE DE DATOS

        # FILTROS (WHERE) DEL QUERY

        query = Q()

        if (s2):
            if(s1 == "carrera"):
                query = Q(carrera__in=s2)
            else:
                query = Q(tipo_beneficio__in=s2)

        # print(query)

        data = estudiantes.objects.values(s1).filter(
            query).annotate(cantidad=Count('cedula'))

        v = []

        # GUARDANDO INFORMACION EN LAS VARIABLES
        for i in data:
            v.append([i[s1], i['cantidad']])

        datos = v

        # Opciones visuales de la gráfica
        tipo_grafica = ""
        dimension = 'true'  # Si la grafica es 3D

        # return render(request, 'google.html', {'values': [['foo', 32], ['bar', 64], ['baz', 96]] })
        return render(request, 'graficas.html', {'values': datos, 'titulo': t, 'dimension': dimension, 'tipo_grafica': s3})

    else:
        return render(request, 'graficas.html')

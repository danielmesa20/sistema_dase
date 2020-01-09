from django.shortcuts import render

#Mostrar mensajes en pantalla
from django.contrib import messages

#Models
from DASE.models import beca_excelencia
from django.db.models import Sum

def graficas(request):

    datos  = buscar_datos()
    
    if request.method == 'POST':
        #return render(request, 'google.html', {'values': [['foo', 32], ['bar', 64], ['baz', 96]] })
        return render(request, 'google.html', {'values': datos})
    else:
        return render(request, 'google.html', {'values': datos})


def buscar_datos():

    # VARIABLE PARA GUARDAR LA INFORMACION A GRAFICAR
    v = []

    # SOLUCITANDO LOS DATOS A LA BASE DE DATOS

    # SELECT carrera, SUM(CEDULA) AS d FROM beca_excelencia GROUP BY carrera
    data = beca_excelencia.objects.values('carrera').annotate(d=Sum('cedula')) 
    
    # GUARDANDO INFORMACION EN LAS VARIABLES
    for i in data:
        v.append( [i['carrera'] , i['d'] ] )
        
    return (v)


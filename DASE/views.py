from django.shortcuts import render, redirect

#Usar objectos "Q"
from django.db.models import Q 

#Leer archivo excel 
import pandas as pd

#Mostrar mensajes en pantalla
from django.contrib import messages

#Models
from DASE.models import estudiantes

#Verificacion de datos del excel
import math

def home (request):
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

        #Inicializando variable donde se guardará el query
        query = Q()
    
        # Construcción del query a partir de las opciones ingresadas por el usuario

        if (input_text):
            for i in input_text.split(" "):
                if (i.isdigit()):
                    query |= Q(cedula = i) 
                elif (not i.isdigit() and i != ''):
                    query |= Q(nombre__icontains = i)
                
        if (s1):
            query &= Q(carrera__in = s1)
        if (s2):
            query &= Q(tipo_beneficio__in = s2)
        if (s3):
            query &= Q(trimestre__in = s3)

        print(query)

        # Solicitando los datos a la base de datos
        if(s4):
            datos = estudiantes.objects.filter(query).order_by(s4)
        else:
            datos = estudiantes.objects.filter(query).order_by("cedula")

        # Si no se encentran resultados se muestra un mensaje al usuario
        if not datos:
            messages.info(request,"No hay resultados que coincidan con su búsqueda")
            
        return render(request, 'busqueda.html', { "c": c , "b": b, "t": t, "search": datos})

    else:
        return render(request, 'busqueda.html', { "c": c , "b": b, "t": t })

def more_info(request, cedula):
    estudiante = estudiantes.objects.filter(cedula=cedula)
    return render(request, 'more_info.html', {"estudiante":estudiante})

#IMPORTAR DATOS DEL ARCHIVO DE EXCEL A LA BASE DE DATOS
def  import_excel (request):

    if request.method == 'POST':

        #IMPORTANDO ARCHIVO EXCEL
        xls = request.FILES['excel']

        #LEYENDO TODAS LAS HOJAS DEL EXCEL
        datos = pd.read_excel(xls, sheet_name=None) 

        # RECORRIENDO LAS HOJAS DEL EXCEL, i = "p1", "p2", data[i] = datos hoja "i"
        for h in datos: 

            # VERIFICANDO QUE LOS DATOS DE LA HOJA "h" NO TENGAN ERRORES
            if  verificacion_datos(datos[h], request, h) == False: 

                # SI NO HAY ERRORES ENTONCES SE INSERTAN LOS DATOS DE LA HOJA "h" en la base de datos

                c = 0  # CONTADOR
                aux = datos[h]

                #SE VAN RECORRIENDO Y GUARDANDO LOS DATOS DE LA HOJA
                for _ in aux['cedula']: 

                    if h == 'p1':
                        print("p1")
                        
                    elif h == 'p2':
                        prueba = beca_excelencia(cedula=aux['cedula'][c], nombre=aux['nombre'][c], carrera=aux['carrera'][c])
                        prueba.save()

                    c = c + 1

    return render(request, 'import.html')

#VERIFICAR SI HAY ERRORES EN LA INFORMACION DE LA HOJA
def verificacion_datos(data, request, hoja):

    e = False   # Si hay errores 

    for i in data['cedula']:
    
        # VERIFICAR EL TIPO DE DATO DEL CAMPO CEDULA
        if  type(i) not in (int, float):
            messages.info(request, 'El tipo de dato de cedula está mal en la  hoja %s' %(hoja))
            e = True

        # VERIFICAR SI EL CAMPO CEDULA ESTÁ VACIO
        elif math.isnan(i):
            messages.info(request, 'Falta el dato cedula en la hoja %s' %(hoja))
            e = True
        
    return e
                
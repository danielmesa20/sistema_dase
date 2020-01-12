from django.shortcuts import render, redirect

#from django.db.models import Q  #Usar objectos "Q"

#Importar archivo excel con pandas
import pandas as pd

#Mostrar mensajes en pantalla
from django.contrib import messages

#Models
from DASE.models import beca_excelencia
from DASE.models import estudiantes

#Verificacion de datos
import math

def home (request):
    return render(request, 'home.html')

def busqueda(request):

    #Query con los valores de los select
    c = estudiantes.objects.values('carrera').distinct()
    b = estudiantes.objects.values('tipo_beneficio').distinct()
    t = estudiantes.objects.values('trimestre').distinct()

    if request.method == 'POST':

        #Recuperar los valores ingresados
        input_text = request.POST['data']
        s1 = request.POST['select_carrera']
        s2 = request.POST['select_beneficio']
        s3 = request.POST['select_trimestre']

        #Verificacion 
        aux = []
    
        #Verificacion 
        aux = []

        if not input_text  and s1  == "all" and s2  == "all" and s3  == "all":          #Buscar todos los estudiantes
            datos = estudiantes.objects.all()

        elif input_text and input_text.isdigit() == False:                      
                if s1 == "all" and s2 == "all" and s3 == "all":                         #Buscar solo por el nombre
                    datos = estudiantes.objects.filter(nombre__icontains = input_text)

                elif s1 != "all" and s2 == "all" and s3 == "all":                       #Buscar por el nombre y la carrera
                    datos = estudiantes.objects.filter(nombre__icontains = input_text, carrera = s1)
                    
                elif s1 != "all" and s2 != "all" and s3 == "all":                       #Buscar por el nombre, la carrera, tipo de beneficio
                    datos = estudiantes.objects.filter(nombre__icontains = input_text ,carrera = s1, tipo_beneficio = s2)
                    
                elif s1 != "all" and s2 != "all" and s3 != "all":                       #Buscar por el nombre, la carrera, tipo de beneficio y trimestre
                    datos = estudiantes.objects.filter(nombre__icontains = input_text, carrera = s1, tipo_beneficio = s2, trimestre = s3)
                    
                elif s1 == "all" and s2 != "all" and s3 == "all":                       #Buscar por el nombre y el tipo de beneficio 
                    datos = estudiantes.objects.filter(nombre__icontains = input_text, tipo_beneficio = s2)

                elif s1 != "all" and s2 == "all" and s3 != "all":                       #Buscar por el nombre, la carrera y  por el trimestre
                    datos = estudiantes.objects.filter(nombre__icontains = input_text, carrera = s1, trimestre = s3)

                elif s1 == "all" and s2 != "all" and s3 != "all":                       #Buscar por el nombre, tipo de beneficio y por el trimestre
                    datos = estudiantes.objects.filter(nombre__icontains = input_text, tipo_beneficio = s2, trimestre = s3)

                elif s1 == "all" and s2 == "all" and s3 != "all":                       #Buscar por el nombre y el trimestre
                    datos = estudiantes.objects.filter(nombre__icontains = input_text, trimestre = s3)

        elif input_text and input_text.isdigit():

                input_text = int(input_text)                                            #Pasar de string a integer

                if s1 == "all" and s2 == "all" and s3 == "all":                         #Buscar solo por el cedula
                    datos = estudiantes.objects.filter(cedula = input_text)
                    
                elif s1 != "all" and s2 == "all" and s3 == "all":                       #Buscar por la cedula y la carrera
                    datos = estudiantes.objects.filter(cedula = input_text, carrera = s1)

                elif s1 != "all" and s2 != "all" and s3 == "all":                       #Buscar por la cedula, la carrera, tipo de beneficio
                    datos = estudiantes.objects.filter(cedula = input_text, carrera = s1, tipo_beneficio = s2)

                elif s1 != "all" and s2 != "all" and s3 != "all":                       #Buscar por la cedula, la carrera, tipo de beneficio y trimestre
                    datos = estudiantes.objects.filter(cedula = input_text, carrera = s1, tipo_beneficio = s2 ,trimestre = s3)

                elif s1 == "all" and s2 != "all" and s3 == "all":                       #Buscar por la cedula y el tipo de beneficio 
                    datos = estudiantes.objects.filter(cedula = input_text, tipo_beneficio = s2)

                elif s1 != "all" and s2 == "all" and s3 != "all":                       #Buscar por la cedula, la carrera y  por el trimestre
                    datos = estudiantes.objects.filter(cedula = input_text, carrera = s1, trimestre = s3)

                elif s1 == "all" and s2 != "all" and s3 != "all":                       #Buscar por la cedula, tipo de beneficio y por el trimestre
                    datos = estudiantes.objects.filter(cedula = input_text, tipo_beneficio = s2, trimestre = s3)

                elif s1 == "all" and s2 == "all" and s3 != "all":                       #Buscar por la cedula y el trimestre
                    datos = estudiantes.objects.filter(cedula = input_text, trimestre = s3)

        else:
                if s1 != "all" and s2 == "all" and s3 == "all":                         #Buscar por la carrera
                    datos = estudiantes.objects.filter(carrera = s1)

                elif s1 != "all" and s2 != "all" and s3 == "all":                       #Buscar por la carrera y el tipo de beneficio
                    datos = estudiantes.objects.filter(carrera = s1, tipo_beneficio = s2)

                elif s1 != "all" and s2 != "all" and s3 != "all":                       #Buscar la carrera, tipo de beneficio y trimestre
                    datos = estudiantes.objects.filter(carrera = s1, tipo_beneficio = s2, trimestre = s3)

                elif s1 == "all" and s2 != "all" and s3 == "all":                       #Buscar por el tipo de beneficio 
                    datos = estudiantes.objects.filter(tipo_beneficio = s2)

                elif s1 != "all" and s2 == "all" and s3 != "all":                       #Buscar por la carrera y  por el trimestre
                    datos = estudiantes.objects.filter(carrera = s1, trimestre = s3)

                elif s1 == "all" and s2 != "all" and s3 != "all":                       #Buscar por el tipo de beneficio y por el trimestre
                    datos = estudiantes.objects.filter(tipo_beneficio = s2, trimestre = s3)

                elif s1 == "all" and s2 == "all" and s3 != "all":                       #Buscar por  el trimestre
                    datos = estudiantes.objects.filter(trimestre = s3)

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
                
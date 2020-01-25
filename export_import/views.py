from django.shortcuts import render

# Leer archivo excel
import pandas as pd

# Mostrar mensajes en pantalla
from django.contrib import messages

# IMPORTAR DATOS DEL ARCHIVO DE EXCEL A LA BASE DE DATOS

from django.contrib.auth.decorators import login_required


@login_required
def import_excel(request):

    if request.method == 'POST':

        # IMPORTANDO ARCHIVO EXCEL
        xls = request.FILES['excel']

        # LEYENDO TODAS LAS HOJAS DEL EXCEL
        datos = pd.read_excel(xls, sheet_name=None)

        # RECORRIENDO LAS HOJAS DEL EXCEL, i = "p1", "p2", data[i] = datos hoja "i"
        for h in datos:

            # VERIFICANDO QUE LOS DATOS DE LA HOJA "h" NO TENGAN ERRORES
            if verificacion_datos(datos[h], request, h) == False:

                # SI NO HAY ERRORES ENTONCES SE INSERTAN LOS DATOS DE LA HOJA "h" en la base de datos

                c = 0  # CONTADOR
                aux = datos[h]

                # SE VAN RECORRIENDO Y GUARDANDO LOS DATOS DE LA HOJA
                for _ in aux['cedula']:

                    if h == 'p1':
                        print("p1")

                    elif h == 'p2':
                        prueba = beca_excelencia(
                            cedula=aux['cedula'][c], nombre=aux['nombre'][c], carrera=aux['carrera'][c])
                        prueba.save()

                    c = c + 1

    return render(request, 'import.html')


# VERIFICAR SI HAY ERRORES EN LA INFORMACION DE LA HOJA
def verificacion_datos(data, request, hoja):

    e = False   # Si hay errores

    for i in data['cedula']:

        # VERIFICAR EL TIPO DE DATO DEL CAMPO CEDULA
        if type(i) not in (int, float):
            messages.info(
                request, 'El tipo de dato de cedula está mal en la  hoja %s' % (hoja))
            e = True

        # VERIFICAR SI EL CAMPO CEDULA ESTÁ VACIO
        elif math.isnan(i):
            messages.info(
                request, 'Falta el dato cedula en la hoja %s' % (hoja))
            e = True

    return e
